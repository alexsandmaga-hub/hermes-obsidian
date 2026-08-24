# Apéndices Adicionales - Guía Hermes + Obsidian + Claude

## Apéndice B: Plantillas y Sistemas de Organización

### 📋 Plantillas Predefinidas para Obsidian

Las plantillas te ahorran tiempo y mantienen consistencia en tus notas.

#### Plantilla 1: Nota Diaria

**Ubicación:** `Sistema/Plantillas/Nota-Diaria.md`

```markdown
---
fecha: {{date:YYYY-MM-DD}}
tipo: nota-diaria
dia-semana: {{date:dddd}}
etiquetas: [diario]
---

# {{date:YYYY-MM-DD}} - {{date:dddd}}

## 🎯 Prioridades del Día

1. 
2. 
3. 

## 📝 Notas y Capturas

### Mañana


### Tarde


### Noche


## ✅ Tareas Completadas

- [ ] 
- [ ] 
- [ ] 

## 💡 Ideas y Aprendizajes


## 🔗 Enlaces Relacionados

- [[Proyecto relacionado]]
- [[Nota relacionada]]

## 📊 Estado del Día

**Energía:** ○○○○○ (1-5)
**Productividad:** ○○○○○ (1-5)
**Ánimo:** ○○○○○ (1-5)

## 🔜 Reflexión

**¿Qué salió bien hoy?**


**¿Qué podría mejorar mañana?**

```

#### Plantilla 2: Proyecto Nuevo

**Ubicación:** `Sistema/Plantillas/Proyecto.md`

```markdown
---
tipo: proyecto
fecha-inicio: {{date:YYYY-MM-DD}}
estado: planificación
prioridad: media
etiquetas: [proyecto]
---

# {{title}}

## 🎯 Objetivo Principal

> [Descripción en una frase del objetivo del proyecto]

## 📊 Contexto

**¿Por qué este proyecto?**


**¿Qué problema resuelve?**


## 🛑 Alcance

### Dentro del Alcance
- 
- 
- 

### Fuera del Alcance
- 
- 

## 📅 Cronograma

| Hito | Fecha Estimada | Estado |
|------|----------------|--------|
| Inicio | {{date:YYYY-MM-DD}} | ⏳ |
|  |  |  |
|  |  |  |
| Finalización |  | ⏳ |

## 📝 Tareas Principales

- [ ] Investigación inicial
- [ ] Planificación detallada
- [ ] Implementación
- [ ] Pruebas
- [ ] Documentación
- [ ] Lanzamiento

## 🛠️ Recursos Necesarios

### Herramientas
- 

### Referencias
- 

### Personas/Contactos
- 

## ⚠️ Riesgos y Dependencias

**Riesgos:**
- 

**Dependencias:**
- 

## 📊 Métricas de Éxito

**¿Cómo sabré que este proyecto fue exitoso?**
- 
- 
- 

## 🔗 Enlaces Relacionados

- [[Proyecto relacionado]]
- [[Recurso relevante]]

## 📝 Notas y Actualizaciones

### {{date:YYYY-MM-DD}}
- Proyecto iniciado

```

#### Plantilla 3: Reunión

**Ubicación:** `Sistema/Plantillas/Reunion.md`

```markdown
---
fecha: {{date:YYYY-MM-DD}}
tipo: reunión
proyecto: 
participantes: []
etiquetas: [reunión]
---

# Reunión: {{title}}

**Fecha:** {{date:YYYY-MM-DD}} a las {{time}}
**Duración:** [Tiempo estimado]
**Proyecto:** [[Nombre del proyecto]]

## 👥 Participantes

- 
- 
- 

## 🎯 Agenda

1. 
2. 
3. 

## 📝 Notas

### Tema 1:


### Tema 2:


### Tema 3:


## ✅ Decisiones Tomadas

1. **Decisión:** 
   - **Razón:** 
   - **Responsable:** 

## 📄 Action Items (Tareas)

- [ ] **[@Persona]** Tarea 1 - Fecha límite: 
- [ ] **[@Persona]** Tarea 2 - Fecha límite: 
- [ ] **[@Persona]** Tarea 3 - Fecha límite: 

## 🔄 Próximo Follow-up

**Fecha:** 
**Temas a cubrir:** 

## 🔗 Referencias

- [[Nota relacionada]]
- [Documento externo](https://...)

```

