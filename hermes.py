#!/usr/bin/env python3
"""
Hermes — asistente de IA sobre la boveda de Obsidian de MaGa.

Plan B confirmado 2026-08-24: el paquete "hermes-agent" de PyPI no es lo que
describia el material original (es un framework generico de Nous Research,
sin relacion con Obsidian). Este script reemplaza esa dependencia: usa el SDK
oficial de Anthropic directo, con herramientas propias de lectura/escritura
de archivos apuntando a la carpeta sincronizada por Nextcloud.

Uso:
    python hermes.py "organiza mi inbox de esta semana"
    python hermes.py                      (modo conversacion interactiva)
    python hermes.py --doctor             (verifica que todo este bien configurado)
"""

import os
import sys
import json
from pathlib import Path

VAULT_PATH = Path(os.environ.get("HERMES_VAULT_PATH", r"D:\Obsidian Vault"))
MODEL = "claude-sonnet-5"
MAX_TURNS = 12


def die(msg: str) -> None:
    print(f"[hermes] {msg}", file=sys.stderr)
    sys.exit(1)


def check_setup() -> None:
    problems = []
    if not os.environ.get("ANTHROPIC_API_KEY"):
        problems.append(
            "ANTHROPIC_API_KEY no esta configurada. Ponla como variable de "
            "entorno de usuario en Windows (Panel de Control > Sistema > "
            "Variables de entorno), nunca pegada en el chat."
        )
    if not VAULT_PATH.exists():
        problems.append(f"No se encontro la boveda en: {VAULT_PATH}")
    try:
        import anthropic  # noqa: F401
    except ImportError:
        problems.append("Falta el paquete 'anthropic' (pip install anthropic).")

    if problems:
        print("[hermes doctor] Problemas encontrados:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"[hermes doctor] Todo bien. Boveda: {VAULT_PATH}")


def _safe_path(rel_path: str) -> Path:
    """Evita que Claude escriba fuera de la boveda por accidente."""
    target = (VAULT_PATH / rel_path).resolve()
    if VAULT_PATH.resolve() not in target.parents and target != VAULT_PATH.resolve():
        raise ValueError(f"Ruta fuera de la boveda, rechazada: {rel_path}")
    return target


def tool_list_notes(folder: str = "") -> str:
    base = _safe_path(folder) if folder else VAULT_PATH
    if not base.exists():
        return f"La carpeta no existe: {folder}"
    entries = []
    for p in sorted(base.rglob("*.md")):
        entries.append(str(p.relative_to(VAULT_PATH)))
    return "\n".join(entries) if entries else "(sin notas .md en esa carpeta)"


def tool_read_note(path: str) -> str:
    target = _safe_path(path)
    if not target.exists():
        return f"No existe: {path}"
    return target.read_text(encoding="utf-8", errors="replace")


def tool_write_note(path: str, content: str) -> str:
    target = _safe_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"Guardado: {path} ({len(content)} caracteres)"


def tool_search_notes(query: str) -> str:
    query_lower = query.lower()
    hits = []
    for p in VAULT_PATH.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if query_lower in text.lower():
            snippet_idx = text.lower().find(query_lower)
            start = max(0, snippet_idx - 60)
            end = min(len(text), snippet_idx + 60)
            snippet = text[start:end].replace("\n", " ")
            hits.append(f"{p.relative_to(VAULT_PATH)}: ...{snippet}...")
    if not hits:
        return f"Sin resultados para: {query}"
    return "\n".join(hits[:25])


TOOLS = [
    {
        "name": "list_notes",
        "description": "Lista las notas .md dentro de una carpeta de la boveda (o toda la boveda si se omite).",
        "input_schema": {
            "type": "object",
            "properties": {"folder": {"type": "string", "description": "Ruta relativa a la boveda, ej. '00 Inbox'"}},
        },
    },
    {
        "name": "read_note",
        "description": "Lee el contenido completo de una nota, dada su ruta relativa a la boveda.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "write_note",
        "description": "Crea o sobreescribe una nota con el contenido dado, en la ruta relativa a la boveda.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "search_notes",
        "description": "Busca un texto/palabra clave en todas las notas de la boveda, devuelve archivo + fragmento.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
]

TOOL_FUNCS = {
    "list_notes": lambda **kw: tool_list_notes(kw.get("folder", "")),
    "read_note": lambda **kw: tool_read_note(kw["path"]),
    "write_note": lambda **kw: tool_write_note(kw["path"], kw["content"]),
    "search_notes": lambda **kw: tool_search_notes(kw["query"]),
}

SYSTEM_PROMPT = f"""Eres Hermes, el asistente personal de MaGa que trabaja sobre su boveda \
de Obsidian ("segundo cerebro"), sincronizada via Nextcloud en {VAULT_PATH}.

La boveda esta organizada asi:
- Sistema/ -> contexto (CLAUDE.md si existe)
- 00 Inbox/ -> bandeja de entrada, ideas sueltas
- 01 Projects/ -> un subfolder por proyecto activo (Homelab, Santa Diabla, Poker Academy, \
Mitos y Leyendas, Coworker_Siemens, TDAH Helper, Amazon, YouTube Faceless, Agustin the Hotdog)
- 02 Areas/, 03 Resources/, 04 Archive/

Responde siempre en espanol, tono directo y natural (venezolano/latinoamericano, nunca "vosotros"). \
Usa las herramientas para leer y escribir notas reales en vez de inventar contenido. Antes de \
escribir una nota nueva, revisa si ya existe algo relacionado con list_notes/search_notes. \
Confirma siempre, en tu respuesta final, que archivos leiste o escribiste."""


def run_agent_turn(client, messages: list) -> str:
    import anthropic

    for _ in range(MAX_TURNS):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        if response.stop_reason != "tool_use":
            final_text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            return final_text

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            func = TOOL_FUNCS.get(block.name)
            try:
                result = func(**block.input) if func else f"Herramienta desconocida: {block.name}"
            except Exception as exc:  # noqa: BLE001
                result = f"Error ejecutando {block.name}: {exc}"
            print(f"  [herramienta] {block.name}({block.input}) -> {str(result)[:120]}")
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                }
            )
        messages.append({"role": "user", "content": tool_results})

    return "(Se alcanzo el limite de pasos sin terminar — revisa manualmente.)"


def main() -> None:
    if "--doctor" in sys.argv:
        check_setup()
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        die("Falta ANTHROPIC_API_KEY. Corre 'python hermes.py --doctor' para mas detalle.")

    import anthropic

    client = anthropic.Anthropic()
    messages: list = []

    query = " ".join(a for a in sys.argv[1:] if not a.startswith("--"))
    if query:
        messages.append({"role": "user", "content": query})
        answer = run_agent_turn(client, messages)
        print(f"\nHermes: {answer}\n")
        return

    print("Hermes listo. Escribe tu pregunta (Ctrl+C para salir).")
    while True:
        try:
            user_input = input("\nTu: ")
        except (KeyboardInterrupt, EOFError):
            print("\nHasta luego.")
            break
        if not user_input.strip():
            continue
        messages.append({"role": "user", "content": user_input})
        answer = run_agent_turn(client, messages)
        print(f"\nHermes: {answer}")
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
