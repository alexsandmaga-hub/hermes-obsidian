# Guía Completa: Conectar Obsidian con Hermes usando Claude como Motor de IA

## 📋 Tabla de Contenidos

1. [¿Qué es todo esto?](#qué-es-todo-esto)
2. [¿Por qué usar esta combinación?](#por-qué-usar-esta-combinación)
3. [Requisitos previos](#requisitos-previos)
4. [Paso 1: Instalar Obsidian](#paso-1-instalar-obsidian)
5. [Paso 2: Crear tu Bóveda (Vault) en Obsidian](#paso-2-crear-tu-bóveda-vault-en-obsidian)
6. [Paso 3: Instalar Python](#paso-3-instalar-python)
7. [Paso 4: Instalar Hermes Agent](#paso-4-instalar-hermes-agent)
8. [Paso 5: Configurar Claude API](#paso-5-configurar-claude-api)
9. [Paso 6: Conectar Hermes con Obsidian](#paso-6-conectar-hermes-con-obsidian)
10. [Paso 7: Configurar el archivo CLAUDE.md](#paso-7-configurar-el-archivo-claudemd)
11. [Paso 8: Probar la integración](#paso-8-probar-la-integración)
12. [Ejemplos Prácticos: Organizando tus Proyectos](#ejemplos-prácticos-organizando-tus-proyectos)
13. [Solución de Problemas](#solución-de-problemas)
14. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)

---

## ¿Qué es todo esto?

Imagina tener un asistente de IA que:
- **Nunca olvida** nada de lo que has hablado
- **Conoce todos tus proyectos** sin que se lo recuerdes
- **Lee y escribe** en tus notas automáticamente
- **Se vuelve más inteligente** con cada conversación

Eso es exactamente lo que logras conectando estas tres herramientas:

### 🧠 Obsidian (Tu Segundo Cerebro)
- **¿Qué es?** Una aplicación de notas que guarda todo en archivos Markdown simples en tu computadora
- **¿Para qué sirve?** Almacena tus proyectos, ideas, conocimientos y conversaciones
- **Ventaja clave:** Todo se guarda localmente, tú tienes control total

### 🤖 Hermes Agent (El Organizador Autónomo)
- **¿Qué es?** Un "agente" de IA que puede trabajar de forma autónoma
- **¿Para qué sirve?** Lee tus notas, ejecuta tareas, organiza información y crea nuevas notas
- **Ventaja clave:** Funciona 24/7, puede programar tareas automáticas

### 🧪 Claude (El Cerebro de IA)
- **¿Qué es?** El modelo de inteligencia artificial de Anthropic (similar a ChatGPT pero de otra compañía)
- **¿Para qué sirve?** Proporciona el razonamiento avanzado y la capacidad de entender contexto
- **Ventaja clave:** Excelente para tareas complejas, programación y razonamiento profundo

---

## ¿Por qué usar esta combinación?

### ✅ Beneficios principales:

1. **Memoria Persistente Infinita**
   - Hermes lee y escribe en tu bóveda de Obsidian
   - Nunca pierdes el contexto de tus proyectos
   - Todo queda documentado automáticamente

2. **Cero Repetición de Contexto**
   - El agente ya conoce tus proyectos desde el inicio
   - No tienes que explicar lo mismo una y otra vez
   - Ahorra tiempo y frustración

3. **Organización Autónoma**
   - Hermes puede ordenar notas desordenadas
   - Crea resúmenes y bitácoras automáticamente
   - Etiqueta y conecta ideas relacionadas

4. **Razonamiento Avanzado + Contexto Personal**
   - Claude proporciona análisis de alto nivel
   - Trabaja con TU información específica
   - Respuestas personalizadas a tu situación real

### 📊 Comparación: Con vs Sin este Sistema

| Situación | Sin el Sistema | Con el Sistema |
|-----------|---------------|----------------|
| Iniciar un proyecto | "Cuéntame sobre tu proyecto..." cada vez | "Continúa con el proyecto HomeLab" - ya sabe todo |
| Buscar información | Revisar múltiples notas manualmente | "¿Qué decidimos sobre X?" - respuesta instantánea |
| Documentar decisiones | Escribir notas manualmente después | Se documenta automáticamente mientras trabajas |
| Recordar conversaciones antiguas | Olvidadas para siempre | Almacenadas y accesibles permanentemente |

---

## Requisitos previos

Antes de empezar, necesitas:

### Hardware
- ✅ Computadora con Windows, Mac o Linux
- ✅ Al menos 4GB de RAM (8GB recomendado)
- ✅ 2GB de espacio libre en disco

### Software
- ✅ Conexión a Internet (para instalar y para usar la API de Claude)
- ✅ Cuenta de correo electrónico (para crear cuenta de Anthropic)
- ✅ Tarjeta de crédito/débito (para la API de Claude - cobran por uso, pero es barato)

### Conocimientos
- ✅ Saber instalar programas en tu computadora
- ✅ No necesitas saber programar
- ✅ No necesitas experiencia previa con IA

### Tiempo estimado
- ⏱️ Primera instalación: 30-45 minutos
- ⏱️ Configuración inicial: 15-20 minutos
- ⏱️ **Total: aproximadamente 1 hora**

---

## Paso 1: Instalar Obsidian

### 1.1 Descargar Obsidian

1. Ve a la página oficial: **https://obsidian.md**
2. Haz clic en "**Download**" (Descargar)
3. Selecciona tu sistema operativo:
   - **Windows**: Descarga el instalador `.exe`
   - **Mac**: Descarga el archivo `.dmg`
   - **Linux**: Descarga el `.AppImage` o usa Snap

### 1.2 Instalar Obsidian

**En Windows:**
```
1. Abre el archivo descargado (Obsidian-X.X.X.exe)
2. Sigue el asistente de instalación
3. Acepta los términos y condiciones
4. Elige la ubicación de instalación (o deja la predeterminada)
5. Haz clic en "Instalar"
6. Espera a que termine la instalación
7. Marca "Ejecutar Obsidian" y haz clic en "Finalizar"
```

**En Mac:**
```
1. Abre el archivo .dmg descargado
2. Arrastra el ícono de Obsidian a la carpeta Applications
3. Abre Launchpad y busca Obsidian
4. Haz clic para abrir (puede que te pida confirmación de seguridad)
```

### 1.3 Primera ejecución

La primera vez que abras Obsidian verás una pantalla de bienvenida. **NO CIERRES OBSIDIAN AÚN**, lo necesitaremos para el siguiente paso.

---

## Paso 2: Crear tu Bóveda (Vault) en Obsidian

Una "bóveda" (vault) es simplemente una carpeta donde Obsidian guardará todas tus notas.

### 2.1 Crear la bóveda

1. En la pantalla de bienvenida de Obsidian, haz clic en "**Create new vault**" (Crear nueva bóveda)

2. Configura tu bóveda:
   - **Vault name** (Nombre): `Mi-Segundo-Cerebro` (o el nombre que prefieras)
   - **Location** (Ubicación): Elige dónde quieres guardar tus notas
     - **Recomendado para Windows**: `C:\Users\TU_USUARIO\Documents\Obsidian\`
     - **Recomendado para Mac**: `/Users/TU_USUARIO/Documents/Obsidian/`

3. Haz clic en "**Create**" (Crear)

### 2.2 Estructura inicial de carpetas

Obsidian abrirá tu nueva bóveda vacía. Vamos a crear una estructura básica:

1. En el panel izquierdo, haz clic derecho en el espacio vacío
2. Selecciona "**New folder**" (Nueva carpeta)
3. Crea estas carpetas una por una:

```
Mi-Segundo-Cerebro/
├── 00-Inbox/              (Ideas y capturas rápidas sin procesar)
├── 01-Proyectos/          (Tus proyectos activos)
├── 02-Areas/              (Áreas de responsabilidad continua)
├── 03-Recursos/           (Material de referencia)
├── 04-Archivo/            (Proyectos completados)
└── Sistema/               (Configuración para Hermes y Claude)
```

### 2.3 Apuntar la ubicación de tu bóveda

**MUY IMPORTANTE:** Necesitas saber la ruta exacta de tu bóveda. Anótala aquí:

**Mi ruta de bóveda:**
```
_________________________________
(Ejemplo: C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro)
```

---

## Paso 3: Instalar Python

Hermes Agent necesita Python para funcionar. No te preocupes, es fácil.

### 3.1 Verificar si ya tienes Python

Abre PowerShell (Windows) o Terminal (Mac/Linux) y escribe:

```powershell
python --version
```

**Si ves algo como:** `Python 3.10.x` o `Python 3.11.x` o superior, **¡ya tienes Python! Salta al Paso 4.**

**Si ves un error** o una versión menor a 3.10, continúa con la instalación.

### 3.2 Descargar Python

1. Ve a: **https://www.python.org/downloads/**
2. Haz clic en el botón amarillo "**Download Python 3.12.x**" (o la versión más reciente)

### 3.3 Instalar Python en Windows

1. Abre el instalador descargado
2. **¡MUY IMPORTANTE!** Marca la casilla "**Add Python to PATH**" (Agregar Python al PATH)
3. Haz clic en "**Install Now**"
4. Espera a que termine la instalación
5. Haz clic en "**Close**"

### 3.4 Instalar Python en Mac

1. Abre el archivo `.pkg` descargado
2. Sigue el asistente de instalación
3. Acepta los términos
4. Instala en la ubicación predeterminada
5. Espera a que termine

### 3.5 Verificar la instalación

Cierra y vuelve a abrir PowerShell/Terminal, luego escribe:

```powershell
python --version
```

Deberías ver algo como: `Python 3.12.x`

---

## Paso 4: Instalar Hermes Agent

### 4.1 Instalar Hermes Agent con pip

Hermes Agent se instala usando `pip`, el gestor de paquetes de Python.

**En PowerShell (Windows):**

```powershell
pip install hermes-agent
```

**En Terminal (Mac/Linux):**

```bash
pip install hermes-agent
```

**Espera a que termine la instalación.** Verás muchas líneas de texto descargando dependencias. Esto puede tomar 2-5 minutos.

### 4.2 Ejecutar la configuración inicial de Hermes

Una vez instalado, ejecuta el comando de configuración:

```powershell
hermes setup
```

Este comando te hará varias preguntas. Aquí te digo qué responder:

**Pregunta 1:** `Enter your name (or press Enter to skip):`
- **Responde:** Tu nombre (ejemplo: `Gabriel`)

**Pregunta 2:** `Select your preferred AI provider:`
- **Responde:** Escribe el número correspondiente a `anthropic` (Claude)

**Pregunta 3:** `Do you want to enable the API server? (yes/no):`
- **Responde:** `yes`

**Pregunta 4:** `API server port (default: 8642):`
- **Responde:** Presiona Enter (usa el predeterminado)

### 4.3 Verificar la instalación de Hermes

Verifica que Hermes se instaló correctamente:

```powershell
hermes --version
```

Deberías ver algo como: `Hermes Agent v0.16.0` (o la versión actual)

---

## Paso 5: Configurar Claude API

Para que Hermes use Claude como cerebro, necesitas una clave API de Anthropic.

### 5.1 Crear cuenta en Anthropic

1. Ve a: **https://console.anthropic.com**
2. Haz clic en "**Sign Up**" (Registrarse)
3. Ingresa tu correo electrónico y crea una contraseña
4. Verifica tu correo (revisa tu bandeja de entrada)
5. Completa tu perfil

### 5.2 Agregar método de pago

**¿Por qué necesito esto?** Anthropic cobra por uso de la API, pero es muy económico:
- Claude 3.5 Sonnet: ~$3 USD por millón de tokens de entrada
- Para uso personal típico: **$5-15 USD al mes**
- Te dan **$5 USD de crédito gratis** para empezar

**Pasos:**
1. En la consola de Anthropic, ve a "**Billing**" (Facturación)
2. Haz clic en "**Add payment method**"
3. Ingresa los datos de tu tarjeta
4. Guarda

### 5.3 Obtener tu API Key (Clave API)

1. En la consola de Anthropic, ve a "**API Keys**" en el menú lateral
2. Haz clic en "**Create Key**" (Crear clave)
3. Dale un nombre: `Hermes-Obsidian`
4. Haz clic en "**Create Key**"
5. **¡MUY IMPORTANTE!** Copia la clave que aparece - solo la verás UNA vez

**Tu API Key se ve así:**
```
sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**GUÁRDALA AQUÍ (temporalmente):**
```
_____________________________________________________________________
```

### 5.4 Configurar la API Key en Hermes

Ahora necesitas decirle a Hermes tu clave API.

**En Windows (PowerShell):**

```powershell
$env:ANTHROPIC_API_KEY="tu-clave-api-aqui"
setx ANTHROPIC_API_KEY "tu-clave-api-aqui"
```

**En Mac/Linux (Terminal):**

```bash
export ANTHROPIC_API_KEY="tu-clave-api-aqui"
echo 'export ANTHROPIC_API_KEY="tu-clave-api-aqui"' >> ~/.bashrc
```

**Reemplaza** `tu-clave-api-aqui` con tu clave real (la que copiaste).

### 5.5 Verificar la configuración

Cierra y vuelve a abrir PowerShell/Terminal, luego verifica:

```powershell
echo $env:ANTHROPIC_API_KEY
```

Deberías ver tu clave API impresa en pantalla.

---

## Paso 6: Conectar Hermes con Obsidian

> **💡 Nota importante:** Si quieres usar un NAS (como Synology DS723+) para almacenar tu bóveda y tener acceso desde cualquier dispositivo, **salta al [Apéndice A: Configuración Avanzada con NAS Synology](#apéndice-a-configuración-avanzada-con-nas-synology)** ANTES de continuar con este paso. Configura el NAS primero y luego vuelve aquí.

Ahora viene la parte mágica: conectar Hermes con tu bóveda de Obsidian.

### 6.1 Configurar la memoria de Hermes

Hermes tiene un comando especial para conectarse con Obsidian:

```powershell
hermes memory setup --provider obsidian --path "RUTA_DE_TU_BOVEDA"
```

**Reemplaza** `RUTA_DE_TU_BOVEDA` con la ruta que anotaste en el Paso 2.3

**Ejemplo para Windows:**
```powershell
hermes memory setup --provider obsidian --path "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro"
```

**Ejemplo para Mac:**
```bash
hermes memory setup --provider obsidian --path "/Users/mgabi/Documents/Obsidian/Mi-Segundo-Cerebro"
```

### 6.2 Verificar la conexión

Ejecuta:

```powershell
hermes memory status
```

Deberías ver algo como:
```
Memory Provider: obsidian
Memory Path: C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro
Status: Connected ✓
```

### 6.3 Configurar el archivo de variables de entorno

Hermes guarda su configuración en un archivo `.env`. Vamos a asegurarnos de que esté bien configurado.

**Ubicación del archivo:**
- **Windows:** `C:\Users\TU_USUARIO\.hermes\.env`
- **Mac/Linux:** `~/.hermes/.env`

Abre este archivo con un editor de texto (Notepad, VSCode, etc.) y verifica que contenga:

```env
# API de Claude
ANTHROPIC_API_KEY=tu-clave-api-aqui
MODEL_PROVIDER=anthropic
MODEL_NAME=claude-sonnet-4-8

# Memoria Obsidian
MEMORY_BACKEND=obsidian
MEMORY_PATH=C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro

# Servidor API
API_SERVER_ENABLED=true
API_SERVER_PORT=8642
```

**Ajusta las rutas según tu sistema.**

---

## Paso 7: Configurar el archivo CLAUDE.md

Este archivo es el "manual de instrucciones" que le dice a Claude cómo trabajar con tu bóveda.

### 7.1 Crear el archivo CLAUDE.md

1. Abre Obsidian
2. En tu bóveda, navega a la carpeta `Sistema/`
3. Haz clic derecho → "**New note**" (Nueva nota)
4. Nómbrala: `CLAUDE.md`

### 7.2 Contenido del archivo CLAUDE.md

Copia y pega este contenido en el archivo `CLAUDE.md`:

```markdown
# Sistema Obsidian + Hermes + Claude

## Ubicación de este archivo
Este archivo está en: `Sistema/CLAUDE.md`
Todas las salidas se guardan en: carpetas correspondientes según el tipo

## Quién soy
**Nombre:** [TU NOMBRE]
**Qué hago:** [TU OCUPACIÓN/ACTIVIDAD PRINCIPAL]
**Enfoque principal:** [TU ÁREA DE INTERÉS PRINCIPAL]

## Cómo está organizada mi bóveda

- **00-Inbox/**: Capturas rápidas sin procesar (ideas, notas de voz, screenshots)
- **01-Proyectos/**: Proyectos activos con subcarpetas para cada proyecto
- **02-Areas/**: Áreas de responsabilidad continua (trabajo, salud, finanzas, etc.)
- **03-Recursos/**: Material de referencia organizado por tema
- **04-Archivo/**: Proyectos completados y material obsoleto
- **Sistema/**: Configuración, CLAUDE.md y archivos del sistema

## Proyectos activos

### HomeLab
- **Estado:** [Estado actual del proyecto]
- **Descripción:** Proyecto de laboratorio casero para experimentar con tecnologías
- **Próxima acción:** [Próximo paso específico]
- **Ubicación:** `01-Proyectos/HomeLab/`

### Hermes-Obsidian
- **Estado:** En configuración inicial
- **Descripción:** Integración de Hermes Agent con Obsidian usando Claude como motor de IA
- **Próxima acción:** Completar configuración y documentar todo el proceso
- **Ubicación:** `01-Proyectos/Hermes-Obsidian/`

## Prioridades actuales

1. [PRIORIDAD MÁS IMPORTANTE ESTA SEMANA]
2. [SEGUNDA PRIORIDAD]
3. [TERCERA PRIORIDAD]

## Temas en los que pienso frecuentemente

- [TEMA 1]
- [TEMA 2]
- [TEMA 3]
- [TEMA 4]
- [TEMA 5]

## Mi estilo de escritura

[DESCRIBE CÓMO TE GUSTA ESCRIBIR Y COMUNICARTE]

**Cosas que NUNCA digo o hago:**
- [Ejemplo: No uso emojis excesivos]
- [Ejemplo: No escribo en tercera persona]
- [Ejemplo: Prefiero explicaciones directas sin rodeos]

## Instrucciones para generar salidas

Cuando generes cualquier salida:

1. **Lee primero** la sección relevante de mi bóveda
2. **Referencia notas específicas** usando sus rutas de archivo
3. **Guarda las salidas** en la subcarpeta correcta según el tipo
4. **Nombra archivos** con formato: `YYYY-MM-DD-[tipo]-[tema].md`
5. **Crea frontmatter** apropiado en Obsidian con tipo y fecha

Ejemplo de frontmatter:
```yaml
---
tipo: nota-proyecto
fecha: 2026-08-01
proyecto: HomeLab
etiquetas: [homelab, documentación]
---
```

## Instrucciones de memoria

**Antes de ejecutar cualquier tarea:**
- Lee la memoria relevante de la base de datos de Hermes
- Lee las notas relevantes de la bóveda vía Filesystem
- Combina ambas fuentes para contexto completo

**Después de ejecutar cualquier tarea:**
- Guarda un resumen en la memoria de Hermes con etiquetas apropiadas
- Crea o actualiza la nota relevante en la bóveda

## Actualización semanal

Este archivo se revisa y actualiza cada lunes.

**Última actualización de prioridades:** [FECHA]
```

### 7.3 Personalizar el archivo

Ahora edita el archivo y reemplaza:
- `[TU NOMBRE]` con tu nombre
- `[TU OCUPACIÓN]` con lo que haces
- Todos los campos entre `[corchetes]` con tu información real

---

## Paso 8: Probar la integración

¡Es hora de probar que todo funciona!

### 8.1 Iniciar Hermes

En PowerShell/Terminal, ejecuta:

```powershell
hermes
```

Verás la interfaz de Hermes cargarse. Deberías ver algo como:

```
╔═══════════════════════════════════════╗
║       🤖 Hermes Agent v0.16.0         ║
║   Powered by Claude via Anthropic     ║
╚═══════════════════════════════════════╝

Memory: Obsidian ✓
Provider: Claude (anthropic) ✓
Status: Ready

You: _
```

### 8.2 Primera prueba: Leer tu bóveda

Escribe en el prompt de Hermes:

```
Hola Hermes. Por favor lee mi archivo CLAUDE.md y dime qué proyectos tengo activos.
```

Si todo está bien configurado, Hermes debería:
1. Leer el archivo `Sistema/CLAUDE.md`
2. Responderte con los proyectos que listaste
3. Demostrar que tiene acceso a tu bóveda

### 8.3 Segunda prueba: Escribir en tu bóveda

Ahora prueba que Hermes puede escribir:

```
Por favor crea una nota de bienvenida en mi carpeta Inbox con el título "Prueba de integración exitosa" y un resumen de cómo funciona este sistema.
```

Hermes debería:
1. Crear un archivo en `00-Inbox/`
2. Escribir contenido relevante
3. Confirmarte que se creó la nota

**Verifica en Obsidian:** Deberías ver la nueva nota aparecer en tu carpeta Inbox.

### 8.4 Tercera prueba: Usar contexto de memoria

Ahora prueba la memoria persistente:

```
Recuerda que mi proyecto más importante ahora es configurar este sistema Hermes-Obsidian. ¿Qué deberíamos documentar a continuación?
```

Hermes debería:
1. Recordar el contexto de tus proyectos
2. Sugerir pasos de documentación relevantes
3. Demostrar que entiende el propósito del sistema

### 8.5 ¡Éxito!

Si las tres pruebas funcionaron, **¡FELICITACIONES!** 🎉

Tu sistema Hermes + Obsidian + Claude está funcionando correctamente.

---

## Ejemplos Prácticos: Organizando tus Proyectos

Ahora vamos a usar Hermes para organizar tus proyectos reales: **HomeLab** y **Hermes-Obsidian**.

### Ejemplo 1: Crear estructura para el proyecto HomeLab

**Tú dices a Hermes:**

```
Hermes, necesito organizar mi proyecto HomeLab. Por favor:

1. Crea una carpeta "HomeLab" dentro de "01-Proyectos/"
2. Dentro de HomeLab, crea estas subcarpetas:
   - Planificación
   - Hardware
   - Software
   - Configuraciones
   - Troubleshooting
   - Notas-Diarias

3. Crea un archivo "README.md" en la raíz de HomeLab con:
   - Descripción del proyecto
   - Objetivos
   - Estado actual
   - Próximos pasos

4. Crea una plantilla para notas diarias de trabajo en HomeLab
```

**Hermes ejecutará:**
1. Creará toda la estructura de carpetas
2. Generará el README con contenido relevante
3. Creará una plantilla reutilizable
4. Te confirmará cada acción

### Ejemplo 2: Documentar el proyecto Hermes-Obsidian

**Tú dices a Hermes:**

```
Hermes, quiero documentar todo el proceso de configuración de este sistema. Por favor:

1. Crea una carpeta "Hermes-Obsidian" en "01-Proyectos/"
2. Dentro, crea estas secciones:
   - Instalación (con todos los pasos que seguimos)
   - Configuración (archivos de config y variables)
   - Casos-de-Uso (ejemplos de cómo usar el sistema)
   - Problemas-Resueltos (troubleshooting)

3. Crea un índice principal que enlace a todas las secciones

4. Documenta el proceso completo que acabamos de seguir en esta guía
```

**Hermes creará:**
- Estructura completa del proyecto
- Documentación detallada de cada paso
- Enlaces entre notas relacionadas
- Un índice navegable

### Ejemplo 3: Captura rápida y procesamiento automático

**Escenario:** Tienes una idea para tu HomeLab mientras estás trabajando.

**Tú dices a Hermes:**

```
Captura rápida: Idea para HomeLab - implementar un servidor Plex para streaming de medios local. Investigar hardware necesario y costos.
```

**Hermes automáticamente:**
1. Crea una nota en `00-Inbox/` con timestamp
2. Extrae los puntos clave (servidor Plex, investigación hardware, costos)
3. Etiqueta la nota con #homelab #ideas #plex
4. Te pregunta si quieres moverla a la carpeta del proyecto HomeLab

### Ejemplo 4: Generar un reporte de proyecto

**Tú dices a Hermes:**

```
Por favor genera un reporte del estado actual del proyecto HomeLab. Incluye:
- Resumen de todo lo que hemos documentado
- Tareas pendientes
- Próximos pasos sugeridos
- Enlaces a todas las notas relevantes

Guarda el reporte en "01-Proyectos/HomeLab/Reportes/" con la fecha de hoy.
```

**Hermes:**
1. Lee todas las notas del proyecto HomeLab
2. Analiza el contenido y extrae información clave
3. Genera un reporte estructurado en Markdown
4. Guarda el archivo con formato `2026-08-01-Reporte-HomeLab.md`
5. Crea enlaces a todas las notas mencionadas

### Ejemplo 5: Crear una bitácora diaria automática

**Configura una tarea programada con Hermes:**

```
Hermes, configura una tarea diaria que se ejecute cada noche a las 10 PM:

1. Revisa todas las notas que creé hoy
2. Genera un resumen de lo que trabajé
3. Identifica próximos pasos para mañana
4. Guarda la bitácora en "02-Areas/Bitacoras-Diarias/"
5. Etiqueta por proyecto al que pertenece cada actividad
```

**Resultado:** Cada noche tendrás automáticamente un resumen de tu día sin mover un dedo.

### Ejemplo 6: Búsqueda inteligente contextual

**Tú preguntas:**

```
Hermes, ¿qué decisiones importantes he tomado sobre el HomeLab en las últimas dos semanas?
```

**Hermes:**
1. Busca en todas las notas del proyecto HomeLab
2. Identifica entradas etiquetadas como decisiones
3. Filtra por fecha (últimas dos semanas)
4. Te presenta un resumen con enlaces a las notas originales

### Ejemplo 7: Conectar ideas entre proyectos

**Tú dices:**

```
Hermes, analiza mis proyectos HomeLab y Hermes-Obsidian. ¿Hay alguna sinergía o forma en que uno pueda ayudar al otro?
```

**Hermes:**
1. Lee las notas de ambos proyectos
2. Identifica conexiones potenciales
3. Sugiere ideas como:
   - "Podrías usar Hermes para automatizar la documentación de tu HomeLab"
   - "Podrías correr Hermes Agent en tu servidor HomeLab para tenerlo 24/7"
   - "El HomeLab podría ser un buen caso de estudio para probar capacidades de Hermes"

---

## Solución de Problemas

### Problema: "Command 'hermes' not found"

**Causa:** Python o Hermes no están en el PATH del sistema.

**Solución:**

1. Verifica que Python esté instalado:
   ```powershell
   python --version
   ```

2. Reinstala Hermes:
   ```powershell
   pip install --upgrade hermes-agent
   ```

3. En Windows, reinicia PowerShell después de instalar

### Problema: "Authentication failed" al usar Claude

**Causa:** La API Key no está configurada correctamente.

**Solución:**

1. Verifica que la variable de entorno esté configurada:
   ```powershell
   echo $env:ANTHROPIC_API_KEY
   ```

2. Si está vacía, configúrala de nuevo:
   ```powershell
   setx ANTHROPIC_API_KEY "tu-clave-api-aqui"
   ```

3. Cierra y vuelve a abrir PowerShell

4. Verifica el archivo `.env`:
   ```
   C:\Users\TU_USUARIO\.hermes\.env
   ```
   Debe contener: `ANTHROPIC_API_KEY=tu-clave-aqui`

### Problema: Hermes no puede leer/escribir en Obsidian

**Causa:** La ruta a la bóveda está mal configurada.

**Solución:**

1. Verifica la ruta configurada:
   ```powershell
   hermes memory status
   ```

2. Si la ruta es incorrecta, reconfigura:
   ```powershell
   hermes memory setup --provider obsidian --path "RUTA_CORRECTA"
   ```

3. Asegúrate de usar la ruta COMPLETA (absoluta), no relativa

4. En Windows, usa comillas dobles y barras invertidas:
   ```
   "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro"
   ```

### Problema: Hermes responde muy lento

**Causa:** Modelo muy grande o conexión a Internet lenta.

**Solución:**

1. Cambia a un modelo más rápido en `.env`:
   ```env
   MODEL_NAME=claude-sonnet-3-5  # Más rápido que opus
   ```

2. Verifica tu conexión a Internet

3. Considera usar un modelo local con Ollama si quieres trabajar offline

### Problema: "Rate limit exceeded" (Límite de tasa excedido)

**Causa:** Estás haciendo demasiadas peticiones a la API de Claude muy rápido.

**Solución:**

1. Espera 1 minuto antes de hacer otra petición

2. Verifica tu tier en Anthropic Console:
   - Tier 1: 50 peticiones por minuto
   - Tier 2: 1000 peticiones por minuto

3. Si necesitas más, contacta a Anthropic para upgrade

### Problema: Archivos .md no se ven bien en Obsidian

**Causa:** Formato Markdown incorrecto.

**Solución:**

1. Verifica que los archivos tengan extensión `.md`

2. Usa un validador de Markdown online:
   - https://markdownlivepreview.com/

3. Asegúrate de que Hermes use frontmatter correcto:
   ```yaml
   ---
   título: Nombre de la nota
   fecha: 2026-08-01
   ---
   ```

### Problema: Obsidian no sincroniza cambios de Hermes

**Causa:** Obsidian no detecta cambios externos automáticamente.

**Solución:**

1. En Obsidian, ve a: `Settings` → `Files & Links`

2. Activa: `Automatically update internal links`

3. Activa: `Detect all file extensions`

4. Para refrescar manualmente: `Ctrl+R` (Windows) o `Cmd+R` (Mac)

### Problema: Costos inesperadamente altos de API

**Causa:** Uso excesivo o prompts muy largos.

**Solución:**

1. Monitorea tu uso en: https://console.anthropic.com/usage

2. Establece un límite de gasto mensual en Billing

3. Optimiza tus prompts:
   - Sé específico y conciso
   - No envíes el mismo prompt repetidamente
   - Usa modelos más económicos para tareas simples

4. Considera usar caching de Claude para prompts repetidos:
   ```env
   ENABLE_PROMPT_CACHING=true
   ```

---

## Consejos y Mejores Prácticas

### 🎯 Para organizar tu bóveda

1. **Usa una estructura simple**
   - No crees demasiadas carpetas al inicio
   - Empieza con las 5-6 carpetas principales
   - Deja que la estructura evolucione con el uso

2. **Convenciones de nombres**
   - Usa guiones (`-`) en lugar de espacios
   - Incluye fechas en formato ISO: `YYYY-MM-DD`
   - Sé descriptivo pero conciso

3. **Etiquetas vs Carpetas**
   - Carpetas: Para organización principal (proyectos, áreas)
   - Etiquetas: Para clasificación cruzada (temas, estados)
   - Ejemplo: Un archivo puede estar en `Proyectos/HomeLab/` y tener etiquetas `#networking #hardware`

### 📝 Para trabajar con Hermes

1. **Sé específico en tus instrucciones**
   ❌ Malo: "Organiza mis notas"
   ✅ Bueno: "Organiza las notas en Inbox del último mes por proyecto y muévelas a sus carpetas correspondientes"

2. **Confirma acciones importantes**
   - Pídele a Hermes que te muestre un resumen antes de ejecutar
   - Usa "modo borrador" para revisar contenido antes de guardarlo
   - Haz backups regulares de tu bóveda

3. **Aprovecha la memoria persistente**
   - Dale contexto una vez, lo recordará para siempre
   - Actualiza regularmente tu `CLAUDE.md` con nuevas prioridades
   - Usa referencias: "Como discutimos ayer sobre X..."

### 💡 Para optimizar costos

1. **Usa el modelo apropiado**
   - Tareas simples: `claude-haiku` (más barato)
   - Tareas complejas: `claude-sonnet` (balance)
   - Tareas muy complejas: `claude-opus` (más caro)

2. **Habilita prompt caching**
   - Reduce costos en un 90% para prompts repetidos
   - Ideal para tu `CLAUDE.md` que se lee frecuentemente

3. **Monitorea tu uso**
   - Revisa el dashboard de Anthropic semanalmente
   - Establece alertas de gasto
   - Típico uso personal: $5-15 USD/mes

### 🔒 Para seguridad y privacidad

1. **Tus datos están seguros**
   - Todo se guarda localmente en tu computadora
   - Obsidian no sube nada a la nube (a menos que configures sync)
   - Claude solo ve lo que le envías explícitamente

2. **Protege tu API Key**
   - Nunca la compartas públicamente
   - No la subas a GitHub o repositorios públicos
   - Rotala cada 3-6 meses

3. **Backups regulares**
   - Tu bóveda es solo una carpeta - haz copias
   - Usa Git para versionar tu bóveda
   - Considera Obsidian Sync o alternativas (Syncthing, Dropbox)

### ⚡ Para productividad máxima

1. **Workflows automatizados**
   - Configura tareas nocturnas (bitácoras, resúmenes)
   - Usa plantillas para notas recurrentes
   - Programa revisiones semanales automáticas

2. **Captura rápida**
   - Ten Obsidian siempre abierto
   - Usa la carpeta Inbox sin miedo
   - Deja que Hermes procese y organice después

3. **Enlaces y contexto**
   - Enlaza notas relacionadas usando `[[Nombre-Nota]]`
   - Hermes puede seguir estos enlaces para contexto
   - Crea "notas índice" para temas importantes

### 🚀 Próximos pasos sugeridos

Una vez que domines lo básico, puedes:

1. **Integrar con Telegram**
   - Hermes puede conectarse a Telegram
   - Envía notas desde tu teléfono
   - Recibe resúmenes automáticos

2. **Usar modelos locales**
   - Instala Ollama para modelos offline
   - Experimenta con LLaMA, Mistral, etc.
   - Cero costos de API

3. **Crear skills personalizados**
   - Hermes puede aprender nuevas habilidades
   - Crea automatizaciones específicas para tu workflow
   - Comparte skills con la comunidad

4. **Explorar plugins de Obsidian**
   - Dataview: Consultas SQL sobre tus notas
   - Templater: Plantillas avanzadas
   - Calendar: Vista de calendario de notas diarias

---

## FAQ (Preguntas Frecuentes)

### ❓ Preguntas Generales

**P: ¿Necesito pagar para usar este sistema?**
R: Solo necesitas pagar por el uso de la API de Claude. Obsidian y Hermes son completamente gratuitos. El costo promedio de Claude para uso personal es $5-15 USD/mes, y te dan $5 de crédito gratis para empezar.

**P: ¿Mis datos están seguros?**
R: Sí. Tus notas se guardan localmente en tu computadora. Solo se envía a Claude la información que explícitamente solicites procesar. Obsidian no sube nada a la nube a menos que configures sincronización opcional.

**P: ¿Funciona sin conexión a Internet?**
R: Parcialmente. Obsidian funciona completamente offline. Hermes necesita conexión para usar Claude, pero puedes configurarlo con modelos locales (Ollama) para trabajar completamente offline.

**P: ¿Puedo usar ChatGPT en lugar de Claude?**
R: Sí. Hermes soporta múltiples proveedores de IA incluyendo OpenAI (ChatGPT), Anthropic (Claude), y modelos locales. Solo cambia la configuración en el archivo `.env`.

**P: ¿Cuánto espacio en disco necesito?**
R: Mínimo 2GB. Tu bóveda de Obsidian crecerá con el tiempo, pero los archivos Markdown son muy ligeros. Incluso con miles de notas, raramente supera 1GB.

**P: ¿Funciona en Mac, Linux y Windows?**
R: Sí, las tres herramientas (Obsidian, Hermes, Claude) funcionan en todos los sistemas operativos principales.

### ⚙️ Preguntas Técnicas

**P: ¿Qué versión de Python necesito?**
R: Python 3.10 o superior. La versión recomendada es Python 3.12 (la más reciente estable).

**P: ¿Puedo tener múltiples bóvedas de Obsidian?**
R: Sí. Puedes crear múltiples bóvedas y cambiar entre ellas en Obsidian. Para usar diferentes bóvedas con Hermes, reconfigura con `hermes memory setup --provider obsidian --path "NUEVA_RUTA"`.

**P: ¿Hermes puede acceder a archivos fuera de la bóveda?**
R: Sí, pero debes darle permiso explícitamente. Por defecto, Hermes solo trabaja con la bóveda configurada para seguridad.

**P: ¿Puedo usar Hermes en mi teléfono móvil?**
R: No directamente. Hermes funciona en computadoras. Sin embargo, puedes:
- Usar Obsidian Mobile (app oficial) para acceder a tu bóveda desde el teléfono
- Conectar Hermes con Telegram y enviar comandos desde tu móvil
- Acceder remotamente a tu computadora donde corre Hermes

**P: ¿Qué pasa si me quedo sin créditos de Claude?**
R: Hermes dejará de funcionar hasta que recargues créditos o cambies a otro proveedor (OpenAI, modelos locales). Tus notas en Obsidian permanecen intactas y accesibles.

### 🔧 Preguntas de Uso

**P: ¿Cómo hago backup de mi bóveda?**
R: Tu bóveda es solo una carpeta. Opciones:
1. Copia manual: Copia toda la carpeta a otro lugar
2. Git: Versiona tu bóveda con Git/GitHub
3. Cloud: Usa Dropbox, Google Drive, OneDrive
4. Obsidian Sync: Servicio oficial de pago ($10/mes)

**P: ¿Puedo compartir mi bóveda con otras personas?**
R: Sí. Como son archivos Markdown estándar, puedes compartir:
- Carpetas individuales
- Notas específicas
- Toda la bóveda
- Vía Git, cloud storage, o Obsidian Publish

**P: ¿Hermes puede cometer errores?**
R: Sí, es IA y puede equivocarse. Por eso es importante:
- Revisar contenido importante antes de guardarlo
- Hacer backups regulares
- Usar control de versiones (Git)
- Verificar datos críticos manualmente

**P: ¿Puedo deshacer algo que Hermes hizo mal?**
R: Si usas Git para versionar tu bóveda, puedes revertir cualquier cambio. Sin Git, Obsidian guarda una "papelera" de archivos eliminados por 30 días.

**P: ¿Cómo actualizo Hermes cuando hay una nueva versión?**
R: Ejecuta: `pip install --upgrade hermes-agent`

---

## Referencia Rápida: Comandos de Hermes Más Útiles

### 📋 Comandos Básicos

```powershell
# Iniciar Hermes
hermes

# Verificar versión instalada
hermes --version

# Ver ayuda general
hermes --help

# Configuración inicial
hermes setup
```

### 🧠 Comandos de Memoria

```powershell
# Configurar memoria con Obsidian
hermes memory setup --provider obsidian --path "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro"

# Ver estado de la memoria
hermes memory status

# Cambiar a otra bóveda
hermes memory setup --provider obsidian --path "NUEVA_RUTA"

# Limpiar caché de memoria
hermes memory clear-cache

# Ver estadísticas de uso de memoria
hermes memory stats
```

### 🔑 Comandos de Configuración

```powershell
# Ver configuración actual
hermes config show

# Cambiar modelo de IA
hermes config set MODEL_NAME claude-sonnet-4-8

# Cambiar proveedor de IA
hermes config set MODEL_PROVIDER anthropic

# Habilitar/deshabilitar servidor API
hermes config set API_SERVER_ENABLED true

# Ver ubicación del archivo de configuración
hermes config path
```

### 🔌 Comandos de Plugins y Skills

```powershell
# Listar plugins instalados
hermes plugins list

# Instalar un plugin
hermes plugins install NOMBRE_PLUGIN

# Habilitar un plugin
hermes plugins enable NOMBRE_PLUGIN

# Deshabilitar un plugin
hermes plugins disable NOMBRE_PLUGIN

# Ver skills disponibles
hermes skills list

# Crear un nuevo skill
hermes skills create NOMBRE_SKILL
```

### 🌐 Comandos del Servidor API

```powershell
# Iniciar servidor API en background
hermes server start

# Detener servidor API
hermes server stop

# Ver estado del servidor
hermes server status

# Reiniciar servidor
hermes server restart
```

### 🔍 Comandos de Diagnóstico

```powershell
# Diagnosticar problemas del sistema
hermes doctor

# Ver logs de Hermes
hermes logs

# Ver logs con más detalle
hermes logs --verbose

# Limpiar caché y archivos temporales
hermes clean

# Resetear configuración a valores predeterminados
hermes reset --confirm
```

### 📊 Comandos de Uso y Estadísticas

```powershell
# Ver uso de API (tokens consumidos)
hermes usage

# Ver historial de conversaciones
hermes history

# Exportar conversación específica
hermes history export --id CONVERSATION_ID --output archivo.md

# Limpiar historial antiguo
hermes history clear --older-than 30d
```

---

## Atajos de Obsidian para Productividad

### ⌨️ Navegación Básica

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `Ctrl + N` | `Cmd + N` | Nueva nota |
| `Ctrl + O` | `Cmd + O` | Abrir búsqueda rápida |
| `Ctrl + P` | `Cmd + P` | Paleta de comandos |
| `Ctrl + ,` | `Cmd + ,` | Abrir configuración |
| `Ctrl + Tab` | `Cmd + Tab` | Cambiar entre notas recientes |
| `Ctrl + E` | `Cmd + E` | Alternar modo edición/vista |
| `Ctrl + W` | `Cmd + W` | Cerrar pestaña actual |

### 📝 Edición de Texto

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `Ctrl + B` | `Cmd + B` | **Negrita** |
| `Ctrl + I` | `Cmd + I` | *Cursiva* |
| `Ctrl + K` | `Cmd + K` | Insertar enlace |
| `Ctrl + ]` | `Cmd + ]` | Indentar |
| `Ctrl + [` | `Cmd + [` | Des-indentar |
| `Ctrl + D` | `Cmd + D` | Eliminar línea actual |
| `Ctrl + Shift + D` | `Cmd + Shift + D` | Duplicar línea |

### 🔗 Enlaces y Referencias

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `[[` | `[[` | Crear/buscar enlace interno |
| `![[` | `![[` | Embeber/insertar archivo |
| `Ctrl + Hover` | `Cmd + Hover` | Vista previa de enlace |
| `Ctrl + Click` | `Cmd + Click` | Abrir enlace en nueva pestaña |
| `Alt + Click` | `Alt + Click` | Abrir enlace en panel derecho |

### 🔍 Búsqueda y Navegación

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `Ctrl + F` | `Cmd + F` | Buscar en nota actual |
| `Ctrl + Shift + F` | `Cmd + Shift + F` | Buscar en toda la bóveda |
| `Ctrl + G` | `Cmd + G` | Abrir vista de gráfico |
| `Ctrl + Alt + ←` | `Cmd + Alt + ←` | Navegar atrás |
| `Ctrl + Alt + →` | `Cmd + Alt + →` | Navegar adelante |

### 📋 Listas y Tareas

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `Ctrl + L` | `Cmd + L` | Alternar checkbox (tarea) |
| `Ctrl + Enter` | `Cmd + Enter` | Marcar/desmarcar tarea |
| `Ctrl + Shift + L` | `Cmd + Shift + L` | Convertir a lista |

### 🎨 Visuales

| Atajo (Windows) | Atajo (Mac) | Acción |
|-----------------|-------------|--------|
| `Ctrl + /` | `Cmd + /` | Mostrar/ocultar barra lateral izquierda |
| `Ctrl + \` | `Cmd + \` | Mostrar/ocultar barra lateral derecha |
| `Ctrl + R` | `Cmd + R` | Refrescar archivos (detectar cambios externos) |
| `F11` | `F11` | Modo pantalla completa |

### 💡 Tips de Atajos Personalizados

Puedes crear tus propios atajos en:
`Settings` → `Hotkeys` → Buscar acción → Asignar atajo

**Atajos recomendados para personalizar:**
- "Move file to..." (Mover archivo a...)
- "Insert template" (Insertar plantilla)
- "Open today's daily note" (Abrir nota diaria de hoy)
- "Toggle pin" (Fijar/desfijar pestaña)

---

## Flujos de Trabajo Recomendados

### 🌅 Rutina Matutina (5-10 minutos)

**Objetivo:** Empezar el día con claridad y contexto.

1. **Abrir Obsidian**
   - Revisa tu nota diaria del día anterior
   - Ve qué quedó pendiente

2. **Consultar a Hermes**
   ```
   Hermes, dame un resumen de mis prioridades para hoy basado en mis proyectos activos.
   ```

3. **Crear nota diaria de hoy**
   - Usa una plantilla (Hermes puede crearla)
   - Incluye: fecha, prioridades del día, espacios para notas

4. **Revisar inbox**
   ```
   Hermes, revisa mi carpeta Inbox y sugiere cómo organizar las notas que capturé ayer.
   ```

### 📝 Captura Durante el Día

**Objetivo:** Capturar ideas sin interrumpir el flujo de trabajo.

**Método 1: Captura rápida en Obsidian**
1. `Ctrl + N` → Nueva nota en Inbox
2. Escribe la idea sin preocuparte por formato
3. Agrega `#inbox` al final
4. Continúa trabajando

**Método 2: Captura con Hermes**
1. Abre chat de Hermes
2. Escribe: `Captura: [tu idea]`
3. Hermes la guarda automáticamente en Inbox con timestamp

**Método 3: Captura por voz (si usas Telegram con Hermes)**
1. Envía nota de voz a tu bot de Hermes en Telegram
2. Se transcribe y guarda automáticamente

### 🗂️ Procesamiento Semanal (30 minutos, ej: viernes tarde o domingo)

**Objetivo:** Organizar lo capturado, revisar progreso.

1. **Procesar Inbox**
   ```
   Hermes, analiza todas las notas en mi Inbox de esta semana.
   Para cada una:
   - Si es una tarea, añádela al proyecto correspondiente
   - Si es una idea, muévela a Recursos con etiquetas apropiadas
   - Si es basura, márcala para eliminar
   - Si necesita más contexto, déjala en Inbox pero agrégale un tag #revisar
   ```

2. **Revisar proyectos activos**
   ```
   Hermes, genera un reporte de estado de todos mis proyectos activos:
   - Qué avanzó esta semana
   - Qué está bloqueado
   - Próximos pasos para la semana que viene
   ```

3. **Actualizar CLAUDE.md**
   - Revisa tus prioridades
   - Actualiza estado de proyectos
   - Ajusta próximas acciones

4. **Generar bitácora semanal**
   ```
   Hermes, crea una bitácora semanal para la semana del [fecha] al [fecha].
   Incluye:
   - Logros principales
   - Aprendizajes
   - Decisiones importantes
   - Plan para la próxima semana
   Guárdala en 02-Areas/Bitacoras-Semanales/
   ```

### 🎯 Inicio de Proyecto Nuevo

**Objetivo:** Establecer estructura y claridad desde el principio.

1. **Crear estructura del proyecto**
   ```
   Hermes, necesito iniciar un nuevo proyecto llamado "[Nombre]".
   
   Por favor:
   1. Crea una carpeta "[Nombre]" en 01-Proyectos/
   2. Dentro, crea:
      - README.md (descripción, objetivos, contexto)
      - Planificacion.md (roadmap, hitos)
      - Recursos.md (enlaces, referencias)
      - Notas/ (carpeta para notas del día a día)
      - Decisiones.md (registro de decisiones importantes)
   3. Crea una plantilla para notas diarias de este proyecto
   ```

2. **Brainstorm inicial con Hermes**
   ```
   Hermes, ayúdame a pensar en el proyecto [Nombre].
   
   Contexto: [describe brevemente]
   
   Necesito:
   - Posibles enfoques para abordar esto
   - Recursos que debería investigar
   - Riesgos potenciales
   - Primeros pasos concretos
   ```

3. **Configurar seguimiento**
   - Agrega el proyecto a tu `CLAUDE.md`
   - Define métrica de éxito
   - Establece check-ins (ej: revisar cada viernes)

### 🔍 Investigación y Aprendizaje

**Objetivo:** Acumular y conectar conocimiento de forma estructurada.

**Flujo de investigación:**

1. **Captura inicial**
   - Encuentra artículo/video/libro interesante
   - Guarda enlace en Inbox con contexto: "Sobre: [tema]"

2. **Procesamiento profundo**
   ```
   Hermes, he leído este artículo sobre [tema]: [enlace o texto].
   
   Por favor:
   1. Extrae las ideas clave (3-5 puntos)
   2. Revisa si tengo notas relacionadas en mi bóveda
   3. Si hay conexiones, crea enlaces [[nota-existente]]
   4. Si es conocimiento nuevo, crea una nota permanente en 03-Recursos/[tema]/
   5. Sugiere próximos pasos o lecturas relacionadas
   ```

3. **Conexión de ideas**
   ```
   Hermes, acabo de aprender sobre [concepto X].
   ¿Hay algo en mis notas que se relacione con esto? Busca conexiones no obvias.
   ```

### 📊 Revisión Mensual (1-2 horas)

**Objetivo:** Perspectiva macro, ajustar rumbo.

1. **Análisis de progreso**
   ```
   Hermes, genera un reporte mensual del mes de [mes]:
   
   - Proyectos completados vs iniciados
   - Temas más frecuentes en mis notas
   - Áreas donde invertí más tiempo
   - Objetivos cumplidos vs no cumplidos
   - Tendencias (¿en qué dirección va mi trabajo/aprendizaje?)
   ```

2. **Mantenimiento de bóveda**
   ```
   Hermes, ayúdame a limpiar la bóveda:
   
   - Identifica notas huérfanas (sin enlaces de/hacia ellas)
   - Encuentra duplicados potenciales
   - Sugiere notas que deberían moverse a Archivo (proyectos completados hace >3 meses)
   - Identifica tags inconsistentes o poco usados
   ```

3. **Reflexión y planificación**
   - ¿Qué aprendí este mes?
   - ¿Qué patrones noto en mi trabajo?
   - ¿Necesito ajustar mi sistema o estructura?
   - ¿Qué quiero lograr el próximo mes?

### 💼 Flujo de Trabajo para Reuniones

**Antes de la reunión:**
```
Hermes, tengo una reunión mañana sobre [tema] con [personas].
Revisa mis notas sobre [tema] y dame:
- Resumen del contexto
- Decisiones previas relacionadas
- Puntos importantes que debería mencionar
```

**Durante la reunión:**
- Toma notas rápidas en Obsidian
- No te preocupes por formato
- Usa abreviaciones

**Después de la reunión:**
```
Hermes, tomé estas notas en la reunión sobre [tema]:
[pega tus notas]

Por favor:
1. Limpia y estructura las notas
2. Extrae action items (tareas)
3. Identifica decisiones tomadas
4. Crea enlaces a proyectos/personas mencionadas
5. Guarda en 01-Proyectos/[proyecto-relevante]/Notas/YYYY-MM-DD-reunion-[tema].md
```

---

## Troubleshooting Avanzado

### 🔴 Problema: Hermes consume mucha RAM

**Síntomas:**
- Tu computadora se pone lenta cuando Hermes está corriendo
- Task Manager muestra uso alto de memoria
- Hermes tarda mucho en responder

**Causas posibles:**
1. Bóveda muy grande con miles de archivos
2. Caché de memoria muy grande
3. Múltiples conversaciones abiertas simultáneamente

**Soluciones:**

1. **Limitar tamaño de caché**
   
   Edita `C:\Users\TU_USUARIO\.hermes\config.yaml`:
   ```yaml
   memory:
     cache_size_mb: 512  # Reduce si es necesario (default: 1024)
     max_documents: 1000  # Limita documentos en memoria
   ```

2. **Limpiar caché periódicamente**
   ```powershell
   hermes memory clear-cache
   ```

3. **Indexar solo carpetas relevantes**
   
   En lugar de indexar toda la bóveda, configura solo las carpetas importantes:
   ```powershell
   hermes config set MEMORY_INCLUDE_PATHS "01-Proyectos,02-Areas,Sistema"
   hermes config set MEMORY_EXCLUDE_PATHS "04-Archivo,03-Recursos/Descartado"
   ```

4. **Usar modo "low memory"**
   ```powershell
   hermes config set MEMORY_MODE low
   ```

### 🔴 Problema: Conflictos de sincronización con múltiples dispositivos

**Síntomas:**
- Archivos duplicados con "_conflict" en el nombre
- Pérdida de cambios recientes
- Errores al abrir notas

**Causas:**
- Edición simultánea desde múltiples dispositivos
- Sincronización activa (Dropbox/OneDrive) + Hermes modificando archivos

**Soluciones:**

1. **Regla de oro: Un dispositivo a la vez**
   - No edites la misma nota desde dos lugares simultáneamente
   - Espera a que sincronice antes de cambiar de dispositivo

2. **Configurar exclusiones en sync**
   
   Excluye de sincronización automática:
   - `.obsidian/workspace` (configuración local)
   - `.hermes/cache/` (caché local)
   - Archivos temporales `.tmp`

3. **Usar Git para versionar (recomendado)**
   
   Git maneja conflictos mejor que Dropbox:
   ```powershell
   cd "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro"
   git init
   git add .
   git commit -m "Initial commit"
   ```
   
   Antes de editar desde otro dispositivo:
   ```bash
   git pull
   ```
   
   Después de editar:
   ```bash
   git add .
   git commit -m "Actualizaciones del [fecha]"
   git push
   ```

4. **Resolver conflictos manualmente**
   
   Si aparecen archivos de conflicto:
   ```
   Hermes, tengo estos archivos de conflicto:
   - Nota.md
   - Nota_conflict_2026-08-02.md
   
   Compáralos y ayúdame a fusionar los cambios manteniendo lo mejor de ambos.
   ```

### 🔴 Problema: Hermes da respuestas inconsistentes

**Síntomas:**
- Respuestas contradictorias sobre el mismo tema
- "Olvida" información que acabas de darle
- No sigue las instrucciones de CLAUDE.md

**Causas:**
1. CLAUDE.md desactualizado o mal formateado
2. Contexto fragmentado en múltiples conversaciones
3. Caché corrupto

**Soluciones:**

1. **Verificar y actualizar CLAUDE.md**
   ```
   Hermes, lee mi archivo Sistema/CLAUDE.md y dime si hay algo ambiguo o contradictorio.
   ```
   
   Asegúrate de que CLAUDE.md tenga:
   - Información actualizada
   - Instrucciones claras y no contradictorias
   - Formato Markdown correcto

2. **Limpiar caché y reiniciar conversación**
   ```powershell
   hermes memory clear-cache
   hermes history clear --older-than 7d
   ```
   
   Luego inicia nueva conversación:
   ```
   Hermes, por favor lee mi CLAUDE.md y confirma que entiendes mis proyectos actuales.
   ```

3. **Usar contexto explícito**
   
   En lugar de asumir que Hermes recuerda:
   ```
   ❌ Malo: "Continúa con lo de ayer"
   ✅ Bueno: "Continúa con el proyecto HomeLab que estamos documentando. La última nota fue sobre configuración de red."
   ```

4. **Revisar logs de Hermes**
   ```powershell
   hermes logs --verbose
   ```
   
   Busca errores como:
   - `Failed to read CLAUDE.md`
   - `Memory cache corrupted`
   - `Context window exceeded`

### 🔴 Problema: Errores de formato en archivos Markdown

**Síntomas:**
- Enlaces rotos `[[Nota]]` no funcionan
- Frontmatter causa errores
- Código o tablas se muestran mal

**Soluciones:**

1. **Validar sintaxis Markdown**
   
   Usa un linter de Markdown:
   ```powershell
   # Instalar markdownlint-cli
   npm install -g markdownlint-cli
   
   # Validar archivo
   markdownlint "C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro\01-Proyectos\HomeLab\README.md"
   ```

2. **Pedirle a Hermes que corrija formato**
   ```
   Hermes, este archivo tiene errores de formato:
   [ruta del archivo]
   
   Por favor:
   1. Identifica los problemas
   2. Corrígelos siguiendo el estándar de Markdown
   3. Asegúrate de que el frontmatter sea válido YAML
   4. Verifica que todos los enlaces [[internos]] usen sintaxis correcta
   ```

3. **Usar plantillas validadas**
   
   Crea plantillas con formato correcto y reutilízalas:
   ```markdown
   ---
   title: Título de la nota
   date: {{date:YYYY-MM-DD}}
   tags: [tag1, tag2]
   project: nombre-proyecto
   ---
   
   # {{title}}
   
   ## Contenido
   
   Tu contenido aquí...
   ```

### 🔴 Problema: La API de Claude devuelve errores 429 o 500

**Error 429: Too Many Requests**

**Causa:** Límite de tasa excedido (demasiadas peticiones muy rápido).

**Soluciones:**
1. Espera 60 segundos antes de reintentar
2. Reduce frecuencia de peticiones
3. Implementa rate limiting en Hermes:
   ```yaml
   # En config.yaml
   api:
     rate_limit:
       requests_per_minute: 40  # Menos que el límite de tu tier
       retry_after_seconds: 60
   ```

**Error 500/502/503: Server Error**

**Causa:** Problemas temporales en servidores de Anthropic.

**Soluciones:**
1. Verifica estado del servicio: https://status.anthropic.com
2. Espera 5-10 minutos y reintenta
3. Configura reintento automático:
   ```yaml
   api:
     retry:
       max_attempts: 3
       backoff_factor: 2
   ```

### 🔴 Problema: Git muestra conflictos con archivos de Obsidian

**Archivos problemáticos comunes:**
- `.obsidian/workspace`
- `.obsidian/workspace.json`
- `.obsidian/graph.json`

**Solución: Crear .gitignore apropiado**

Crea `C:\Users\mgabi\Documents\Obsidian\Mi-Segundo-Cerebro\.gitignore`:

```gitignore
# Obsidian
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.obsidian/plugins/*/data.json
.trash/

# Hermes
.hermes/cache/
*.tmp
*.temp

# Sistema
.DS_Store
Thumbs.db
desktop.ini

# Backup
*.backup
*_backup_*
```

Si ya hay conflictos:
```powershell
git checkout --theirs .obsidian/workspace.json
git add .gitignore
git commit -m "Add gitignore for Obsidian config files"
```

### 🔴 Problema: Obsidian no detecta cambios de Hermes en tiempo real

**Causa:** Obsidian cachea el estado de archivos.

**Soluciones:**

1. **Refrescar manualmente:** `Ctrl + R` (Windows) o `Cmd + R` (Mac)

2. **Habilitar detección automática:**
   
   Settings → Files & Links:
   - ✅ `Detect all file extensions`
   - ✅ `Automatically update internal links`

3. **Usar plugin "Restart" (reinicio rápido)**
   
   Instala el plugin community "Restart" para refrescar sin cerrar Obsidian.

4. **Configurar Obsidian para verificar cambios más frecuentemente:**
   
   Settings → About → Advanced:
   Reduce "File recovery" interval a 30 segundos

---

## Centro de Soporte y Comunidad

### 📚 Documentación Oficial

- **Hermes Agent:** https://github.com/NousResearch/hermes-agent
- **Obsidian:** https://help.obsidian.md/
- **Claude API:** https://docs.anthropic.com/

### 🎓 Tutoriales y Guías

- **Obsidian for Beginners:** https://obsidian.rocks/
- **Hermes Agent Examples:** https://hermes-agent.nousresearch.com/examples
- **Claude Prompt Engineering:** https://docs.anthropic.com/claude/docs/prompt-engineering
- **Markdown Guide:** https://www.markdownguide.org/
- **Git Basics:** https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git

### 👬 Comunidades

- **Obsidian Forum:** https://forum.obsidian.md/
- **Hermes Discord:** (busca en el GitHub de Hermes)
- **r/ObsidianMD:** https://reddit.com/r/ObsidianMD
- **r/artificial (en español):** https://reddit.com/r/inteligenciaartificial
- **Discord de Claude:** https://discord.gg/anthropic

### 🛠️ Herramientas Complementarias

- **Ollama:** Modelos de IA locales - https://ollama.ai/
- **Omi:** Captura de memoria pasiva - https://github.com/BasedHardware/omi
- **Obsidian Sync:** Sincronización oficial (de pago) - https://obsidian.md/sync
- **Syncthing:** Sincronización gratuita entre dispositivos - https://syncthing.net/
- **Obsidian Git Plugin:** Plugin para versionamiento automático
- **Dataview Plugin:** Consultas tipo base de datos sobre tus notas

### 🎯 Cómo Obtener Ayuda

**Si tienes un problema específico:**

1. **Consulta esta guía primero**
   - Revisa la sección "Solución de Problemas"
   - Revisa "Troubleshooting Avanzado"
   - Revisa el FAQ

2. **Busca en la documentación oficial**
   - Hermes: GitHub Issues y Wiki
   - Obsidian: Help docs y Forum
   - Claude: Documentación de Anthropic

3. **Pregunta en comunidades**
   - **Para Obsidian:** Forum de Obsidian o r/ObsidianMD
   - **Para Hermes:** GitHub Issues del proyecto
   - **Para Claude API:** Discord de Anthropic o soporte oficial

4. **Usa Hermes para diagnosticar**
   ```
   Hermes, estoy teniendo este problema: [describe el problema].
   
   Por favor:
   1. Diagnostica qué podría estar causando esto
   2. Sugiere pasos de troubleshooting
   3. Revisa mis logs si es necesario
   ```

**Si quieres compartir tu experiencia o contribuir:**

1. **Documenta en tu bóveda**
   - Crea una nota con lo que aprendiste
   - Comparte tips y trucos que descubriste

2. **Contribuye a la comunidad**
   - Comparte tus plantillas en los foros
   - Ayuda a otros con problemas similares
   - Crea plugins o skills para Hermes

3. **Reporta bugs**
   - Hermes: https://github.com/NousResearch/hermes-agent/issues
   - Obsidian: https://forum.obsidian.md/c/bug-reports/7

### 📧 Soporte Oficial

**Hermes Agent:**
- GitHub Issues: https://github.com/NousResearch/hermes-agent/issues
- Documentación: https://hermes-agent.nousresearch.com
- No hay soporte de pago (es open source)

**Obsidian:**
- Email de soporte: support@obsidian.md (para usuarios de pago)
- Forum: https://forum.obsidian.md/ (soporte comunitario gratuito)
- Discord: https://discord.gg/veuWUTm

**Claude / Anthropic:**
- Email de soporte: support@anthropic.com
- Console de API: https://console.anthropic.com
- Status del servicio: https://status.anthropic.com
- Documentación: https://docs.anthropic.com

### ✅ Checklist de Troubleshooting General

Antes de pedir ayuda, verifica:

- [ ] ¿Reiniciaste Hermes?
- [ ] ¿Reiniciaste Obsidian?
- [ ] ¿Verificaste que tu API Key de Claude está configurada?
- [ ] ¿Tienes conexión a Internet?
- [ ] ¿La ruta a tu bóveda es correcta?
- [ ] ¿Ejecutaste `hermes doctor` para diagnosticar?
- [ ] ¿Revisaste los logs con `hermes logs --verbose`?
- [ ] ¿Buscaste el error en Google o en el FAQ de esta guía?
- [ ] ¿Tienes la última versión de Hermes? (`pip install --upgrade hermes-agent`)
- [ ] ¿Probaste con una bóveda nueva/vacía para aislar el problema?

---

## Apéndice A: Configuración Avanzada con NAS Synology DS723+

### 🎯 ¿Por qué usar un NAS para Hermes + Obsidian?

**Ventajas:**
- ✅ **Acceso desde cualquier dispositivo** (PC, laptop, tablet)
- ✅ **Backup centralizado y automático**
- ✅ **Sincronización en tiempo real** entre dispositivos
- ✅ **Mayor espacio de almacenamiento**
- ✅ **Acceso remoto** desde cualquier lugar con Internet
- ✅ **Protección de datos** con RAID y snapshots

**Consideraciones:**
- ⚠️ Requiere conexión de red estable
- ⚠️ Rendimiento depende de la velocidad de tu red
- ⚠️ Configuración inicial más compleja

---

### PARTE 1: Configuración en el NAS Synology DS723+

#### Paso 1.1: Acceder a DSM (DiskStation Manager)

1. Abre tu navegador web
2. Ve a la dirección IP de tu NAS:
   - Ejemplo: `http://192.168.1.100:5000`
   - O usa: `http://diskstation:5000`
3. Inicia sesión con tus credenciales de administrador

#### Paso 1.2: Instalar Aplicaciones Necesarias en el NAS

**Apps que DEBES instalar desde el Package Center:**

1. **Synology Drive Server** ⭐ (MÁS IMPORTANTE)
   - Ve a `Package Center` → Busca "Synology Drive Server"
   - Haz clic en "Install"
   - Espera a que termine la instalación
   - **Para qué sirve:** Sincronización en tiempo real de archivos entre dispositivos

2. **Snapshot Replication** (Recomendado)
   - Package Center → "Snapshot Replication"
   - Instalar
   - **Para qué sirve:** Backups automáticos con versiones (como "Time Machine")

3. **Cloud Sync** (Opcional)
   - Package Center → "Cloud Sync"
   - Instalar
   - **Para qué sirve:** Backup adicional a Google Drive, Dropbox, etc.

4. **Universal Search** (Opcional)
   - Package Center → "Universal Search"
   - Instalar
   - **Para qué sirve:** Búsqueda rápida de archivos en el NAS

#### Paso 1.3: Crear Carpeta Compartida para Obsidian

1. **Abrir Control Panel**
   - En DSM, haz clic en el menú principal
   - Selecciona "Control Panel"

2. **Crear Carpeta Compartida**
   - Ve a `Shared Folder` (Carpeta Compartida)
   - Haz clic en "Create" (Crear)
   
3. **Configurar la carpeta:**
   ```
   Nombre: Obsidian-Vault
   Descripción: Bóveda de Obsidian con memoria de Hermes
   Ubicación: Volume 1 (o el volumen que uses)
   ```
   
   **Configuraciones importantes:**
   - ✅ Marca "Enable Recycle Bin" (Papelera de reciclaje)
   - ✅ Marca "Enable data checksum for advanced data integrity" (Checksums)
   - ❌ NO marques "Hide this shared folder" (queremos que sea visible)
   - ❌ NO marques "Encrypt this shared folder" (puede causar problemas de rendimiento)

4. **Configurar Permisos de Usuario**
   
   En la misma ventana, pestaña "Permissions":
   - Busca tu usuario (por ejemplo: `mgabi`)
   - Dale permisos:
     - ✅ Read (Lectura)
     - ✅ Write (Escritura)
   - Haz clic en "Apply" (Aplicar)
   - Haz clic en "OK"

#### Paso 1.4: Configurar Synology Drive Server

1. **Abrir Synology Drive Admin Console**
   - En el menú principal de DSM
   - Busca y abre "Synology Drive Admin Console"

2. **Habilitar Synology Drive**
   - En la pestaña "Overview" (Descripción general)
   - Haz clic en "Enable Synology Drive"
   
3. **Configurar Team Folder**
   - Ve a la pestaña "Team Folder"
   - Haz clic en "Create"
   - Nombre: `Obsidian-Vault`
   - Selecciona la carpeta compartida que creaste: `Obsidian-Vault`
   - Habilita "Enable versioning" (Versionado)
     - Configuración recomendada:
       - ✅ Keep all versions for: `30 days`
       - ✅ Keep versions: `Unlimited` (o al menos 100)
   - Haz clic en "Done"

4. **Dar permisos al Team Folder**
   - Selecciona el Team Folder creado
   - Haz clic en "Edit"
   - Pestaña "User permissions"
   - Tu usuario debe tener:
     - ✅ Read & Write
   - Guarda cambios

#### Paso 1.5: Configurar Snapshots (Backup Automático)

1. **Abrir Snapshot Replication**
   - Menú principal → "Snapshot Replication"

2. **Crear Snapshot Schedule**
   - Pestaña "Snapshot" → "Shared Folder"
   - Selecciona `Obsidian-Vault`
   - Haz clic en "Settings" (Configuración)
   - Haz clic en "Schedule" → "Create"
   
3. **Configurar frecuencia de snapshots:**
   ```
   Frecuencia: Daily (Diaria)
   Hora: 2:00 AM (cuando no estés trabajando)
   Retención:
     - Keep snapshots for: 30 days
     - Keep 24 hourly snapshots
     - Keep 7 daily snapshots
     - Keep 4 weekly snapshots
   ```
   
4. **Guardar configuración**
   - Haz clic en "OK"
   - Los snapshots se crearán automáticamente

#### Paso 1.6: Configurar Acceso Remoto (Opcional pero recomendado)

1. **Configurar QuickConnect (la forma más fácil)**
   - Control Panel → "QuickConnect"
   - Sigue el asistente para crear tu ID de QuickConnect
   - Ejemplo: `mgabi-nas` (será tu dirección: `mgabi-nas.quickconnect.to`)

2. **O configurar Port Forwarding (más avanzado)**
   - En tu router, abre los puertos:
     - Puerto 5000 (HTTP)
     - Puerto 5001 (HTTPS)
     - Puerto 6690 (Synology Drive)
   - Apunta al IP del NAS (ej: `192.168.1.100`)

#### Paso 1.7: Habilitar SMB/CIFS para Windows

1. **Control Panel → File Services**
2. Pestaña "SMB/AFP/NFS"
3. **Configuración SMB:**
   ```
   ✅ Enable SMB service
   Maximum SMB protocol: SMB3
   Minimum SMB protocol: SMB2
   ✅ Enable opportunistic locking
   ✅ Enable SMB 2 leases (recomendado para mejor rendimiento)
   ```
4. Haz clic en "Apply"

---

### PARTE 2: Configuración en Windows

#### Paso 2.1: Instalar Synology Drive Client en Windows

1. **Descargar Synology Drive Client**
   - Ve a: https://www.synology.com/es-mx/support/download/DS723+
   - En "Desktop Utilities" → Descarga "Synology Drive Client"
   - Descarga la versión para Windows

2. **Instalar Synology Drive Client**
   - Ejecuta el instalador descargado
   - Sigue el asistente de instalación
   - Marca:
     - ✅ Synology Drive (sincronización de archivos)
     - ✅ Sync Task (para crear tareas de sincronización)

3. **Configurar Synology Drive Client**
   
   Al abrir por primera vez:
   - **Server Address:** `192.168.1.100:5001` (o tu IP del NAS)
     - O usa QuickConnect: `mgabi-nas.quickconnect.to`
   - **Username:** Tu usuario del NAS (ej: `mgabi`)
   - **Password:** Tu contraseña del NAS
   - Haz clic en "Sign In"

4. **Configurar Tarea de Sincronización**
   
   Después de iniciar sesión:
   - Modo de sincronización:
     - Selecciona: **"Sync with Synology Drive"** (Sincronizar con Synology Drive)
   
   - **Remote folder** (Carpeta remota en el NAS):
     - Selecciona: `Obsidian-Vault`
   
   - **Local folder** (Carpeta local en tu PC):
     - **IMPORTANTE:** Usa una ruta fácil de recordar:
     - Recomendado: `C:\Synology\Obsidian-Vault`
     - Crea la carpeta si no existe
   
   - **Opciones de sincronización:**
     - Modo: **Two-way sync** (Sincronización bidireccional)
     - ✅ "Sync files on demand" (Sincronización bajo demanda - ahorra espacio)
     - ✅ "Enable file versioning" (Versionado de archivos)
   
   - Haz clic en "Done"

5. **Verificar que está sincronizando**
   - En la bandeja del sistema (system tray), verás el ícono de Synology Drive
   - Haz clic derecho → "Recent Changes" para ver la actividad
   - Debería mostrar "Syncing..." inicialmente

#### Paso 2.2: Mapear el NAS como Unidad de Red (Alternativa a Synology Drive)

**Si prefieres acceso directo sin sincronización local:**

1. **Abrir Explorador de Archivos**
   - Presiona `Win + E`

2. **Mapear Unidad de Red**
   - Haz clic derecho en "This PC" (Este equipo)
   - Selecciona "Map network drive" (Conectar a unidad de red)

3. **Configurar la unidad:**
   ```
   Drive letter: Z: (o la letra que prefieras)
   Folder: \\192.168.1.100\Obsidian-Vault
   (Reemplaza 192.168.1.100 con la IP de tu NAS)
   
   ✅ Reconnect at sign-in (Reconectar al iniciar sesión)
   ✅ Connect using different credentials (si tu usuario de Windows es diferente)
   ```

4. **Ingresar credenciales**
   - Username: `NOMBRE_DEL_NAS\usuario`
     - Ejemplo: `DS723\mgabi`
   - Password: Tu contraseña del NAS
   - ✅ Marca "Remember my credentials"
   - Haz clic en "OK"

5. **Verificar**
   - Ahora deberías ver la unidad `Z:` en "This PC"
   - Ábrela para verificar que puedes ver archivos

---

### PARTE 3: Configurar Obsidian para usar el NAS

#### Opción A: Usando Synology Drive Client (Recomendado)

1. **Espera a que Synology Drive termine la sincronización inicial**
   - Verás un check verde en el ícono de Synology Drive

2. **Abrir Obsidian**
   - Inicia Obsidian
   - "Create new vault" o "Open folder as vault"

3. **Seleccionar la carpeta sincronizada:**
   - Navega a: `C:\Synology\Obsidian-Vault`
   - Crea una subcarpeta: `Mi-Segundo-Cerebro`
   - Selecciónala como tu bóveda

4. **Verificar sincronización**
   - Crea una nota de prueba en Obsidian
   - Verifica en DSM (interfaz web del NAS) que el archivo aparece
   - Camino en NAS: `Obsidian-Vault/Mi-Segundo-Cerebro/`

**✅ Ventajas de este método:**
- Funciona offline (tienes copia local)
- Sincronización automática en segundo plano
- Rendimiento rápido (trabajas en archivos locales)

#### Opción B: Usando Unidad Mapeada (Acceso directo)

1. **Abrir Obsidian**
   - "Open folder as vault"

2. **Seleccionar la unidad mapeada:**
   - Navega a: `Z:\Mi-Segundo-Cerebro`
   - Selecciónala como bóveda

**⚠️ Consideraciones:**
- Requiere conexión de red constante
- Puede ser más lento
- No funciona offline

---

### PARTE 4: Configurar Hermes para usar el NAS

#### Si usas Synology Drive (Opción A - Recomendado):

```powershell
hermes memory setup --provider obsidian --path "C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro"
```

#### Si usas Unidad Mapeada (Opción B):

```powershell
hermes memory setup --provider obsidian --path "Z:\Mi-Segundo-Cerebro"
```

#### Verificar configuración:

```powershell
hermes memory status
```

Deberías ver:
```
Memory Provider: obsidian
Memory Path: C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro
Status: Connected ✓
```

#### Configurar archivo .env de Hermes:

Edita: `C:\Users\mgabi\.hermes\.env`

```env
# API de Claude
ANTHROPIC_API_KEY=tu-clave-api-aqui
MODEL_PROVIDER=anthropic
MODEL_NAME=claude-sonnet-4-8

# Memoria Obsidian en NAS (vía Synology Drive)
MEMORY_BACKEND=obsidian
MEMORY_PATH=C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro

# O si usas unidad mapeada:
# MEMORY_PATH=Z:\Mi-Segundo-Cerebro

# Servidor API
API_SERVER_ENABLED=true
API_SERVER_PORT=8642
```

---

### PARTE 5: Configuración Multi-Dispositivo (Windows + Mac)

> 🎯 **ESCENARIO IMPORTANTE:** Esta sección es para ti si quieres trabajar desde tu PC Windows Y tu Mac, compartiendo el mismo Hermes y Obsidian, con sincronización en tiempo real entre ambos dispositivos.

#### Cómo Funciona la Sincronización entre Dispositivos

**El flujo es así:**

```
Windows PC                    NAS (DS723+)                    Mac
    |                              |                             |
    |  1. Creas nota en Obsidian  |                             |
    |----------------------------->|                             |
    |                              |                             |
    |                              | 2. NAS guarda el archivo    |
    |                              |                             |
    |                              | 3. Synology Drive detecta   |
    |                              |    el cambio                |
    |                              |                             |
    |                              |----------------------------->|
    |                              | 4. Sincroniza a Mac         |
    |                              |                             |
    |                              |    5. Obsidian en Mac       |
    |                              |       ve el archivo nuevo   |
```

**Tiempo de sincronización:** Normalmente 1-5 segundos entre dispositivos.

---

#### Paso 5.1: Configuración Inicial en Windows (Primera PC)

**Ya lo hiciste en la PARTE 2**, pero repasemos lo importante:

1. ✅ Synology Drive Client instalado
2. ✅ Carpeta de sincronización: `C:\Synology\Obsidian-Vault`
3. ✅ Obsidian apuntando a: `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro`
4. ✅ Hermes configurado con: `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro`

---

#### Paso 5.2: Configuración en Mac (Segunda PC)

**💻 En tu Mac, sigue estos pasos:**

##### 5.2.1: Instalar Synology Drive Client en Mac

1. **Descargar Synology Drive Client para Mac**
   - Ve a: https://www.synology.com/es-mx/support/download/DS723+
   - Sección "Desktop Utilities"
   - Descarga "Synology Drive Client for Mac"
   - Descarga el archivo `.dmg`

2. **Instalar**
   - Abre el archivo `.dmg` descargado
   - Arrastra "Synology Drive" a la carpeta Applications
   - Abre Synology Drive desde Launchpad o Applications

3. **Configurar Synology Drive en Mac**
   
   Al abrir por primera vez:
   - **Server Address:** `192.168.1.100:5001` (la IP de tu NAS)
     - O usa tu QuickConnect: `mgabi-nas.quickconnect.to`
   - **Username:** `mgabi` (tu usuario del NAS)
   - **Password:** Tu contraseña del NAS
   - Haz clic en "Sign In"

4. **Configurar Tarea de Sincronización en Mac**
   
   **⚠️ MUY IMPORTANTE:** Usa EXACTAMENTE la misma estructura que en Windows:
   
   - **Modo:** "Sync with Synology Drive"
   - **Remote folder:** `Obsidian-Vault` (¡Exactamente el mismo que en Windows!)
   - **Local folder:** `/Users/mgabi/Synology/Obsidian-Vault`
     - Crea esta carpeta si no existe
     - **Importante:** Usa tu nombre de usuario de Mac real
   - **Sync mode:** Two-way sync
   - ✅ "Enable file versioning"
   - ✅ "Sync files on demand" (opcional, ahorra espacio)
   - Haz clic en "Done"

5. **Esperar a que termine la sincronización inicial**
   - Verás un ícono de Synology Drive en la barra de menú (arriba a la derecha)
   - Haz clic en él para ver el progreso
   - Espera hasta que veas el check verde ✅
   - **Esto puede tomar varios minutos la primera vez**, dependiendo de cuántos archivos ya tienes

##### 5.2.2: Instalar Python en Mac

1. **Verificar si ya tienes Python**
   ```bash
   python3 --version
   ```

2. **Si no lo tienes, instalar con Homebrew (recomendado)**
   
   Primero instala Homebrew si no lo tienes:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   
   Luego instala Python:
   ```bash
   brew install python@3.12
   ```

3. **Verificar instalación**
   ```bash
   python3 --version
   pip3 --version
   ```

##### 5.2.3: Instalar Hermes Agent en Mac

```bash
pip3 install hermes-agent
```

##### 5.2.4: Configurar Hermes en Mac

1. **Ejecutar setup de Hermes**
   ```bash
   hermes setup
   ```
   
   Responde las preguntas:
   - Nombre: Tu nombre
   - AI provider: `anthropic` (Claude)
   - Enable API server: `yes`
   - Port: `8642` (default)

2. **Configurar la API Key de Claude en Mac**
   
   ```bash
   export ANTHROPIC_API_KEY="tu-clave-api-aqui"
   echo 'export ANTHROPIC_API_KEY="tu-clave-api-aqui"' >> ~/.zshrc
   ```
   
   **Usa LA MISMA API Key que en Windows** (la misma cuenta de Anthropic)

3. **Configurar Hermes para usar la bóveda del NAS**
   
   ```bash
   hermes memory setup --provider obsidian --path "/Users/mgabi/Synology/Obsidian-Vault/Mi-Segundo-Cerebro"
   ```
   
   **⚠️ IMPORTANTE:** Reemplaza `mgabi` con tu nombre de usuario real de Mac

4. **Verificar configuración**
   ```bash
   hermes memory status
   ```
   
   Deberías ver:
   ```
   Memory Provider: obsidian
   Memory Path: /Users/mgabi/Synology/Obsidian-Vault/Mi-Segundo-Cerebro
   Status: Connected ✓
   ```

5. **Editar archivo .env de Hermes en Mac**
   
   Ubicación: `~/.hermes/.env`
   
   ```bash
   nano ~/.hermes/.env
   ```
   
   Contenido:
   ```env
   # API de Claude (LA MISMA que en Windows)
   ANTHROPIC_API_KEY=tu-clave-api-aqui
   MODEL_PROVIDER=anthropic
   MODEL_NAME=claude-sonnet-4-8
   
   # Memoria Obsidian en NAS (vía Synology Drive)
   MEMORY_BACKEND=obsidian
   MEMORY_PATH=/Users/mgabi/Synology/Obsidian-Vault/Mi-Segundo-Cerebro
   
   # Servidor API
   API_SERVER_ENABLED=true
   API_SERVER_PORT=8642
   ```

##### 5.2.5: Instalar Obsidian en Mac

1. **Descargar Obsidian para Mac**
   - Ve a: https://obsidian.md
   - Descarga la versión para macOS
   - Descarga el archivo `.dmg`

2. **Instalar**
   - Abre el `.dmg`
   - Arrastra Obsidian a Applications
   - Abre Obsidian

3. **Abrir la bóveda sincronizada**
   - En Obsidian, haz clic en "Open folder as vault"
   - Navega a: `/Users/mgabi/Synology/Obsidian-Vault/Mi-Segundo-Cerebro`
   - Selecciónala
   - ¡Deberías ver TODAS las notas que creaste en Windows!

---

#### Paso 5.3: Verificación de Sincronización en Tiempo Real

**Prueba que todo funciona correctamente:**

##### Test 1: De Windows a Mac

1. **En Windows:**
   - Abre Obsidian
   - Crea una nota nueva: "Test-Windows-to-Mac.md"
   - Escribe algo: "Esta nota se creó en Windows"
   - Guarda (Ctrl+S)

2. **Espera 3-5 segundos**

3. **En Mac:**
   - Abre Obsidian (o refresca si ya estaba abierto: Cmd+R)
   - ¡Deberías ver la nota "Test-Windows-to-Mac.md"!
   - Ábrela y verifica que tiene el contenido

##### Test 2: De Mac a Windows

1. **En Mac:**
   - En Obsidian, crea una nota: "Test-Mac-to-Windows.md"
   - Escribe: "Esta nota se creó en Mac"
   - Guarda (Cmd+S)

2. **Espera 3-5 segundos**

3. **En Windows:**
   - Refresca Obsidian (Ctrl+R)
   - ¡Deberías ver "Test-Mac-to-Windows.md"!

##### Test 3: Hermes puede leer desde ambos

**En Windows:**
```powershell
hermes
```
```
Hola Hermes, lee mis notas y dime cuáles vienen de Windows y cuáles de Mac.
```

**En Mac:**
```bash
hermes
```
```
Hermes, por favor lista todas las notas que hay en mi bóveda.
```

**Deberías ver las mismas notas en ambos dispositivos.**

##### Test 4: Hermes puede escribir desde ambos

**En Windows, pídele a Hermes:**
```
Crea una nota llamada "Creada-por-Hermes-Windows" con el contenido "Hermes creando desde Windows".
```

**En Mac, verifica que aparece:**
- Refresca Obsidian
- La nota debería estar ahí

**En Mac, pídele a Hermes:**
```
Crea una nota llamada "Creada-por-Hermes-Mac" con el contenido "Hermes creando desde Mac".
```

**En Windows, verifica que aparece.**

---

#### Paso 5.4: Reglas de Oro para Trabajar con Múltiples Dispositivos

🚨 **¡MUY IMPORTANTE para evitar problemas!**

##### Regla 1: NO edites el mismo archivo simultáneamente

**❌ MAL:**
- 10:00 AM - Abres "Proyecto.md" en Windows
- 10:05 AM - Abres "Proyecto.md" en Mac
- Editas en ambos al mismo tiempo
- **RESULTADO:** Conflicto de archivo

**✅ BIEN:**
- 10:00 AM - Abres "Proyecto.md" en Windows
- Editas y guardas
- Cierras el archivo
- Esperas 5 segundos a que sincronice
- 10:10 AM - Abres "Proyecto.md" en Mac (ahora tiene los cambios de Windows)

##### Regla 2: Verifica que Synology Drive esté sincronizado antes de cambiar de dispositivo

**Antes de cerrar tu sesión en Windows:**
1. Mira el ícono de Synology Drive (bandeja del sistema)
2. Debe mostrar check verde ✅
3. Si está sincronizando, espera a que termine

**Antes de empezar a trabajar en Mac:**
1. Mira el ícono de Synology Drive (barra de menú)
2. Debe mostrar check verde ✅
3. Refresca Obsidian (Cmd+R)

##### Regla 3: Cierra Obsidian cuando no lo uses

**¿Por qué?**
- Obsidian mantiene archivos "abiertos" en memoria
- Si dejas Obsidian abierto en Windows todo el día
- Y luego trabajas en Mac
- Puede haber conflictos de cache

**Mejor práctica:**
- Terminas de trabajar en Windows → Cierra Obsidian
- Vas a trabajar en Mac → Abre Obsidian en Mac

##### Regla 4: Hermes puede correr en ambos simultáneamente (pero no es necesario)

**Puedes tener:**
- Hermes corriendo en Windows
- Hermes corriendo en Mac
- Al mismo tiempo

**Ambos compartirán:**
- ✅ La misma bóveda
- ✅ La misma API Key de Claude
- ✅ Las mismas notas

**Pero tendrán separados:**
- ❌ Historial de conversaciones
- ❌ Configuraciones específicas de cada máquina

**Recomendación:** Trabaja con Hermes en UN dispositivo a la vez.

---

#### Paso 5.5: Flujo de Trabajo Recomendado

##### Escenario 1: Trabajas principalmente en Windows, ocasionalmente en Mac

**En casa (Windows - PC principal):**
1. Trabajas normalmente con Obsidian + Hermes
2. Creas notas, proyectos, etc.
3. Todo se sincroniza automáticamente al NAS

**Cuando sales (Mac - Laptop):**
1. Abres Mac
2. Esperas a que Synology Drive sincronice (check verde)
3. Abres Obsidian → Tienes todo lo de Windows
4. Puedes:
   - Ver notas
   - Editar notas
   - Crear notas nuevas
5. Al guardar, se sincroniza de vuelta al NAS
6. Cuando vuelvas a Windows, tendrás los cambios del Mac

##### Escenario 2: Alternas entre Windows y Mac frecuentemente

**Por la mañana (Windows):**
```
08:00 - Enciendes Windows
08:02 - Synology Drive sincroniza (check verde)
08:03 - Abres Obsidian
08:05 - Trabajas en tus proyectos
12:00 - IMPORTANTE: Guardas todo y cierras Obsidian
12:01 - Verificas check verde en Synology Drive
```

**Por la tarde (Mac):**
```
14:00 - Enciendes Mac
14:02 - Synology Drive sincroniza (check verde)
14:03 - Abres Obsidian → Ves cambios de la mañana
14:05 - Continúas trabajando
18:00 - Guardas y cierras
18:01 - Check verde en Synology Drive
```

**Al día siguiente (Windows):**
```
08:00 - Abres Windows
08:02 - Synology Drive trae cambios de ayer (Mac)
08:03 - Abres Obsidian → Todo actualizado
```

##### Escenario 3: Trabajas en equipo (tú + otra persona)

**Si quieres que otra persona también acceda:**

1. **Crear usuario en el NAS**
   - DSM → Control Panel → User & Group
   - Create user: `colaborador`
   - Darle permisos a `Obsidian-Vault`

2. **El colaborador instala:**
   - Synology Drive Client
   - Se conecta con su usuario
   - Sincroniza la misma carpeta

3. **Reglas de coordinación:**
   - 💬 Comunícanse antes de editar archivos compartidos
   - 📅 Usen un calendario compartido o Slack
   - 📝 Mejor práctica: Cada persona tiene sus propias subcarpetas

---

#### Paso 5.6: Qué hacer si aparecen conflictos

**Si ves archivos como:**
```
Nota.md
Nota (Conflicted Copy 2026-08-02 from DESKTOP-WINDOWS).md
Nota (Conflicted Copy 2026-08-02 from MacBook).md
```

**Significa:** Editaste el mismo archivo en ambos dispositivos sin esperar a que sincronice.

**Solución:**

1. **Abre ambos archivos lado a lado en Obsidian**

2. **Pídele a Hermes que los fusione:**
   ```
   Hermes, tengo estos archivos en conflicto:
   - Nota.md
   - Nota (Conflicted Copy 2026-08-02 from DESKTOP-WINDOWS).md
   - Nota (Conflicted Copy 2026-08-02 from MacBook).md
   
   Por favor:
   1. Compáralos
   2. Identifica qué es diferente en cada uno
   3. Fusiona el contenido manteniendo TODO lo importante
   4. Crea un archivo final con el mejor contenido de todos
   5. Guárdalo como "Nota.md"
   ```

3. **Elimina los archivos de conflicto**
   - Una vez que Hermes haya fusionado
   - Elimina las versiones "Conflicted Copy"

4. **Prevención futura:**
   - Sigue la Regla 1: No edites simultáneamente
   - Espera a que sincronice antes de cambiar de dispositivo

---

#### Paso 5.7: Configuración de Respaldo (Solo Offline)

**¿Qué pasa si no tienes Internet y necesitas trabajar offline?**

**Con Synology Drive (Opción A - Recomendada):**
- ✅ **FUNCIONA OFFLINE**
- Tienes copia local completa
- Puedes trabajar normalmente
- Cuando vuelva Internet, todo se sincroniza automáticamente

**Con Unidad Mapeada (Opción B):**
- ❌ **NO FUNCIONA OFFLINE**
- Necesitas conexión al NAS todo el tiempo
- Si pierdes conexión, no puedes acceder a los archivos

**Por eso recomendamos Synology Drive.**

---

#### Resumen de Configuración Multi-Dispositivo

| Aspecto | Windows | Mac |
|---------|---------|-----|
| **Synology Drive** | `C:\Synology\Obsidian-Vault` | `/Users/mgabi/Synology/Obsidian-Vault` |
| **Bóveda Obsidian** | `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro` | `/Users/mgabi/Synology/Obsidian-Vault/Mi-Segundo-Cerebro` |
| **Hermes config** | Igual que bóveda Obsidian | Igual que bóveda Obsidian |
| **API Key Claude** | La misma en ambos | La misma en ambos |
| **Archivo .env** | `C:\Users\mgabi\.hermes\.env` | `~/.hermes/.env` |
| **Sincronización** | Automática en tiempo real | Automática en tiempo real |
| **Offline** | ✅ Funciona | ✅ Funciona |

**✅ Con esta configuración:**
- Trabajas en Windows → Se sincroniza a Mac automáticamente
- Trabajas en Mac → Se sincroniza a Windows automáticamente
- Hermes en Windows y Mac comparten la misma memoria
- Obsidian en Windows y Mac muestran las mismas notas
- Todo en tiempo real (1-5 segundos de delay)

🎉 **¡Tienes un verdadero sistema unificado entre tus dos computadoras!**

---

### PARTE 6: Acceso desde Otros Dispositivos Adicionales

#### En otra computadora Windows:

1. Instala Synology Drive Client
2. Inicia sesión con las mismas credenciales
3. Configura la misma carpeta de sincronización
4. Instala Obsidian y Hermes
5. Configura con la misma ruta local: `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro`

#### En dispositivos móviles (iOS/Android):

1. **Instala Obsidian Mobile** (de la App Store o Google Play)
2. **Instala Synology Drive Mobile**
3. **Configura Synology Drive Mobile:**
   - Inicia sesión en tu NAS
   - Habilita sincronización de `Obsidian-Vault`
4. **En Obsidian Mobile:**
   - "Open folder as vault"
   - Selecciona la carpeta sincronizada
   - iOS: `On My iPhone/Synology Drive/Obsidian-Vault/Mi-Segundo-Cerebro`
   - Android: `Internal Storage/Synology Drive/Obsidian-Vault/Mi-Segundo-Cerebro`

**Nota:** Hermes no funciona directamente en móviles, pero puedes usar Telegram + Hermes en tu computadora para enviar comandos desde el móvil.

---

### PARTE 6: Optimizaciones y Mejores Prácticas

#### 6.1: Optimizar Rendimiento de Red

**En el NAS (DSM):**
1. Control Panel → Network → Network Interface
2. Asegúrate de tener configurado:
   - Speed: `Auto` o `1000 Mbps Full Duplex` (Gigabit)
   - MTU: `1500` (default) o `9000` (Jumbo Frames si tu red lo soporta)

**En Windows:**
1. Asegúrate de estar conectado a la misma red que el NAS
2. Preferiblemente usa cable Ethernet (no WiFi) para mejor rendimiento

#### 6.2: Habilitar Indexación de Archivos en el NAS

1. **Control Panel → Indexing Service**
2. Habilitar indexación para `Obsidian-Vault`
3. Esto mejora la velocidad de búsqueda

#### 6.3: Configurar Cache en Hermes

Edita `C:\Users\mgabi\.hermes\config.yaml`:

```yaml
memory:
  cache_enabled: true
  cache_size_mb: 1024  # Aumenta el cache para compensar acceso de red
  cache_ttl_seconds: 3600  # Mantén cache por 1 hora
  
  # Configuraciones específicas para NAS
  network_timeout: 30  # Aumenta timeout para red
  retry_attempts: 3
  batch_operations: true  # Agrupa operaciones para eficiencia
```

#### 6.4: Programar Backups Adicionales

**Backup del NAS a la Nube (recomendado):**

1. **Abrir Cloud Sync** (en DSM)
2. **Crear nueva tarea:**
   - Servicio: Google Drive / Dropbox / OneDrive (tu preferencia)
   - Carpeta local: `Obsidian-Vault`
   - Modo: `Upload local changes only` (Solo subir cambios locales)
   - Programación: Diaria, 3:00 AM

**Backup a USB externo:**

1. **Conecta disco USB al NAS**
2. **Control Panel → External Devices**
3. **Hyper Backup**
   - Crear tarea de backup
   - Origen: `Obsidian-Vault`
   - Destino: Disco USB
   - Frecuencia: Semanal

---

### PARTE 7: Troubleshooting Específico del NAS

#### Problema: "No se puede conectar al NAS"

**Verificaciones:**

1. **Ping al NAS**
   ```powershell
   ping 192.168.1.100
   ```
   Deberías recibir respuestas

2. **Verificar que el NAS está encendido**
   - Luces LED frontales encendidas
   - Pitido de inicio completado

3. **Verificar que estás en la misma red**
   ```powershell
   ipconfig
   ```
   Tu IP debe estar en el mismo rango (ej: `192.168.1.x`)

4. **Verificar firewall de Windows**
   - Windows Security → Firewall & network protection
   - Permite "File and Printer Sharing"

#### Problema: "Synology Drive no sincroniza"

**Soluciones:**

1. **Verificar estado del servicio**
   - Click derecho en ícono Synology Drive
   - "Settings" → "About"
   - Debe decir "Connected"

2. **Reiniciar sincronización**
   - Settings → "Advanced"
   - "Clear local data and re-sync"

3. **Verificar permisos en el NAS**
   - DSM → Synology Drive Admin Console
   - Team Folder → `Obsidian-Vault`
   - Verifica que tu usuario tiene Read & Write

#### Problema: "Obsidian muy lento en el NAS"

**Causas comunes:**
- Conexión WiFi lenta → Usa cable Ethernet
- Muchos archivos en la bóveda → Usa indexación
- Cache de Hermes pequeño → Aumenta cache

**Solución:**

1. **Usa Synology Drive con "Sync files on demand"**
   - Solo descarga archivos cuando los necesitas
   - Resto se mantiene en el NAS

2. **Aumenta cache de Obsidian**
   - Obsidian Settings → Files & Links
   - "Deleted files" → Reduce días de retención

3. **Reduce plugins de Obsidian**
   - Menos plugins = mejor rendimiento

#### Problema: "Conflictos de archivos"

**Prevención:**

1. **No edites el mismo archivo desde dos dispositivos simultáneamente**
2. **Espera a que Synology Drive sincronice antes de cambiar de dispositivo**
   - Verifica check verde en ícono

**Resolución:**

Si aparecen conflictos:
```
Nota.md
Nota (Conflicted Copy 2026-08-02).md
```

Pídele a Hermes que los fusione:
```
Hermes, tengo estos archivos en conflicto:
- Nota.md
- Nota (Conflicted Copy 2026-08-02).md

Por favor compáralos y fusiona manteniendo la información más actualizada.
```

#### Problema: "Acceso remoto no funciona"

**Verificar QuickConnect:**

1. DSM → Control Panel → QuickConnect
2. Estado debe ser "Connected"
3. Prueba acceder desde: `https://tu-quickconnect-id.quickconnect.to`

**Verificar Port Forwarding (si no usas QuickConnect):**

1. Router → Port Forwarding
2. Verifica que los puertos están abiertos:
   - 5000 → 192.168.1.100:5000
   - 5001 → 192.168.1.100:5001
   - 6690 → 192.168.1.100:6690

---

### PARTE 8: Monitoreo y Mantenimiento

#### Dashboard de Monitoreo en DSM

1. **Resource Monitor** (Monitor de Recursos)
   - Menú principal → "Resource Monitor"
   - Verifica:
     - CPU: No debe estar constantemente a 100%
     - RAM: Idealmente < 80% de uso
     - Network: Tráfico normal de sincronización
     - Disk: Verifica salud de los discos

2. **Storage Manager**
   - Menú principal → "Storage Manager"
   - Pestaña "HDD/SSD"
   - Verifica estado de salud: "Healthy"
   - Si aparece "Warning" → Considera reemplazar disco

#### Mantenimiento Programado

**Mensual:**
- Revisa snapshots: Snapshot Replication → Verifica que se están creando
- Verifica espacio disponible: Storage Manager → Al menos 20% libre
- Revisa logs de sistema: Log Center → Busca errores

**Trimestral:**
- Actualiza DSM: Control Panel → Update & Restore → Check for updates
- Actualiza paquetes: Package Center → Update all
- Prueba restaurar un snapshot (para verificar que funciona)

**Anual:**
- Verifica salud de discos (S.M.A.R.T. test)
- Considera expansión de almacenamiento si estás >70% lleno
- Revisa configuración de seguridad

#### Alertas por Email

1. **Control Panel → Notification**
2. **Email**
   - Configura servidor SMTP (Gmail, Outlook, etc.)
   - Email de destino: tu correo personal

3. **Rules**
   - ✅ "Storage space is running out"
   - ✅ "Volume crashed"
   - ✅ "Connection failure"
   - ✅ "Bad sector detected"

---

### PARTE 9: Checklist Final de Configuración con NAS

**En el NAS (Synology DS723+):**
- [ ] Carpeta compartida `Obsidian-Vault` creada
- [ ] Synology Drive Server instalado y configurado
- [ ] Team Folder de Synology Drive creado
- [ ] Permisos de usuario configurados (Read & Write)
- [ ] Snapshots programados (diarios)
- [ ] SMB/CIFS habilitado
- [ ] (Opcional) QuickConnect configurado
- [ ] (Opcional) Cloud Sync para backup externo

**En Windows:**
- [ ] Synology Drive Client instalado
- [ ] Tarea de sincronización configurada
- [ ] Carpeta local: `C:\Synology\Obsidian-Vault`
- [ ] Sincronización activa (check verde)
- [ ] (Opcional) Unidad de red mapeada (Z:)

**En Obsidian:**
- [ ] Bóveda apuntando a carpeta sincronizada
- [ ] Puede crear y editar notas
- [ ] Cambios se sincronizan al NAS

**En Hermes:**
- [ ] `hermes memory setup` ejecutado con ruta del NAS
- [ ] `hermes memory status` muestra "Connected"
- [ ] Archivo `.env` configurado correctamente
- [ ] Hermes puede leer notas de la bóveda
- [ ] Hermes puede escribir notas nuevas

**Verificación Final:**
- [ ] Crea una nota de prueba en Obsidian
- [ ] Verifica que aparece en DSM (interfaz web del NAS)
- [ ] Pídele a Hermes que lea esa nota
- [ ] Pídele a Hermes que cree una nota nueva
- [ ] Verifica que la nota de Hermes aparece en Obsidian
- [ ] (Si tienes otro dispositivo) Verifica que se sincroniza

---

### Resumen de Rutas

**Para configuraciones con Synology Drive (Recomendado):**

| Ubicación | Ruta |
|-----------|------|
| NAS (real storage) | `/volume1/Obsidian-Vault/Mi-Segundo-Cerebro` |
| Windows (sincronizado) | `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro` |
| Mac (sincronizado) | `/Users/TU_USUARIO/Synology/Obsidian-Vault/Mi-Segundo-Cerebro` |
| Hermes config (Windows) | `C:\Synology\Obsidian-Vault\Mi-Segundo-Cerebro` |
| Hermes config (Mac) | `/Users/TU_USUARIO/Synology/Obsidian-Vault/Mi-Segundo-Cerebro` |

**Para configuraciones con Unidad Mapeada:**

| Ubicación | Ruta |
|-----------|------|
| NAS | `/volume1/Obsidian-Vault/Mi-Segundo-Cerebro` |
| Windows | `Z:\Mi-Segundo-Cerebro` |
| Hermes config | `Z:\Mi-Segundo-Cerebro` |


### Lo que has logrado:

1. ✅ Obsidian instalado y configurado con estructura de carpetas
2. ✅ Python y Hermes Agent funcionando
3. ✅ Claude API conectado y verificado
4. ✅ Integración completa entre las tres herramientas
5. ✅ Archivo CLAUDE.md personalizado
6. ✅ Proyectos organizados (HomeLab y Hermes-Obsidian)
7. ✅ Sistema probado y funcionando

### Próximos pasos recomendados:

1. **Esta semana:**
   - Usa Hermes diariamente para capturar ideas
   - Documenta al menos un proyecto completo
   - Experimenta con diferentes tipos de prompts

2. **Este mes:**
   - Crea plantillas para tus notas más frecuentes
   - Configura al menos una tarea automatizada
   - Explora plugins de Obsidian que complementen tu workflow

3. **Este trimestre:**
   - Evalúa qué funciona y qué no en tu sistema
   - Ajusta la estructura de tu bóveda según necesites
   - Considera compartir tus aprendizajes con la comunidad

### Recuerda:

> "El mejor sistema es el que realmente usas."

No te preocupes por tener el sistema "perfecto" desde el día 1. Úsalo, aprende, ajusta, mejora. Con el tiempo, este sistema se convertirá en una extensión natural de tu pensamiento.

---

**¿Preguntas? ¿Problemas? ¿Mejoras a esta guía?**

Este documento está vivo y puede mejorar. Si encuentras errores, tienes sugerencias o quieres compartir tu experiencia, documenta todo en tu bóveda - ¡es para eso que la tienes!

**Última actualización:** 2026-08-01
**Versión de la guía:** 1.0
**Autor:** Creado con Hermes + Claude para Gabriel

---

¡Que disfrutes tu nuevo segundo cerebro! 🧠✨