#### Plantilla 4: Nota de Investigación/Aprendizaje

```markdown
---
fecha: {{date:YYYY-MM-DD}}
tipo: investigación
tema: 
fuente: 
etiquetas: [aprendizaje, investigación]
---

# {{title}}

## 📚 Fuente

**Título:** 
**Autor:** 
**URL:** 
**Fecha de acceso:** {{date:YYYY-MM-DD}}

## 🎯 ¿Por qué estoy investigando esto?


## 📝 Notas Clave

### Idea Principal


### Puntos Importantes

1. 
2. 
3. 

### Citas Textuales

> "..."

## 🧠 Mi Análisis

**¿Qué significa esto para mí/mi proyecto?**


**¿Cómo se conecta con lo que ya sé?**


## 🔗 Conexiones

- [[Nota relacionada 1]]
- [[Nota relacionada 2]]
- [[Proyecto donde aplicar esto]]

## ❓ Preguntas Abiertas

- 
- 

## 💡 Próximos Pasos

- [ ] 
- [ ] 

```

---

### 📚 Sistemas de Organización Populares

#### Sistema PARA (Projects, Areas, Resources, Archive)

**El más recomendado para empezar.**

**Estructura:**
```
Mi-Segundo-Cerebro/
├── 01-Proyectos/          (Objetivos con fecha de finalización)
│   ├── HomeLab/
│   ├── Hermes-Obsidian/
│   └── Aprender-Python/
│
├── 02-Areas/              (Responsabilidades continuas)
│   ├── Salud/
│   ├── Finanzas/
│   ├── Carrera/
│   └── Familia/
│
├── 03-Recursos/           (Material de referencia)
│   ├── Tecnología/
│   ├── Libros/
│   ├── Cursos/
│   └── Artículos/
│
└── 04-Archivo/            (Proyectos completados)
    └── 2025/
        ├── Proyecto-Viejo-1/
        └── Proyecto-Viejo-2/
```

**Cuándo usar PARA:**
- ✅ Eres nuevo en Obsidian
- ✅ Quieres algo simple y claro
- ✅ Tienes múltiples proyectos y áreas de responsabilidad
- ✅ Te gusta la organización jerárquica

#### Sistema Zettelkasten (Notas Atómicas)

**Para pensadores y escritores.**

**Principios:**
1. **Una idea por nota** (notas atómicas)
2. **Enlaces entre ideas** (pensamiento conectado)
3. **Tus propias palabras** (no solo copia-pega)
4. **IDs únicos** (YYYYMMDDHHMMSS)

**Estructura:**
```
Mi-Segundo-Cerebro/
├── Inbox/                 (Capturas sin procesar)
├── Notas/                 (Notas atómicas permanentes)
│   ├── 202608021430 - La procrastinación es miedo.md
│   ├── 202608021445 - Sistemas vs Objetivos.md
│   └── 202608021500 - Código como comunicación.md
│
├── Mapas-de-Contenido/    (MOCs - índices temáticos)
│   ├── MOC-Productividad.md
│   ├── MOC-Programación.md
│   └── MOC-Filosofía.md
│
└── Referencias/           (Material externo)
    └── Libros/
    └── Artículos/
```

**Cuándo usar Zettelkasten:**
- ✅ Escribes mucho (libros, artículos, investigación)
- ✅ Te gusta pensar en conexiones entre ideas
- ✅ Quieres desarrollar tu propio pensamiento
- ✅ Tienes paciencia para el proceso

#### Sistema Johnny Decimal

**Para amantes del orden numérico.**

**Estructura:**
```
00-09 Sistema
  00 Inbox
  01 Plantillas
  02 Configuración

10-19 Personal
  10 Salud
  11 Finanzas
  12 Familia

20-29 Proyectos Activos
  20 HomeLab
    20.01 Planificación
    20.02 Hardware
    20.03 Software
  21 Hermes-Obsidian
    21.01 Configuración
    21.02 Documentación

30-39 Trabajo
  30 Proyectos Laborales
  31 Reuniones
  32 Reportes

90-99 Archivo
  90 Proyectos Completados 2025
  91 Proyectos Completados 2024
```

**Cuándo usar Johnny Decimal:**
- ✅ Te gusta el orden numérico
- ✅ Quieres navegación rápida
- ✅ Tienes muchas categorías bien definidas
- ✅ Trabajas con archivos fuera de Obsidian también

