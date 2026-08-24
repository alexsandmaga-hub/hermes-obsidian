# Apéndices Adicionales - Git y Casos de Uso

## Apéndice H: Control de Versiones con Git

### 🗂️ Historial Completo de tu Segundo Cerebro

#### 1. Configuración Inicial de Git

**Windows:**
```powershell
# Descargar desde: https://git-scm.com/download/win
# O con Chocolatey:
choco install git

# Verificar
git --version
```

**Mac:**
```bash
# Con Homebrew
brew install git
git --version
```

**Configurar Git globalmente:**

```bash
# Tu información
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@gmail.com"

# Editor (opcional)
git config --global core.editor "code --wait"  # VS Code
```

---

#### 2. Inicializar Repositorio

```powershell
# Navegar a tu bóveda en el NAS
cd "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro"

# Inicializar Git
git init

# Crear .gitignore
@"
# Obsidian
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.trash/

# Sistema
.DS_Store
Thumbs.db
desktop.ini

# Hermes
.hermes/cache/
.hermes/temp/

# Temporales
*.tmp
~$*
"@ | Out-File -FilePath .gitignore -Encoding utf8

# Primer commit
git add .
git commit -m "Initial commit - Mi Segundo Cerebro

Estructura inicial
- Carpetas: Proyectos, Areas, Recursos, Archivo
- Plantillas configuradas
- CLAUDE.md configurado

Co-Authored-By: Claude <oz-agent@warp.dev>"
```

---

#### 3. Conectar con GitHub

**Crear repositorio en GitHub:**
1. https://github.com/new
2. Nombre: `mi-segundo-cerebro` (privado ✅)
3. NO inicialices con README
4. Create repository

**Conectar:**

```bash
# Agregar remote
git remote add origin https://github.com/tu-usuario/mi-segundo-cerebro.git

# Configurar rama
git branch -M main

# Push inicial
git push -u origin main
```

**Autenticación:**

```bash
# GitHub: Settings → Developer settings → Personal access tokens
# Generate new token → "repo" → Generate

# Configurar credential helper:
git config --global credential.helper wincred  # Windows
git config --global credential.helper osxkeychain  # Mac
```

---

#### 4. Workflow Diario

```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Commit
git commit -m "HomeLab: Agregar configuración Proxmox

- Documentar instalación
- Agregar diagrama de red
- Checklist de tareas

Co-Authored-By: Claude <oz-agent@warp.dev>"

# Push a GitHub
git push
```

**Convención de mensajes:**
```
<proyecto>: <acción>

- Detalle 1
- Detalle 2

Co-Authored-By: Claude <oz-agent@warp.dev>
```

**Ejemplos:**
- `HomeLab: Agregar documentación Docker`
- `Plantillas: Mejorar template reuniones`
- `Inbox: Procesar 15 notas`

---

#### 5. Plugin Obsidian Git (Recomendado)

**Instalación:**
1. Settings → Community Plugins → Browse
2. "Obsidian Git" → Install → Enable

**Configuración:**

```
✅ Auto pull: Every 10 minutes
✅ Auto save: Every 5 minutes
✅ Auto push: Every 10 minutes
✅ Pull updates on startup

Commit message: "Auto: {{date}} {{time}}"
Commit Author: "Tu Nombre <tu-email@gmail.com>"
```

**Beneficios:**
- Auto-commits cada 5 min
- Auto-push a GitHub
- Auto-pull (sincroniza dispositivos)
- Historial completo
- Cero esfuerzo

---

#### 6. Revertir Cambios

**Deshacer cambios locales:**

```bash
# Descartar cambios en archivo
git checkout -- archivo.md

# Descartar TODOS los cambios (⚠️)
git reset --hard HEAD
```

**Volver a versión anterior:**

```bash
# Ver historial
git log --oneline

# Revertir commit (crea nuevo commit)
git revert a1b2c3d

# Restaurar archivo específico
git checkout e4f5g6h -- archivo.md
```

---

#### 7. Branching para Experimentos

```bash
# Crear rama experimental
git checkout -b experimento-zettelkasten

# Hacer cambios...
# Commits...

# Volver a main
git checkout main

# Si te gustó, merge:
git merge experimento-zettelkasten

# Si no, eliminar:
git branch -d experimento-zettelkasten
```

---

## Apéndice I: Casos de Uso por Profesión

### 👨‍💻 Workflows Especializados

#### 1. Para Desarrolladores de Software

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Proyectos/
│   ├── App-Mobile/
│   ├── API-Backend/
│   └── DevOps-Infrastructure/
├── 02-Areas/
│   ├── Arquitectura/
│   ├── Code-Review/
│   └── Debugging/
├── 03-Recursos/
│   ├── Snippets/
│   │   ├── Python/
│   │   ├── JavaScript/
│   │   └── SQL/
│   ├── Patrones-de-Diseño/
│   └── Documentación-API/
└── 04-Reuniones/
    ├── Standups/
    └── Planning/
