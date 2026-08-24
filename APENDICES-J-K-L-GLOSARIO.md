# Apéndices Finales - Migración, Modelos Locales, Referencia y Glosario

## Apéndice J: Migración desde Otros Sistemas

### 📦 Importar tu Conocimiento Existente

#### 1. Migración desde Notion

**Exportar desde Notion:**

1. Notion → Settings & Members → Settings
2. Export all workspace content
3. Export format: **Markdown & CSV**
4. Include subpages: ✅
5. Create folders for subpages: ✅
6. Export

**Convertir a formato Obsidian:**

```bash
# Instalar herramienta
npm install -g notion-to-md

# Convertir
notion-to-md \
  --input "./Notion_Export" \
  --output "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\03-Recursos\Desde-Notion"
```

**Script de limpieza (Python):**

```python
# Script: clean-notion-export.py
import os
import re

def clean_notion_md(file_path):
    """Limpia formato de Notion para Obsidian"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convertir links de Notion a Obsidian
    content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\.md\)', r'[[\1]]', content)
    
    # Remover IDs de Notion
    content = re.sub(r'\s+[a-f0-9]{32}', '', content)
    
    # Convertir checkboxes
    content = content.replace('☑', '- [x]')
    content = content.replace('☐', '- [ ]')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Procesar todos los archivos
import_folder = "\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\03-Recursos\\Desde-Notion"
for root, dirs, files in os.walk(import_folder):
    for file in files:
        if file.endswith('.md'):
            clean_notion_md(os.path.join(root, file))

print("✅ Archivos limpiados")
```

---

#### 2. Migración desde Evernote

**Exportar desde Evernote:**

1. Evernote → File → Export Notes
2. Format: **Evernote XML Format (.enex)**
3. Include tags: ✅
4. Export

**Convertir con Yarle:**

```bash
# Instalar Yarle
npm install -g yarle

# Convertir
yarle \
  --enexSource "./Evernote_Export.enex" \
  --outputDir "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\03-Recursos\Desde-Evernote" \
  --isMetadataNeeded true \
  --isNotebookNameNeeded true \
  --isZettelkastenNeeded false
```

**Resultado:**

```markdown
---
source: evernote
notebook: Trabajo
tags: [proyecto, importante]
created: 2024-01-15
updated: 2026-08-09
---

# Título de la Nota

[Contenido convertido]
```

---

#### 3. Migración desde OneNote

**Exportar desde OneNote:**

1. Cada sección → File → Export → PDF o Word
2. Convierte múltiples secciones

**Convertir Word/PDF a Markdown:**

```bash
# Instalar Pandoc
choco install pandoc  # Windows
brew install pandoc   # Mac

# Convertir archivo Word
pandoc documento.docx -o documento.md

# Por lote
for file in *.docx; do
    pandoc "$file" -o "${file%.docx}.md"
done
```

---

#### 4. Migración desde Google Keep

**Exportar con Google Takeout:**

1. https://takeout.google.com
2. Deselect all → Select "Keep"
3. Next → Export once
4. Download

**Script de conversión:**

```python
# Script: convert-google-keep.py
import json
import os
from datetime import datetime

keep_export = "./Takeout/Keep"
output_folder = "\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox\\Desde-Keep"

for file in os.listdir(keep_export):
    if file.endswith('.json'):
        with open(os.path.join(keep_export, file), 'r', encoding='utf-8') as f:
            note = json.load(f)
        
        title = note.get('title', 'Sin título')
        content = note.get('textContent', '')
        created = note.get('createdTimestampUsec', 0) / 1000000
        created_date = datetime.fromtimestamp(created).strftime('%Y-%m-%d')
        
        # Labels to tags
        labels = note.get('labels', [])
        tags = [f"#{label['name'].replace(' ', '-')}" for label in labels]
        
        md_content = f"""---
fuente: google-keep
fecha: {created_date}
etiquetas: {tags}
---

# {title}

{content}
"""
        
        safe_title = title.replace('/', '-').replace('\\', '-')
        output_file = os.path.join(output_folder, f"{created_date}-{safe_title}.md")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)

print("✅ Google Keep convertido")
```

---

#### 5. Migración desde Apple Notes

**Exportar con Exporter:**

```bash
# Instalar Exporter (Mac only)
brew install apple-notes-exporter

# Exportar
apple-notes-exporter \
  --output "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\03-Recursos\Desde-AppleNotes" \
  --format markdown
```