---

### 🏷️ Sistema de Etiquetas Recomendado

**Etiquetas por Tipo:**
```
#proyecto
#tarea
#idea
#reunión
#nota-diaria
#investigación
#recurso
```

**Etiquetas por Estado:**
```
#activo
#en-pausa
#completado
#cancelado
#planificación
```

**Etiquetas por Tema:**
```
#tecnología
#salud
#finanzas
#programación
#productividad
```

**Etiquetas por Urgencia:**
```
#urgente
#importante
#algún-día
```

---

## Apéndice C: Plugins Esenciales de Obsidian

### 🔌 Top 10 Plugins Community que Debes Conocer

#### 1. Dataview ⭐⭐⭐ (IMPRESCINDIBLE)

**¿Qué hace?** Consultas tipo base de datos sobre tus notas.

**Instalación:**
1. Settings → Community Plugins → Browse
2. Busca "Dataview"
3. Install → Enable

**Ejemplo de uso:**

````markdown
```dataview
TABLE fecha, estado, prioridad
FROM #proyecto
WHERE estado = "activo"
SORT prioridad DESC
```
````

Muestra tabla de todos los proyectos activos ordenados por prioridad.

**Casos de uso:**
- Listar todas las tareas pendientes
- Ver proyectos por estado
- Generar reportes automáticos
- Dashboard dinámico

**Ejemplos adicionales:**

```dataview
LIST
FROM #tarea
WHERE !completed
SORT fecha ASC
```

```dataview
TABLE file.cdate as "Creado", estado
FROM "01-Proyectos"
WHERE estado = "activo"
```

---

#### 2. Templater ⭐⭐⭐ (IMPRESCINDIBLE)

**¿Qué hace?** Plantillas avanzadas con lógica y scripts.

**Instalación:**
1. Community Plugins → "Templater"
2. Install → Enable
3. Settings → Templater → Template folder: `Sistema/Plantillas`

**Ejemplo:**

```markdown
<%* 
const fecha = tp.date.now("YYYY-MM-DD");
const diaSemana = tp.date.now("dddd");
%>

# Nota del <% fecha %> - <% diaSemana %>

<% tp.file.cursor() %>
```

**Casos de uso:**
- Plantillas dinámicas con fechas
- Automatizar creación de estructura de carpetas
- Insertar contenido dinámico
- Ejecutar scripts personalizados

---

#### 3. Calendar ⭐⭐

**¿Qué hace?** Vista de calendario para notas diarias.

**Instalación:**
1. Community Plugins → "Calendar"
2. Install → Enable

**Uso:**
- Aparece un calendario en el panel derecho
- Haz clic en cualquier día para crear/abrir nota diaria
- Puntos indican días con notas existentes
- Navegación rápida por fechas

---

#### 4. Tasks ⭐⭐

**¿Qué hace?** Gestión avanzada de tareas con fechas y recurrencia.

**Sintaxis:**
```markdown
- [ ] Tarea simple
- [ ] Tarea con fecha 📅 2026-08-15
- [ ] Tarea recurrente 🔁 every week
- [ ] Tarea urgente ❗ high
- [ ] Tarea con fecha de inicio ▶️ 2026-08-10
- [ ] Tarea programada ⏳ 2026-08-20
```

**Consulta de tareas:**
````markdown
```tasks
not done
path includes Proyectos
sort by priority
```
````

**Configuración recomendada:**
- Settings → Tasks
- Date format: `YYYY-MM-DD`
- Global filter: Personaliza según necesites

---

#### 5. Kanban ⭐⭐

**¿Qué hace?** Tableros estilo Trello dentro de Obsidian.

**Crear tablero:**
1. Crea nota nueva
2. Command Palette (Ctrl+P)
3. "Kanban: Create new board"

**Columnas típicas:**
```
Por Hacer | En Progreso | Bloqueado | Completado
```

**Características:**
- Drag & drop de tarjetas
- Cada tarjeta puede ser una nota
- Colores y etiquetas
- Archivado automático

**Ejemplo de uso:**
- Gestión de proyectos
- Sprint planning
- Flujo de trabajo personal
- Seguimiento de bugs

---

#### 6. Excalidraw ⭐⭐