```

**Template: Bug Report**

```markdown
---
tipo: bug
severidad: alta
estado: abierto
fecha: 2026-08-09
---

# 🐛 [Título del Bug]

## Descripción
[Breve descripción]

## Pasos para Reproducir
1. 
2. 
3. 

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué está pasando]

## Ambiente
- **OS:** Windows 11
- **Browser:** Chrome 126
- **Versión:** 1.5.2

## Logs/Screenshots


## Posible Causa


## Solución Propuesta


## Enlaces
- [[Documentación relacionada]]
- [Issue GitHub](#)
```

**Comandos útiles:**

```bash
# Documentar bug
hermes create bug-report \
  --title "Login falla con OAuth" \
  --severity high

# Investigación técnica
hermes create research \
  --topic "GraphQL vs REST" \
  --folder "02-Areas/Arquitectura"

# Guardar snippet
hermes save snippet \
  --language python \
  --code "def fibonacci(n): ..." \
  --tags "algoritmos, recursion"
```

---

#### 2. Para Escritores y Creadores

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Proyectos/
│   ├── Libro-Productividad/
│   │   ├── Investigación/
│   │   ├── Outlines/
│   │   ├── Drafts/
│   │   └── Ediciones/
│   ├── Blog-Posts/
│   └── Newsletter/
├── 02-Ideas/
│   ├── Ideas-Articulos/
│   ├── Frases/
│   └── Historias/
├── 03-Recursos/
│   ├── Fuentes/
│   ├── Citas/
│   └── Referencias/
└── 04-Publicado/
    └── 2026/
```

**Template: Artículo**

```markdown
---
tipo: artículo
estado: draft
fecha-inicio: 2026-08-09
palabras-objetivo: 1500
tema: productividad
---

# [Título]

## 🎯 Hook

[Primera frase enganchadora]

## 📝 Outline

1. **Introducción**
   - Problema
   - Por qué importa

2. **Desarrollo**
   - Punto 1
   - Punto 2
   - Punto 3

3. **Conclusión**
   - Recap
   - Call to action

## 🧠 Ideas Principales

- 
- 

## 📚 Fuentes

1. [[Fuente 1]]
2. [[Fuente 2]]

## ✍️ Draft

[Escribir aquí...]

---

## 📊 Métricas

**Palabras:** 
**Legibilidad:** 
**Keywords:** 
```

**Comandos útiles:**

```bash
# Captura rápida de idea
hermes capture "Artículo: IA cambia la escritura"

# Generar outline
hermes outline article \
  --title "10 Técnicas Productividad" \
  --target-words 2000

# Analizar legibilidad
hermes analyze readability --file "draft.md"
```

---

#### 3. Para Estudiantes e Investigadores

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Cursos/
│   ├── Matematicas/
│   ├── Fisica/
│   └── Programacion/
├── 02-Investigación/
│   ├── Tesis/
│   ├── Papers-a-Leer/
│   └── Papers-Leidos/
├── 03-Notas-de-Clase/
│   └── 2026-Semestre-1/
└── 04-Recursos/
    ├── Libros/
    └── Articulos/
```

**Método Cornell Notes:**

```markdown
---
curso: Física Cuántica
clase: 05
fecha: 2026-08-09
profesor: Dr. Smith
---

# Clase 5: Principio de Incertidumbre

## 📝 Notas

- Principio de Heisenberg
- Ecuación: Δx · Δp ≥ ℏ/2
- No se puede medir posición y momentum simultáneamente
- Ejemplos: electrón, fotón

## ❓ Preguntas/Keywords

**¿Qué es Δx?**
Incertidumbre en posición

**¿Por qué existe?**
Naturaleza ondulatoria

**Aplicaciones:**
- Microscopia electrónica
- Computación cuántica

## 📋 Resumen

El principio de incertidumbre establece límite 
teórico a la precisión de medición de propiedades 
complementarias.

## 🔗 Enlaces

- [[Clase 4 - Dualidad]]
- [[Ecuación Schrödinger]]
```

**Comandos útiles:**

```bash
# Nota de paper
hermes create paper-note \
  --title "Quantum Computing 2026" \
  --authors "Smith, J."

# Generar bibliografía
hermes bibliography generate \
  --folder "Tesis" \
  --format APA

# Crear flashcards
hermes create flashcards \
  --from "Notas-de-Clase/Fisica" \
  --count 20
```

---

#### 4. Para Managers y Líderes

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Equipo/
│   ├── 1-on-1s/
│   ├── Performance-Reviews/
│   └── Contrataciones/
├── 02-Proyectos/
│   ├── Q3-2026-OKRs/
│   └── Producto-Nuevo/
├── 03-Estrategia/
│   ├── Roadmap/
│   └── Vision/
└── 04-Reuniones/
    ├── All-Hands/
    └── Board-Meetings/
```

**Template: 1-on-1**

```markdown
---
tipo: 1-on-1
persona: [Nombre]
fecha: 2026-08-09
frecuencia: quincenal
---

# 1-on-1 con [Nombre]

## 🎯 Agenda

1. Cómo va la persona
2. Updates proyectos
3. Blockers
4. Carrera / Desarrollo
5. Feedback bidireccional

## 💬 Notas

### Cómo está

[Estado general, moral, energía]

### Proyectos

**Proyecto A:**
- Status: 
- Blockers: 
- Necesita: 

### Feedback

**De mí:**
- 

**De [Nombre]:**
- 

## ✅ Action Items

- [ ] **[@Yo]** Revisar X - [Fecha]
- [ ] **[@Nombre]** Documentar Y - [Fecha]

## 🔜 Próxima Reunión

**Fecha:** [+2 semanas]
**Pendientes:**
- 

## 🔗 Enlaces

- [[1-on-1 anterior]]
- [[Performance Review]]
```

---

#### 5. Para Emprendedores

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Producto/
│   ├── Vision/
│   ├── Roadmap/
│   ├── User-Research/
│   └── Features/
├── 02-Crecimiento/
│   ├── Marketing/
│   ├── Ventas/
│   └── Métricas/
├── 03-Fundraising/
│   ├── Pitch-Deck/
│   ├── Inversores/
│   └── Term-Sheets/
└── 04-Operaciones/
    ├── Finanzas/
    └── Legal/
```

**Dashboard:**

````markdown
# 📊 Startup Dashboard

```dataview
TABLE estado, prioridad, deadline
FROM "01-Producto/Features"
WHERE estado = "en-desarrollo"
SORT prioridad DESC
```

## 💰 Métricas (Última semana)

- **MRR:** $12,500 (+8%)
- **Usuarios:** 450 (+15)
- **Churn:** 3.2% (-0.5%)
- **CAC:** $85
- **LTV:** $1,200

## 🎯 OKRs Q3

### Alcanzar PMF
- **KR1:** 50 entrevistas ✅ (50/50)
- **KR2:** NPS > 40 🟡 (35/40)
- **KR3:** 60% retention 🔴 (45%)

## 🔥 Esta Semana

1. [ ] Cerrar ronda ($500K)
2. [ ] Lanzar notificaciones
3. [ ] Contratar diseñador

## 📅 Reuniones

- **Lunes 10 AM:** Inversores
- **Miércoles 2 PM:** All hands
- **Viernes 4 PM:** User testing
````

---

#### 6. Para Profesores/Educadores

**Estructura:**

```
Mi-Segundo-Cerebro/
├── 01-Cursos/
│   ├── Matematicas-101/
│   │   ├── Syllabus/
│   │   ├── Clases/
│   │   ├── Tareas/
│   │   └── Examenes/
│   └── Fisica-202/
├── 02-Estudiantes/
│   └── Seguimiento/
├── 03-Recursos/
│   ├── Materiales/
│   └── Referencias/
└── 04-Investigación/
```

**Template: Plan de Clase**

```markdown
---
curso: Matemáticas 101
clase: 12
fecha: 2026-08-15
duracion: 90min
---

# Clase 12: Derivadas

## 🎯 Objetivos

Al final de la clase, estudiantes podrán:
1. Definir concepto de derivada
2. Calcular derivadas básicas
3. Aplicar regla de la cadena

## 📚 Materiales

- Pizarra
- Proyector
- Handout de ejercicios

## ⏱️ Timeline

### Introducción (15 min)
- Review clase anterior
- Motivación: velocidad instantánea

### Teoría (30 min)
- Definición formal
- Ejemplos geométricos
- Notación

### Práctica (30 min)
- Ejercicios guiados
- Trabajo en grupos

### Cierre (15 min)
- Q&A
- Tarea asignada

## 📝 Tarea

**Para próxima clase:**
- Ejercicios 1-10 del libro
- Leer capítulo 4

## 🔗 Enlaces

- [[Clase 11 - Límites]]
- [[Examen Parcial]]
```

---

### 📊 Comparación de Workflows

| Profesión | Plugins Clave | Complejidad | Beneficio |
|-----------|--------------|-------------|-----------|
| Desarrollador | Dataview, Git | Alta | ⭐⭐⭐⭐⭐ |
| Escritor | Templater, Calendar | Media | ⭐⭐⭐⭐⭐ |
| Estudiante | Tasks, Excalidraw | Baja | ⭐⭐⭐⭐⭐ |
| Manager | Kanban, Dataview | Media | ⭐⭐⭐⭐ |
| Emprendedor | Dataview, Tasks | Alta | ⭐⭐⭐⭐⭐ |
| Profesor | Templater, Calendar | Media | ⭐⭐⭐⭐ |

---

*Continúa en: APENDICES-J-K-L.md*