---

#### 6. Migración desde Bear

**Exportar desde Bear:**

1. Bear → File → Export Notes
2. Format: **Markdown**
3. Export

Bear ya usa Markdown, solo necesitas:

```bash
# Copiar archivos
cp -r ~/Bear-Export/* "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\03-Recursos\Desde-Bear"

# Convertir tags de Bear (#tag#) a Obsidian (#tag)
find . -name "*.md" -exec sed -i 's/#\([^#]*\)#/#\1/g' {} \;
```

---

### 📋 Checklist Post-Migración

Después de importar:

- [ ] Revisar enlaces rotos
- [ ] Verificar imágenes importadas
- [ ] Limpiar metadata innecesaria
- [ ] Reorganizar en estructura PARA
- [ ] Agregar etiquetas faltantes
- [ ] Eliminar duplicados
- [ ] Crear índice de contenido migrado
- [ ] Hacer backup antes de limpiar

---

## Apéndice K: Modelos Locales con Ollama

### 🏠 Ejecutar IA Localmente (Sin Costo)

#### 1. ¿Qué es Ollama?

**Ollama** permite ejecutar modelos de IA (como Llama, Mistral, etc.) **localmente** en tu computadora, **sin internet** y **sin costo de API**.

**Ventajas:**
- ✅ Gratis (sin límites de uso)
- ✅ Privacidad total (datos no salen de tu máquina)
- ✅ Sin internet necesario
- ✅ Control total

**Desventajas:**
- ❌ Requiere hardware potente (16GB+ RAM recomendado)
- ❌ Modelos menos capaces que Claude/GPT
- ❌ Más lento
- ❌ Consume recursos locales

---

#### 2. Instalación de Ollama

**Windows:**

```powershell
# Descargar desde: https://ollama.ai/download/windows
# O con winget:
winget install Ollama.Ollama

# Verificar
ollama --version
```

**Mac:**

```bash
# Descargar desde: https://ollama.ai/download/mac
# O con Homebrew:
brew install ollama

# Verificar
ollama --version
```

**Iniciar servicio:**

```bash
# Inicia el servidor Ollama
ollama serve
```

---

#### 3. Descargar Modelos

```bash
# Modelos recomendados:

# Llama 3.1 8B (requiere ~8GB RAM)
ollama pull llama3.1:8b

# Mistral 7B (requiere ~7GB RAM)
ollama pull mistral:7b

# Phi-3 Mini (requiere ~4GB RAM) - más ligero
ollama pull phi3:mini

# Gemma 2 9B (requiere ~9GB RAM)
ollama pull gemma2:9b

# Ver modelos descargados
ollama list
```

---

#### 4. Configurar Hermes con Ollama

**Editar config de Hermes:**

```yaml
# ~/.hermes/config.yaml

# Configuración para Ollama (local)
local_mode:
  enabled: true
  provider: ollama
  model: llama3.1:8b
  endpoint: http://localhost:11434
  
# Alternar entre Claude y Ollama
mode: local  # O 'cloud' para Claude

# Fallback automático
fallback:
  enabled: true
  # Si Ollama falla, usar Claude
  cloud_provider: anthropic
```

**O crear perfil separado:**

```yaml
# Perfiles
profiles:
  default:
    provider: anthropic
    model: claude-sonnet-4-8
    
  local:
    provider: ollama
    model: llama3.1:8b
    
  fast:
    provider: ollama
    model: phi3:mini
    
# Usar perfil
# hermes --profile local "pregunta"
```

---

#### 5. Comparación: Claude vs Ollama

| Aspecto | Claude (Cloud) | Ollama (Local) |
|---------|---------------|----------------|
| **Costo** | ~$5-20/mes | Gratis |
| **Privacidad** | Datos en cloud | 100% local |
| **Velocidad** | Muy rápido | Depende de tu PC |
| **Calidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| **Internet** | Requerido | No necesario |
| **Setup** | Fácil | Moderado |
| **Hardware** | No importa | 16GB+ RAM ideal |

---

#### 6. Casos de Uso Recomendados

**Usa Claude para:**
- ✅ Análisis complejos
- ✅ Generación de contenido largo
- ✅ Razonamiento avanzado
- ✅ Código complejo
- ✅ Tareas críticas