**¿Qué hace?** Diagramas y dibujos a mano dentro de Obsidian.

**Uso:**
- Diagramas de flujo
- Mapas mentales
- Mockups de UI
- Anotaciones visuales
- Arquitectura de sistemas

**Características:**
- Dibujo a mano alzada
- Formas predefinidas
- Conectores entre elementos
- Exportar a PNG/SVG
- Incrustar en notas

---

#### 7. Advanced Tables ⭐

**¿Qué hace?** Edición fácil de tablas Markdown.

**Características:**
- Tab para navegar entre celdas
- Auto-formato de tablas
- Agregar/eliminar filas y columnas fácilmente
- Atajos de teclado
- Ordenamiento de columnas

**Atajos útiles:**
- `Tab`: Siguiente celda
- `Shift+Tab`: Celda anterior
- `Enter`: Nueva fila
- `Ctrl+Shift+D`: Eliminar fila

---

#### 8. Homepage ⭐

**¿Qué hace?** Define una nota como página de inicio.

**Configuración:**
1. Instala plugin
2. Settings → Homepage
3. Elige tu nota (ej: `Dashboard.md`)
4. Ahora esa nota se abre al iniciar Obsidian

**Ideas para tu homepage:**
- Dashboard con Dataview queries
- Resumen de proyectos activos
- Tareas del día
- Enlaces rápidos
- Citas motivacionales

---

#### 9. QuickAdd ⭐

**¿Qué hace?** Capturas rápidas y macros.

**Ejemplo:**
- Hotkey para captura rápida de ideas
- Automatizar workflows complejos
- Crear notas con plantillas desde cualquier lugar
- Ejecutar comandos en secuencia

**Configuración típica:**
1. Settings → QuickAdd
2. Add Choice → Capture
3. File Name: `{{DATE:YYYY-MM-DD}}-captura`
4. Folder: `00-Inbox/`
5. Asignar hotkey (ej: `Ctrl+Shift+N`)

---

#### 10. Obsidian Git ⭐

**¿Qué hace?** Sincroniza tu bóveda con GitHub automáticamente.

**Configuración:**
1. Instala plugin
2. Inicializa Git en tu bóveda:
   ```bash
   cd "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro"
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/tu-usuario/tu-repo.git
   git push -u origin main
   ```
3. Settings → Obsidian Git
4. Auto-commit: Cada 30 minutos (configurable)
5. Auto-push: Después de cada commit
6. Auto-pull: Al iniciar Obsidian

**Ventajas:**
- ✅ Control de versiones completo
- ✅ Backup en la nube (GitHub)
- ✅ Historial de cambios
- ✅ Revertir cambios fácilmente
- ✅ Colaboración con otros

---

### 🎨 Plugins Adicionales Útiles

#### 11. File Tree Alternative

Mejora la vista del explorador de archivos con estructura de árbol más clara.

#### 12. Note Refactor

Extrae secciones de notas largas en notas separadas manteniendo enlaces.

#### 13. Tag Wrangler

Gestión avanzada de etiquetas: renombrar, fusionar, búsqueda.

#### 14. Periodic Notes

Notas diarias, semanales, mensuales, anuales con plantillas.

#### 15. Outliner

Mejora la edición de listas con comportamiento tipo Workflowy/Dynalist.

---

## Apéndice D: Seguridad y Privacidad

### 🔒 Protección de tu Sistema

#### 1. Seguridad de la Cuenta de Anthropic (Claude)

**Habilitar 2FA (Autenticación de Dos Factores):**

1. Inicia sesión en https://console.anthropic.com
2. Haz clic en tu perfil (esquina superior derecha)
3. "Account Settings"
4. "Security" → "Enable Two-Factor Authentication"
5. Escanea QR con Google Authenticator o Authy
6. **IMPORTANTE:** Guarda códigos de recuperación en lugar seguro

**Códigos de recuperación:**
- Anótalos en papel
- Guárdalos en password manager
- NO los guardes en Obsidian sin encriptar
- Cada código se usa una sola vez

**Rotar API Keys regularmente:**

Cada 3-6 meses:
1. Console → API Keys
2. "Create Key" (nueva)
3. Actualiza en `.env` de Hermes (Windows y Mac)
4. Prueba que todo funciona
5. "Delete" la key antigua

**Monitoreo de acceso:**
- Revisa "Activity Log" mensualmente
- Busca accesos sospechosos
- Revoca sesiones desconocidas

---

#### 2. Seguridad del NAS Synology

**Habilitar 2FA en DSM:**

1. DSM → Control Panel → User & Group
2. Tu usuario → Edit
3. Pestaña "Security"
4. "Enable 2-step verification"
5. Escanea QR con app autenticadora
6. Guarda códigos de emergencia

**Configurar Firewall:**

1. Control Panel → Security → Firewall
2. Enable firewall
3. Crear reglas:

**Regla 1 - Permitir red local:**
```
Ports: All
Source IP: 192.168.1.0/24
Action: Allow
```

**Regla 2 - Denegar todo lo demás:**
```
Ports: All
Source IP: All
Action: Deny
```

**Regla 3 - QuickConnect (si usas):**
```
Ports: 5000, 5001, 6690
Source IP: All
Action: Allow
```

**Auto-Block (protección contra fuerza bruta):**

1. Control Panel → Security → Account
2. "Enable auto block"
3. Parámetros recomendados:
   - Login attempts: `5`
   - Within (minutes): `5`
   - Block for (minutes): `30`
   - ✅ "Enable DoS protection"

**Habilitar HTTPS:**

1. Control Panel → Security → Certificate
2. "Add" → "Get a certificate from Let's Encrypt"
3. Ingresa tu dominio (QuickConnect o propio)
4. Email para renovaciones
5. Acepta términos
6. Auto-renovación habilitada

**Configuración adicional:**
- Control Panel → Security → Security
- ✅ "Enhance browser compatibility by skipping IP checking"
- ✅ "Enable HTTP compression"
- ⚠️ Deshabilita HTTP si solo usas HTTPS

---

#### 3. Encriptación de Datos

**Opción 1: Encriptar Carpeta Compartida**

⚠️ **Solo para datos MUY sensibles** (impacto en rendimiento)

1. DSM → Control Panel → Shared Folder
2. Selecciona `Obsidian-Vault` → Edit
3. Pestaña "Encryption"
4. "Encrypt this shared folder"
5. Ingresa contraseña FUERTE (16+ caracteres)
6. **CRÍTICO:** Guarda esta contraseña en lugar seguro
7. Si la pierdes, pierdes TODOS los datos

**Consideraciones:**
- ✅ Máxima seguridad
- ❌ 10-15% más lento
- ❌ Debes "montar" carpeta después de cada reinicio
- ❌ No compatible con algunos features (dedup, compression)

**Opción 2: Encriptación a Nivel de Disco (Recomendado)**

1. Solo disponible al crear el volumen
2. Storage Manager → Volume → Create
3. Durante creación, marca "Encrypt this volume"
4. Contraseña maestra
5. Todo el disco se encripta transparentemente

**Ventajas:**
- ✅ Rendimiento casi nativo
- ✅ Totalmente transparente
- ✅ Protege todo el volumen
- ❌ Solo al crear volumen nuevo

**Opción 3: Archivos Individuales con GPG**

Para archivos ultra-sensibles dentro de tu bóveda:

```bash
# Encriptar archivo
gpg -c archivo-sensible.md
# Crea: archivo-sensible.md.gpg

# Desencriptar
gpg archivo-sensible.md.gpg
# Pide contraseña y restaura archivo
```

---

#### 4. Protección de API Keys

**En Windows:**

```powershell
# Hacer archivo .env de solo lectura
Set-ItemProperty -Path "C:\Users\mgabi\.hermes\.env" -Name IsReadOnly -Value $true

# Ocultar el archivo
Set-ItemProperty -Path "C:\Users\mgabi\.hermes\.env" -Name Attributes -Value Hidden

# Verificar
Get-ItemProperty "C:\Users\mgabi\.hermes\.env" | Select-Object Name,IsReadOnly,Attributes
```

**En Mac/Linux:**

```bash
# Permisos de solo lectura para propietario
chmod 400 ~/.hermes/.env

# Verificar
ls -la ~/.hermes/.env
# Debería mostrar: -r--------
```

**Auditar acceso:**

```powershell
# Windows - Ver quién accedió al archivo
Get-FileAccessAudit "C:\Users\mgabi\.hermes\.env"
```

---

#### 5. Backup Seguro de Credenciales