**Usa Ollama para:**
- ✅ Tareas simples/repetitivas
- ✅ Procesar inbox
- ✅ Organizar notas
- ✅ Etiquetar automáticamente
- ✅ Resúmenes básicos
- ✅ Cuando no tienes internet
- ✅ Datos ultra sensibles

---

#### 7. Workflow Híbrido

**Automatizar con script:**

```python
# Script: hybrid-ai.py
import subprocess
import os

def ask_ai(question, use_local=False):
    """Pregunta a Claude o Ollama según preferencia"""
    
    if use_local:
        # Usar Ollama
        result = subprocess.run(
            ['ollama', 'run', 'llama3.1:8b', question],
            capture_output=True,
            text=True
        )
        return result.stdout
    else:
        # Usar Claude via Hermes
        result = subprocess.run(
            ['hermes', 'ask', question],
            capture_output=True,
            text=True
        )
        return result.stdout

# Ejemplos
# Tarea simple → Ollama (gratis)
summary = ask_ai("Resume esta nota en 3 puntos", use_local=True)

# Tarea compleja → Claude (mejor calidad)
analysis = ask_ai("Analiza arquitectura de este sistema", use_local=False)
```

---

## Apéndice L: Cheat Sheet / Referencia Rápida

### ⚡ Guía de Consulta Rápida

#### Comandos Esenciales de Hermes

```bash
# Crear nota
hermes create nota "Título" --folder "01-Proyectos/HomeLab"

# Buscar
hermes search "keyword"

# Leer nota
hermes read "ruta/nota.md"

# Listar notas
hermes list --folder "01-Proyectos" --tag "activo"

# Organizar inbox
hermes organize inbox

# Generar resumen
hermes summarize --folder "01-Proyectos/HomeLab"

# Análisis
hermes analyze "¿Cuál es el estado de mis proyectos?"
```

---

#### Atajos de Teclado Obsidian

| Acción | Windows | Mac |
|--------|---------|-----|
| Crear nota | `Ctrl+N` | `Cmd+N` |
| Buscar | `Ctrl+O` | `Cmd+O` |
| Paleta comandos | `Ctrl+P` | `Cmd+P` |
| Vista previa | `Ctrl+E` | `Cmd+E` |
| Abrir link | `Ctrl+Click` | `Cmd+Click` |
| Backlinks | `Ctrl+Alt+←` | `Cmd+Option+←` |
| Graph view | `Ctrl+G` | `Cmd+G` |
| Buscar en archivos | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Abrir settings | `Ctrl+,` | `Cmd+,` |

---

#### Sintaxis Markdown Esencial

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold**
*Italic*
==Highlight==
~~Strikethrough~~

- Lista
- Sin orden

1. Lista
2. Ordenada

- [ ] Checkbox
- [x] Checked