**Qué guardar:**
- ✅ API Key de Anthropic
- ✅ Contraseña del NAS
- ✅ Contraseña de encriptación (si usas)
- ✅ Códigos de recuperación 2FA
- ✅ Credenciales de QuickConnect
- ✅ Contraseñas de Git/GitHub
- ✅ Claves SSH (si usas)

**Dónde guardar (en orden de seguridad):**

**1. Password Manager (Más recomendado)**
- **1Password** (de pago, excelente)
- **Bitwarden** (freemium, open source)
- **LastPass** (freemium)
- **KeePassXC** (gratis, local, open source)

**2. Archivo encriptado offline**

Usando VeraCrypt:
```
1. Crear container encriptado (VeraCrypt)
2. Tamaño: 10MB es suficiente
3. Encryption: AES
4. Hash: SHA-512
5. Guardar archivo .txt con credenciales dentro
6. Montar solo cuando necesites
7. Desmonta después de usar
8. Guarda container en USB seguro
```

**3. ❌ NUNCA:**
- Archivo de texto plano
- Email o mensajes
- Notas en Obsidian sin encriptar
- Screenshots
- Notas físicas sin protección
- Código fuente en Git público
- Variables de entorno sin protección
- Hojas de cálculo sin encriptar

---

#### 6. Mejores Prácticas de Seguridad

**Para API Keys:**
- ✅ Rotación cada 3-6 meses
- ✅ Una key por dispositivo/propósito
- ✅ Nombres descriptivos
- ✅ Monitoreo de uso
- ✅ Revocación inmediata si compromiso

**Para contraseñas:**
- ✅ Mínimo 16 caracteres
- ✅ Mayúsculas, minúsculas, números, símbolos
- ✅ Única para cada servicio
- ✅ Generadas aleatoriamente
- ✅ Almacenadas en password manager

**Para 2FA:**
- ✅ Usa app autenticadora (no SMS)
- ✅ Backup de códigos de recuperación
- ✅ Habilita en TODOS los servicios que lo soporten

**Para el NAS:**
- ✅ Actualiza DSM regularmente
- ✅ Monitorea logs de acceso
- ✅ Deshabilita servicios no usados
- ✅ Cambia puerto SSH del default (22)
- ✅ Deshabilita root login
- ✅ Usa nombres de usuario no obvios

---

## Apéndice E: Monitoreo de Costos y Optimización

### 💰 Controlar Gastos de la API de Claude

#### 1. Dashboard de Uso de Anthropic

**Acceder:**
1. https://console.anthropic.com/usage
2. Ver uso en tiempo real

**Métricas importantes:**
- **Tokens de entrada (Input):** Lo que envías a Claude
- **Tokens de salida (Output):** Lo que Claude responde
- **Costo por modelo:** Diferentes modelos cuestan diferente
- **Requests:** Número de llamadas API

**Precios aproximados (Agosto 2026 - pueden cambiar):**

| Modelo | Input (por 1M tokens) | Output (por 1M tokens) |
|--------|----------------------|------------------------|
| Claude 3.5 Haiku | $0.80 | $4.00 |
| Claude 3.5 Sonnet | $3.00 | $15.00 |
| Claude 4 Sonnet | $3.00 | $15.00 |
| Claude 4 Opus | $15.00 | $75.00 |

**Prompt Caching (reduce costos 90%):**
- Cached input: $0.30 por 1M tokens (Sonnet)
- Cache write: $3.75 por 1M tokens (Sonnet)
- Si reutilizas contexto, ahorras MUCHO

---

#### 2. Establecer Límites de Gasto

**En Anthropic Console:**

1. Settings → Billing
2. "Set usage limit"
3. Configurar:
   - **Soft limit:** $20/mes (recibes alerta)
   - **Hard limit:** $50/mes (se bloquea automáticamente)

**Alertas por email:**
1. Settings → Notifications
2. Habilita "Usage alerts"
3. Umbrales:
   - 50% del límite ($10)
   - 75% del límite ($15)
   - 90% del límite ($18)
   - 100% del límite ($20)

**Monitoreo diario:**
- Revisa dashboard cada semana
- Gráfico de tendencia
- Compara mes a mes

---

#### 3. Optimizar Uso para Reducir Costos

**Técnica 1: Usa el modelo apropiado**

No uses siempre el modelo más caro. Ajusta según la tarea:

```env
# .env para tareas simples
MODEL_NAME=claude-haiku-4-5  # Más barato, rápido

# Para tareas complejas
MODEL_NAME=claude-sonnet-4-8  # Balance precio/calidad

# Para tareas muy complejas
MODEL_NAME=claude-opus-4-8  # Más caro, mejor calidad
```

**Cuándo usar cada modelo:**

| Tarea | Modelo Recomendado | Por qué |
|-------|-------------------|---------|
| Leer notas simples | Haiku | Suficiente para lectura |
| Organizar inbox | Haiku | Tarea mecánica |
| Crear nota nueva | Sonnet | Necesita coherencia |
| Análisis complejo | Sonnet | Balance ideal |
| Escribir código complejo | Opus | Razonamiento profundo |
| Decisiones críticas | Opus | Máxima capacidad |

**Técnica 2: Prompts concisos**

❌ **MAL** (usa ~150 tokens innecesarios):
```
Hola Hermes, espero que estés teniendo un excelente día. 
Me preguntaba si podrías, por favor, si no es mucha molestia, 
ayudarme a crear una nota para mi proyecto de HomeLab. 
La nota debería incluir, si es posible, los siguientes elementos: 
una descripción breve del proyecto, los objetivos principales que 
quiero lograr, el estado actual en el que se encuentra, y los 
próximos pasos que planeo tomar. Además, me gustaría que la 
guardaras en la ubicación correcta dentro de mi bóveda, 
específicamente en la carpeta de Proyectos, en la subcarpeta 
de HomeLab. Muchas gracias de antemano por tu ayuda.
```

✅ **BIEN** (usa ~30 tokens):
```
Crea nota proyecto HomeLab con: descripción, objetivos, 
estado, próximos pasos. Guarda en 01-Proyectos/HomeLab/.
```

**Ahorro: 80% menos tokens = 80% menos costo**

**Técnica 3: Evita contexto innecesario**

❌ **MAL:**
```
Hermes, lee mi archivo CLAUDE.md completo, luego lee todas 
mis notas del proyecto HomeLab, después revisa mis notas 
diarias de la última semana, analiza mis tareas pendientes, 
revisa mis reuniones del mes, y finalmente dime qué hice ayer.
```

✅ **BIEN:**
```
Lee mi nota diaria de ayer y resume qué hice.
```

**Técnica 4: Usa caché de Hermes**

En `~/.hermes/config.yaml`:

```yaml
memory:
  cache_enabled: true
  cache_size_mb: 2048
  cache_ttl_seconds: 7200  # 2 horas
  
  # Evita re-leer archivos sin cambios
  check_file_modified: true
  
api:
  # Habilita prompt caching de Claude
  use_prompt_caching: true
  cache_ttl_minutes: 120
```

**Técnica 5: Batch operations**

En lugar de 10 llamadas separadas, agrupa:

❌ **MAL (10 llamadas = 10x costo):**
```
Hermes, lee nota 1
Hermes, lee nota 2
Hermes, lee nota 3
...
Hermes, lee nota 10
```

✅ **BIEN (1 llamada):**
```
Hermes, lee estas 10 notas y resume cada una:
1. Nota1.md
2. Nota2.md
...
10. Nota10.md
```

---

#### 4. Monitorear con Comandos de Hermes

```bash
# Ver uso total acumulado
hermes usage

# Ver uso del último mes
hermes usage --period month

# Ver uso de hoy
hermes usage --period today

# Ver uso por modelo
hermes usage --by-model

# Ver gasto en dinero
hermes usage --cost

# Exportar reporte detallado
hermes usage --export uso-agosto-2026.json

# Ver top prompts más costosos
hermes usage --top-prompts 10
```

**Interpretar el output:**
```
Usage Report - August 2026
==========================
Total Requests: 1,247
Total Input Tokens: 2,458,392
Total Output Tokens: 892,441
Total Cost: $12.34

By Model:
- claude-sonnet-4-8: $10.20 (83%)
- claude-haiku-4-5: $2.14 (17%)

Top Prompts by Cost:
1. "Generate weekly report" - $1.45 (12%)
2. "Analyze project status" - $0.98 (8%)
...
```

---

#### 5. Calculadora de Costos Estimados

**Uso típico personal:**