[[Internal Link]]
[External Link](https://url.com)

![Image](image.png)

> Quote

`inline code`

```language
code block
```

---
Separador

| Table | Header |
|-------|--------|
| Cell  | Cell   |
```

---

#### Dataview Queries Comunes

**Listar proyectos activos:**

````markdown
```dataview
LIST
FROM #proyecto
WHERE estado = "activo"
SORT fecha DESC
```
````

**Tabla de tareas:**

````markdown
```dataview
TABLE fecha, prioridad, estado
FROM #tarea
WHERE !completed
SORT prioridad DESC, fecha ASC
```
````

**Reuniones del mes:**

````markdown
```dataview
TABLE participantes, proyecto
FROM #reunión
WHERE fecha >= date(today) - dur(30 days)
SORT fecha DESC
```
````

---

#### Solución Rápida de Problemas

| Problema | Solución |
|----------|----------|
| Hermes no responde | `hermes restart` |
| API key inválida | Regenerar en console.anthropic.com |
| NAS desconectado | Verificar red, reiniciar Drive Client |
| Sync no funciona | Plugin Git → Pull/Push manual |
| Obsidian lento | Deshabilitar plugins no usados |
| Links rotos | Buscar `[[` y verificar rutas |
| Git conflictos | `git status` → resolver manualmente |

---

#### Rutas Importantes

```bash
# Windows
C:\Users\mgabi\.hermes\             # Config Hermes
C:\Users\mgabi\AppData\Local\Obsidian\  # Obsidian
\\192.168.1.100\Obsidian-Vault\     # NAS

# Mac
~/.hermes/                          # Config Hermes
~/Library/Application Support/obsidian/  # Obsidian
/Volumes/Obsidian-Vault/            # NAS
```

---

## Glosario de Términos

### 📚 Definiciones Clave

**API (Application Programming Interface)**
Interfaz que permite a aplicaciones comunicarse entre sí. Hermes usa la API de Claude.

**API Key**
Clave secreta que autentica tu acceso a la API de Claude. NO compartir.

**Bóveda (Vault)**
Carpeta principal donde Obsidian guarda todas tus notas.

**Caché / Caching**
Almacenamiento temporal de datos para reutilizar y reducir costos de API.

**CLAUDE.md**
Archivo de configuración donde defines instrucciones personalizadas para Claude.

**Dataview**
Plugin de Obsidian que permite consultas tipo base de datos sobre tus notas.

**DSM (DiskStation Manager)**
Sistema operativo de los NAS Synology.

**Frontmatter**
Metadatos en formato YAML al inicio de una nota Markdown, entre `---`.

**Git**
Sistema de control de versiones que rastrea cambios en archivos.

**GitHub**
Plataforma en la nube para alojar repositorios Git.

**Hermes**
Agente de IA que conecta Obsidian con Claude, permitiendo gestión inteligente de notas.

**Inbox**
Carpeta donde capturas ideas rápidamente antes de organizarlas (00-Inbox).

**LLM (Large Language Model)**
Modelo de IA entrenado con grandes cantidades de texto (ej: Claude, GPT).

**Markdown**
Lenguaje de marcado ligero para formatear texto (`.md` archivos).

**MOC (Map of Content)**
Nota que sirve como índice o mapa de otras notas sobre un tema.

**NAS (Network Attached Storage)**
Dispositivo de almacenamiento conectado a red. Tu Synology DS723+.

**Nota Atómica**
Nota que contiene una sola idea, principio de Zettelkasten.

**Obsidian**
Aplicación de notas que usa Markdown y funciona localmente.

**PARA**
Sistema de organización: Projects, Areas, Resources, Archive.

**Plugin**
Extensión que agrega funcionalidad a Obsidian.

**Prompt**
Instrucción o pregunta que envías a una IA.

**Prompt Caching**
Técnica de Claude que reutiliza prompts para reducir costos 90%.

**Repository (Repo)**
Proyecto versionado con Git. Tu bóveda puede ser un repo.

**Segundo Cerebro**
Sistema para capturar, organizar y conectar conocimiento externamente.

**SMB**
Protocolo de red para compartir archivos (usado por NAS).

**Snippet**
Fragmento pequeño de código o texto reutilizable.

**Synology Drive**
App de Synology para sincronizar archivos entre dispositivos y NAS.

**Tag / Etiqueta**
Marcador (#palabra) para categorizar notas.

**Template / Plantilla**
Estructura predefinida para crear notas consistentes.

**Templater**
Plugin avanzado de Obsidian para plantillas con lógica.

**Token**
Unidad de texto que la IA procesa. ~4 caracteres = 1 token.

**Vault → Ver Bóveda**

**Wikilink**
Enlace interno de Obsidian: `[[nombre-nota]]`

**YAML**
Formato de datos usado en frontmatter de Markdown.

**Zettelkasten**
Método de toma de notas basado en notas atómicas interconectadas.

---

## 🎉 Conclusión de los Apéndices

Has completado todos los apéndices adicionales:

✅ **Apéndice B:** Plantillas y Sistemas de Organización
✅ **Apéndice C:** Plugins Esenciales
✅ **Apéndice D:** Seguridad y Privacidad
✅ **Apéndice E:** Monitoreo de Costos
✅ **Apéndice F:** Workflows Avanzados
✅ **Apéndice G:** Integraciones
✅ **Apéndice H:** Control de Versiones Git
✅ **Apéndice I:** Casos de Uso por Profesión
✅ **Apéndice J:** Migración desde Otros Sistemas
✅ **Apéndice K:** Modelos Locales (Ollama)
✅ **Apéndice L:** Cheat Sheet
✅ **Glosario:** Términos Técnicos

---

### Recursos Adicionales

**Comunidades:**
- r/ObsidianMD (Reddit)
- Obsidian Forum (forum.obsidian.md)
- Discord de Obsidian

**YouTube:**
- Linking Your Thinking (Nick Milo)
- Bryan Jenks
- Sergio Duque (español)

**Blogs:**
- obsidian.rocks
- betterhumans.pub

---

**¡Tu sistema Hermes + Obsidian + Claude está completo!** 🚀