| Actividad | Veces/día | Tokens aprox | Costo/mes (Sonnet) |
|-----------|-----------|--------------|---------------------|
| Crear nota diaria | 1 | 500 | $0.05 |
| Organizar inbox (Haiku) | 1 | 1,000 | $0.01 |
| Consultas a Hermes | 10 | 5,000 | $0.50 |
| Generar reportes | 1 | 2,000 | $0.20 |
| Procesar documentos | 3 | 10,000 | $1.00 |
| Análisis semanal | 1/semana | 5,000 | $0.20 |
| **TOTAL MENSUAL** | - | ~500K | **~$5-8** |

**Uso intensivo (desarrollador):**

| Actividad | Veces/día | Tokens aprox | Costo/mes (Sonnet) |
|-----------|-----------|--------------|---------------------|
| Todas las anteriores | - | 500K | $8.00 |
| Generación de código | 5 | 20,000 | $3.00 |
| Code reviews | 3 | 15,000 | $2.25 |
| Documentación auto | 2 | 10,000 | $1.50 |
| Debug assistance | 5 | 25,000 | $3.75 |
| **TOTAL MENSUAL** | - | ~2M | **~$25-35** |

**Uso muy intensivo (escritor/investigador):**

| Actividad | Veces/día | Tokens aprox | Costo/mes (Opus) |
|-----------|-----------|--------------|-------------------|
| Drafts largos | 2 | 30,000 | $45.00 |
| Research | 5 | 25,000 | $37.50 |
| Editing | 3 | 20,000 | $30.00 |
| Brainstorming | 5 | 15,000 | $22.50 |
| **TOTAL MENSUAL** | - | ~3M | **~$60-90** |

---

#### 6. Alertas Personalizadas

**Script para monitoreo (Windows PowerShell):**

```powershell
# Script: monitor-claude-costs.ps1
# Ejecutar diariamente con Task Scheduler

$apiKey = $env:ANTHROPIC_API_KEY
$currentUsage = hermes usage --cost --json | ConvertFrom-Json
$monthlyLimit = 20  # Tu límite en USD

if ($currentUsage.total_cost -gt ($monthlyLimit * 0.8)) {
    # Enviar email de alerta
    Send-MailMessage `
        -To "tu-email@gmail.com" `
        -From "alertas@tudominio.com" `
        -Subject "⚠️ Alerta: Uso de Claude al 80%" `
        -Body "Has usado $($currentUsage.total_cost) de $monthlyLimit USD este mes." `
        -SmtpServer "smtp.gmail.com" `
        -Port 587 `
        -UseSsl `
        -Credential (Get-Credential)
}
```

**Programar con Task Scheduler:**
1. Task Scheduler → Create Task
2. Trigger: Daily at 8:00 PM
3. Action: Run PowerShell script
4. Script: `C:\Scripts\monitor-claude-costs.ps1`

---

#### 7. Tips de Optimización Avanzada

**1. Reutiliza prompts con caching:**

```python
# En lugar de enviar CLAUDE.md cada vez:
# Primera vez: Se cachea (costo normal)
# Siguientes 5 minutos: Caché (90% descuento)

hermes config set ENABLE_PROMPT_CACHING=true
```

**2. Comprime notas largas antes de enviar:**

```
Hermes, resume esta nota larga antes de analizarla:
[nota-muy-larga.md]

Luego analiza el resumen.
```

**3. Usa modelos híbridos:**

```yaml
# config.yaml
models:
  default: claude-sonnet-4-8
  
  # Tareas específicas con modelos específicos
  tasks:
    read: claude-haiku-4-5
    write: claude-sonnet-4-8
    analyze: claude-opus-4-8
```

**4. Limita longitud de respuestas:**

```
Hermes, responde en máximo 100 palabras: [pregunta]
```

Reduce tokens de output significativamente.

---

### 💡 Resumen de Ahorro

| Estrategia | Ahorro Potencial |
|-----------|------------------|
| Usar modelo apropiado | 40-60% |
| Prompts concisos | 30-50% |
| Habilitar caching | 70-90% (en reutilización) |
| Batch operations | 20-40% |
| Limitar contexto | 25-45% |
| Compresión previa | 30-50% |

**Aplicando todas:** Potencial de reducir costos **60-80%** manteniendo la misma funcionalidad.

---

*Continúa en: APENDICES-F-G-H-I.md*
