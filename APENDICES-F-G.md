# Apéndices Adicionales - Workflows e Integraciones

## Apéndice F: Workflows Avanzados con Hermes

### 🤖 Automatización y Tareas Programadas

#### 1. Procesamiento Automático del Inbox

**Script de procesamiento diario (PowerShell):**

```powershell
# Script: process-inbox.ps1
# Procesa automáticamente las notas del inbox cada noche

# Ubicación de tu bóveda en el NAS
$vaultPath = "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro"
$inboxPath = "$vaultPath\00-Inbox"

# Cambiar al directorio
cd $vaultPath

# Llamar a Hermes para procesar inbox
hermes process inbox --organize --tag --link

# Log del resultado
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -Path "$vaultPath\Logs\inbox-processing.log" -Value "$timestamp - Inbox procesado"
```

**Programar con Task Scheduler:**
1. Task Scheduler → Create Task
2. Name: "Procesar Inbox Obsidian"
3. Trigger: Daily at 11:00 PM
4. Action: `C:\Scripts\process-inbox.ps1`
5. Conditions: Solo si PC está encendida

**Para Mac (cron):**

```bash
# Editar crontab
crontab -e

# Agregar línea (cada día a las 11 PM)
0 23 * * * /Users/mgabi/Scripts/process-inbox.sh

# Script: process-inbox.sh
#!/bin/bash
cd "/Volumes/Obsidian-Vault/Mi-Segundo-Cerebro"
hermes process inbox --organize --tag --link
echo "$(date): Inbox procesado" >> Logs/inbox-processing.log
```

---

#### 2. Resumen Semanal Automático

**Generar reporte cada domingo:**

```powershell
# Script: weekly-review.ps1

$vaultPath = "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro"
$date = Get-Date -Format "yyyy-MM-dd"
$weekNumber = Get-Date -UFormat %V

# Generar resumen semanal
hermes generate weekly-review `
    --week $weekNumber `
    --output "$vaultPath\02-Areas\Revisiones\Semana-$weekNumber-$date.md"
```

**Contenido del resumen generado:**

```markdown
# Revisión Semanal - Semana 31 (2026-08-02)

## 📊 Resumen de la Semana

**Productividad General:** ⭐⭐⭐⭐☆

### Estadísticas
- **Notas creadas:** 23
- **Tareas completadas:** 47
- **Proyectos activos:** 3
- **Horas invertidas:** ~28h

## 🎯 Proyectos Actualizados

### HomeLab
- **Estado:** En progreso (60%)
- **Actualizaciones:** 5 notas nuevas
- **Próximo hito:** Configurar Proxmox

### Hermes-Obsidian
- **Estado:** En progreso (80%)
- **Actualizaciones:** Documentación completa
- **Próximo hito:** Pruebas finales

## ✅ Logros de la Semana

1. ✓ Configurado NAS Synology
2. ✓ Sincronizado Obsidian entre PC y Mac
3. ✓ Creadas 4 plantillas nuevas
4. ✓ Organizado inbox completo

## 🔜 Prioridades Próxima Semana

- [ ] Finalizar configuración Hermes
- [ ] Comenzar proyecto Python
- [ ] Review de sistema de tags

## 💡 Aprendizajes

[Generado automáticamente desde notas con tag #aprendizaje]

## 📈 Tendencias

**Temas más trabajados:**
1. Tecnología (40%)
2. Productividad (30%)
3. HomeLab (20%)
4. Otros (10%)
```

---

#### 3. Backup Automático a GitHub

**Script completo:**

```powershell
# Script: backup-vault-to-github.ps1

param(
    [string]$VaultPath = "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro",
    [string]$LocalBackupPath = "C:\Backup\Obsidian-Temp"
)

# Copiar desde NAS a local temporal
Write-Host "Copiando desde NAS..."
robocopy $VaultPath $LocalBackupPath /MIR /R:3 /W:5 /NFL /NDL

# Cambiar a directorio local
cd $LocalBackupPath

# Git operations
Write-Host "Commiting cambios..."
git add .

$commitMessage = "Auto-backup $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git commit -m $commitMessage

Write-Host "Pusheando a GitHub..."
git push origin main

# Log
$logFile = "C:\Backup\Logs\backup-log.txt"
Add-Content -Path $logFile -Value "$(Get-Date): Backup completado exitosamente"

Write-Host "✅ Backup completado"
```

**Programar:**
- Frequency: Every 6 hours
- O usar plugin Obsidian Git con auto-commit cada 30 minutos

---

#### 4. Recordatorios Inteligentes

```yaml
# ~/.hermes/reminders.yaml

reminders:
  - name: "Revisar proyectos activos"
    schedule: "every Monday at 9:00 AM"
    action: |
      hermes query "¿Qué proyectos están activos y cuál es su estado?"
      hermes notify --title "Revisión Semanal" --message "Revisa tus proyectos activos"
  
  - name: "Procesar inbox"
    schedule: "every day at 6:00 PM"
    action: |
      hermes query "¿Cuántas notas hay en inbox sin procesar?"
      hermes notify --message "Inbox necesita atención"
  
  - name: "Backup reminder"
    schedule: "every Sunday at 10:00 AM"
    action: |
      hermes notify --title "Backup Semanal" --message "Verifica el backup a GitHub"
```

---

#### 5. Templates Inteligentes con Variables

```markdown
---
template: proyecto-automatico
version: 2.0
---

<%*
// Obtener información del contexto
const projectName = await tp.system.prompt("Nombre del proyecto");
const projectType = await tp.system.suggester(
  ["Desarrollo", "Investigación", "Personal", "Trabajo"],
  ["dev", "research", "personal", "work"]
);
const priority = await tp.system.suggester(
  ["Alta", "Media", "Baja"],
  ["alta", "media", "baja"]
);

// Generar estructura basada en tipo
let taskTemplate = "";
if (projectType === "dev") {
  taskTemplate = `
- [ ] Investigación técnica
- [ ] Diseño de arquitectura
- [ ] Implementación
- [ ] Testing
- [ ] Documentación
- [ ] Deploy`;
} else if (projectType === "research") {
  taskTemplate = `
- [ ] Revisión bibliográfica
- [ ] Recopilación de datos
- [ ] Análisis
- [ ] Redacción de hallazgos
- [ ] Revisión`;
}

const endDate = tp.date.now("YYYY-MM-DD", 30);
%>

# <% projectName %>

**Tipo:** <% projectType %>
**Prioridad:** <% priority %>
**Fecha Inicio:** <% tp.date.now("YYYY-MM-DD") %>
**Fecha Estimada:** <% endDate %>

## ✅ Tareas

<% taskTemplate %>
```

---

## Apéndice G: Integraciones con Otras Herramientas

### 🔗 Conectar Hermes con el Ecosistema

#### 1. Telegram Bot para Capturas Rápidas

```python
# Script: telegram-to-obsidian.py
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
INBOX_PATH = "\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox"

async def capture(update: Update, context):
    """Captura mensaje y lo guarda en inbox"""
    message = update.message.text
    timestamp = update.message.date.strftime("%Y%m%d-%H%M%S")
    
    filename = f"{INBOX_PATH}/telegram-{timestamp}.md"
    
    content = f"""---
fuente: telegram
fecha: {update.message.date}
---

# Captura desde Telegram

{message}

---
*Enviado por {update.message.from_user.first_name}*
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    await update.message.reply_text("✅ Guardado en Obsidian Inbox")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("capture", capture))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture))
    
    print("🤖 Bot iniciado. Envía mensajes para capturar en Obsidian.")
    app.run_polling()

if __name__ == '__main__':
    main()
```

**Configuración:**
1. Habla con @BotFather en Telegram
2. `/newbot` → Crea tu bot → Obtén token
3. Guarda token: `$env:TELEGRAM_BOT_TOKEN = "tu-token"`
4. Ejecuta: `python telegram-to-obsidian.py`

---

#### 2. Discord Webhook para Notificaciones

```python
# Script: obsidian-discord-notify.py
import requests
import os

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

def notify_discord(title, message, color=0x00ff00):
    """Envía notificación a Discord"""
    data = {
        "embeds": [{
            "title": title,
            "description": message,
            "color": color,
            "footer": {"text": "Obsidian + Hermes"}
        }]
    }
    requests.post(DISCORD_WEBHOOK, json=data)

# Ejemplo: Proyecto completado
notify_discord(
    "🎉 Proyecto Completado",
    "HomeLab está 100% completo!",
    color=0x00ff00
)

# Recordatorio de tarea urgente
notify_discord(
    "⚠️ Tarea Urgente",
    "Reunión en 30 minutos",
    color=0xff0000
)
```

---

#### 3. Zapier / Make.com (No-Code)

**Ejemplo de Zap:**

```
Trigger: Nuevo email con etiqueta "Obsidian"
↓
Action 1: Extraer contenido del email
↓
Action 2: Formatear como Markdown
↓
Action 3: Crear archivo en NAS Synology
  Ubicación: /Obsidian-Vault/Mi-Segundo-Cerebro/00-Inbox/
  Nombre: email-{fecha}-{asunto}.md
↓
Action 4: Notificación Discord
```

**Twitter/X a Obsidian:**

```
Trigger: Guardas un tweet (bookmark)
↓
Action: Crear nota en Obsidian
  Template:
  ---
  fuente: twitter
  autor: @{username}
  ---
  
  # Tweet de @{username}
  
  {tweet_content}
  
  [Link]({tweet_url})
```

---

#### 4. IFTTT para Automatizaciones Mobile

**Receta: Dictado de voz**

```
IF: "OK Google, nota para Obsidian"
THEN: 
  - Transcribe audio a texto
  - Envía a webhook
  - Webhook guarda en inbox
```

**Webhook endpoint:**

```python
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
INBOX = "\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox"

@app.route('/voice-capture', methods=['POST'])
def voice_capture():
    data = request.json
    text = data.get('text', '')
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{INBOX}/voice-{timestamp}.md"
    
    content = f"""---
fuente: voz
fecha: {datetime.now()}
---

# Nota de Voz

{text}
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return {"status": "success"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

#### 5. Readwise para Highlights de Lectura

```bash
# Instalar
pip install readwise-obsidian-sync

# Configurar
readwise-sync configure \
  --api-key "tu-api-key" \
  --vault-path "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro"

# Sincronizar
readwise-sync pull --folder "03-Recursos/Lecturas"
```

**Resultado:**

```markdown
---
fuente: readwise
libro: "Atomic Habits"
autor: James Clear
---

# Atomic Habits - Highlights

## Highlight 1
> "You do not rise to the level of your goals. You fall to the level of your systems."

**Mi nota:** Aplica a mi sistema Obsidian.

## Highlight 2
> "Every action is a vote for who you wish to become."

**Conexión:** [[Sistema de Hábitos]]
```

---

#### 6. Todoist Sincronización

```python
# Script: todoist-obsidian-sync.py
from todoist_api_python.api import TodoistAPI
import re

todoist = TodoistAPI("tu-api-key")
TASKS_FILE = "\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\Sistema\\Tareas.md"

def sync_todoist_to_obsidian():
    """Importa tareas de Todoist"""
    tasks = todoist.get_tasks()
    
    content = "# Tareas desde Todoist\n\n"
    for task in tasks:
        due = task.due.date if task.due else "Sin fecha"
        content += f"- [ ] {task.content} 📅 {due} #todoist\n"
    
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def sync_obsidian_to_todoist():
    """Exporta tareas a Todoist"""
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'- \[ \] (.+?) 📅 (\d{4}-\d{2}-\d{2}) #todoist'
    matches = re.findall(pattern, content)
    
    for task_name, due_date in matches:
        todoist.add_task(
            content=task_name,
            due_string=due_date
        )
```

---

#### 7. Google Calendar Sincronización

```python
# Script: sync-calendar.py
import hermes
from google_calendar_api import GoogleCalendar

calendar = GoogleCalendar()

# Crear tareas desde eventos
events = calendar.get_events(days=30)
for event in events:
    hermes.create_task(
        title=event.title,
        due_date=event.date,
        calendar_link=event.url
    )

# Exportar tareas al calendario
tasks = hermes.get_tasks(has_date=True)
for task in tasks:
    if not task.in_calendar:
        calendar.create_event(
            title=task.title,
            date=task.due_date,
            description=f"Desde Obsidian: {task.note_link}"
        )
```

---

#### 8. Notion (Migración)

```bash
# Exportar desde Notion
npm install -g notion-to-md
notion-to-md export --token "tu-token" --output "./notion-export"

# Convertir a Obsidian
python convert-notion-to-obsidian.py \
  --input "./notion-export" \
  --output "\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\03-Recursos\Desde-Notion"
```

---

#### 9. WhatsApp - 3 Formas de Integración

WhatsApp ofrece múltiples formas de integración según tus necesidades:

| Método | Tipo | Costo | Confiabilidad | Complejidad |
|--------|------|-------|---------------|-------------|
| **whatsapp-web.js** | No oficial | Gratis | ⭐⭐⭐ | Baja |
| **Baileys** | No oficial | Gratis | ⭐⭐⭐⭐ | Media |
| **Meta Business API** | Oficial | Pago* | ⭐⭐⭐⭐⭐ | Alta |

*Meta Business API: Primeros 1,000 mensajes/mes gratis, luego desde $0.005 por mensaje.

---

### Opción 1: whatsapp-web.js (Más Simple)

**Ventajas:**
- ✅ Más fácil de configurar
- ✅ No requiere aprobación de Meta
- ✅ Totalmente gratis

**Desventajas:**
- ❌ Menos estable que Baileys
- ❌ Sesión puede expirar más frecuente

**Configurar bot básico:**

**Instalación:**

```bash
# Crear directorio del proyecto
mkdir whatsapp-obsidian-bot
cd whatsapp-obsidian-bot

# Inicializar Node.js
npm init -y

# Instalar dependencias
npm install whatsapp-web.js qrcode-terminal
```

**Script completo:**

```javascript
// Script: whatsapp-to-obsidian.js
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const fs = require('fs');
const path = require('path');

// Configuración
const INBOX_PATH = '\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox';
const COMMAND_PREFIX = '!obs'; // Comando para capturar

// Crear cliente WhatsApp
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: true,
        args: ['--no-sandbox']
    }
});

// Generar QR para conectar
client.on('qr', (qr) => {
    console.log('📱 Escanea este QR con WhatsApp:');
    qrcode.generate(qr, { small: true });
});

// Cliente listo
client.on('ready', () => {
    console.log('✅ WhatsApp Bot conectado!');
    console.log('💡 Envía mensajes con "!obs [texto]" para capturar en Obsidian');
});

// Procesar mensajes
client.on('message', async (message) => {
    const text = message.body;
    
    // Solo procesar si empieza con comando
    if (!text.startsWith(COMMAND_PREFIX)) return;
    
    // Extraer contenido (después del comando)
    const content = text.substring(COMMAND_PREFIX.length).trim();
    
    if (!content) {
        await message.reply('❌ Uso: !obs [tu nota aquí]');
        return;
    }
    
    // Obtener info del mensaje
    const contact = await message.getContact();
    const contactName = contact.pushname || contact.number;
    const timestamp = new Date();
    const filename = `whatsapp-${timestamp.getTime()}.md`;
    
    // Crear nota en formato Markdown
    const noteContent = `---
fuente: whatsapp
autor: ${contactName}
fecha: ${timestamp.toISOString()}
---

# Captura desde WhatsApp

${content}

---
*Enviado por ${contactName} vía WhatsApp*
*Capturado: ${timestamp.toLocaleString('es-ES')}*
`;
    
    // Guardar en inbox
    const filePath = path.join(INBOX_PATH, filename);
    
    try {
        fs.writeFileSync(filePath, noteContent, 'utf-8');
        await message.reply('✅ Guardado en Obsidian Inbox!');
        console.log(`✓ Nota guardada: ${filename}`);
    } catch (error) {
        console.error('Error al guardar:', error);
        await message.reply('❌ Error al guardar en Obsidian');
    }
});

// Manejar errores
client.on('auth_failure', () => {
    console.error('❌ Autenticación fallida');
});

client.on('disconnected', (reason) => {
    console.log('⚠️ Desconectado:', reason);
});

// Iniciar cliente
client.initialize();
```

**Ejecutar el bot:**

```bash
# Primera vez (genera QR)
node whatsapp-to-obsidian.js

# Escanea el QR con tu WhatsApp
# El bot quedará conectado
```

**Usar el bot:**

1. Abre WhatsApp en tu teléfono
2. Envíate un mensaje a ti mismo (o crea grupo solo contigo)
3. Escribe: `!obs Mi idea genial para el proyecto`
4. El bot responde: "✅ Guardado en Obsidian Inbox!"
5. La nota aparece en `00-Inbox/whatsapp-[timestamp].md`

**Comandos adicionales (opcional):**

Puedes extender el bot con más comandos:

```javascript
// Agregar después de la línea "if (!text.startsWith(COMMAND_PREFIX)) return;"

// Comando: !obs-tarea [texto] - Crear tarea
if (text.startsWith('!obs-tarea ')) {
    const taskContent = text.substring('!obs-tarea '.length).trim();
    const taskNote = `- [ ] ${taskContent} #whatsapp 📅 ${new Date().toISOString().split('T')[0]}`;
    // ... guardar como tarea
    await message.reply('✅ Tarea creada!');
    return;
}

// Comando: !obs-urgente [texto] - Captura urgente
if (text.startsWith('!obs-urgente ')) {
    const urgentContent = text.substring('!obs-urgente '.length).trim();
    // ... guardar con etiqueta #urgente
    await message.reply('🚨 Captura urgente guardada!');
    return;
}

// Comando: !obs-help - Ayuda
if (text === '!obs-help') {
    await message.reply(`
📚 *Comandos disponibles:*

!obs [texto] - Captura nota
!obs-tarea [texto] - Crea tarea
!obs-urgente [texto] - Captura urgente
!obs-help - Esta ayuda
    `);
    return;
}
```

**Ejecutar como servicio (siempre activo):**

**Windows (con PM2):**

```powershell
# Instalar PM2 globalmente
npm install -g pm2

# Iniciar bot como servicio
cd whatsapp-obsidian-bot
pm2 start whatsapp-to-obsidian.js --name "whatsapp-obsidian"

# Ver logs
pm2 logs whatsapp-obsidian

# Configurar auto-inicio con Windows
pm2 startup
pm2 save

# Comandos útiles:
pm2 status              # Ver estado
pm2 restart whatsapp-obsidian  # Reiniciar
pm2 stop whatsapp-obsidian     # Detener
pm2 delete whatsapp-obsidian   # Eliminar
```

**Mac/Linux (con PM2):**

```bash
npm install -g pm2
cd whatsapp-obsidian-bot
pm2 start whatsapp-to-obsidian.js --name "whatsapp-obsidian"
pm2 startup
pm2 save
```

**Ventajas de WhatsApp:**
- ✅ Captura desde cualquier lugar (móvil siempre contigo)
- ✅ Interfaz familiar (todos usan WhatsApp)
- ✅ No requiere app adicional
- ✅ Funciona sin internet (mensajes quedan en cola)
- ✅ Puede capturar fotos (guardadas como archivos)

**Limitaciones:**
- ⚠️ Requiere computadora encendida con bot activo
- ⚠️ No es API oficial (puede cambiar)
- ⚠️ Sesión puede expirar (re-escanear QR)

**Capturar imágenes desde WhatsApp:**

```javascript
// Agregar después del manejo de mensajes de texto

if (message.hasMedia) {
    const media = await message.downloadMedia();
    const ext = media.mimetype.split('/')[1];
    const imageFilename = `whatsapp-image-${Date.now()}.${ext}`;
    const imagePath = path.join(INBOX_PATH, imageFilename);
    
    // Guardar imagen
    fs.writeFileSync(imagePath, media.data, 'base64');
    
    // Crear nota con referencia a imagen
    const noteContent = `---
fuente: whatsapp
fecha: ${new Date().toISOString()}
---

# Imagen desde WhatsApp

![](${imageFilename})

${message.body || 'Sin descripción'}
`;
    
    const noteFilename = `whatsapp-${Date.now()}.md`;
    fs.writeFileSync(path.join(INBOX_PATH, noteFilename), noteContent);
    
    await message.reply('✅ Imagen guardada en Obsidian!');
}
```

---

### Opción 2: Baileys (Más Confiable - No Oficial)

**🎯 Recomendada para uso serio**

**Ventajas:**
- ✅ Más estable que whatsapp-web.js
- ✅ Reconexiones automáticas
- ✅ Mejor manejo de sesiones
- ✅ Implementación nativa del protocolo WhatsApp
- ✅ Código activamente mantenido

**Desventajas:**
- ⚠️ Configuración más técnica
- ⚠️ Requiere conocimientos de Node.js

**Instalación:**

```bash
mkdir whatsapp-baileys-bot
cd whatsapp-baileys-bot
npm init -y

# Instalar Baileys
npm install @whiskeysockets/baileys qrcode-terminal
```

**Script completo con Baileys:**

```javascript
// Script: baileys-to-obsidian.js
const { default: makeWASocket, DisconnectReason, useMultiFileAuthState } = require('@whiskeysockets/baileys');
const qrcode = require('qrcode-terminal');
const fs = require('fs');
const path = require('path');

const INBOX_PATH = '\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox';
const COMMAND_PREFIX = '!obs';

async function connectToWhatsApp() {
    // Autenticación persistente
    const { state, saveCreds } = await useMultiFileAuthState('auth_info_baileys');
    
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true
    });
    
    // Guardar credenciales cuando cambien
    sock.ev.on('creds.update', saveCreds);
    
    // Manejo de conexión
    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update;
        
        if (qr) {
            console.log('📱 Escanea este QR con WhatsApp:');
            qrcode.generate(qr, { small: true });
        }
        
        if (connection === 'close') {
            const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log('⚠️ Conexión cerrada. Reconectando:', shouldReconnect);
            
            if (shouldReconnect) {
                connectToWhatsApp(); // Reconectar automáticamente
            }
        } else if (connection === 'open') {
            console.log('✅ WhatsApp conectado con Baileys!');
        }
    });
    
    // Procesar mensajes
    sock.ev.on('messages.upsert', async ({ messages }) => {
        for (const msg of messages) {
            // Ignorar mensajes propios o sin texto
            if (!msg.message || msg.key.fromMe) continue;
            
            const text = msg.message.conversation || 
                        msg.message.extendedTextMessage?.text || '';
            
            // Solo procesar comandos
            if (!text.startsWith(COMMAND_PREFIX)) continue;
            
            const content = text.substring(COMMAND_PREFIX.length).trim();
            
            if (!content) {
                await sock.sendMessage(msg.key.remoteJid, {
                    text: '❌ Uso: !obs [tu nota aquí]'
                });
                continue;
            }
            
            // Obtener info del remitente
            const sender = msg.pushName || msg.key.remoteJid.split('@')[0];
            const timestamp = new Date(msg.messageTimestamp * 1000);
            const filename = `whatsapp-baileys-${timestamp.getTime()}.md`;
            
            // Crear nota
            const noteContent = `---
fuente: whatsapp-baileys
autor: ${sender}
fecha: ${timestamp.toISOString()}
---

# Captura desde WhatsApp

${content}

---
*Enviado por ${sender} vía WhatsApp (Baileys)*
*Capturado: ${timestamp.toLocaleString('es-ES')}*
`;
            
            try {
                const filePath = path.join(INBOX_PATH, filename);
                fs.writeFileSync(filePath, noteContent, 'utf-8');
                
                await sock.sendMessage(msg.key.remoteJid, {
                    text: '✅ Guardado en Obsidian Inbox!'
                });
                
                console.log(`✓ Nota guardada: ${filename}`);
            } catch (error) {
                console.error('Error:', error);
                await sock.sendMessage(msg.key.remoteJid, {
                    text: '❌ Error al guardar'
                });
            }
        }
    });
    
    return sock;
}

// Iniciar
connectToWhatsApp();
```

**Ejecutar:**

```bash
node baileys-to-obsidian.js

# Primera vez: escanea QR
# Siguientes veces: se conecta automáticamente
```

**Ventajas de Baileys sobre whatsapp-web.js:**

| Característica | whatsapp-web.js | Baileys |
|-----------------|-----------------|----------|
| Estabilidad | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Reconexiones | Manual | Automática |
| Manejo de sesiones | Básico | Avanzado |
| Rendimiento | Medio | Alto |
| Mantenimiento | Activo | Muy activo |
| Comunidad | Grande | Mediana |

**Ejecutar como servicio con PM2:**

```bash
npm install -g pm2
pm2 start baileys-to-obsidian.js --name "whatsapp-baileys"
pm2 startup
pm2 save
pm2 logs whatsapp-baileys
```

---

### Opción 3: Meta Business API (Oficial - Profesional)

**🏢 Recomendada para producción/empresas**

**Ventajas:**
- ✅ API oficial de Meta
- ✅ Máxima estabilidad
- ✅ Soporte oficial
- ✅ Webhooks en tiempo real
- ✅ No requiere mantener sesión abierta
- ✅ Escalable

**Desventajas:**
- ❌ Requiere aprobación de Meta (proceso de 1-3 días)
- ❌ Pago después de 1,000 mensajes/mes
- ❌ Configuración más compleja
- ❌ Requiere número telefónico dedicado

**Precios (2026):**
- **1,000 conversaciones/mes:** Gratis 🎉
- **Después:** $0.005 - $0.09 por conversación (según país)
- **Una conversación = 24 horas** con mismo usuario

#### Paso 1: Configuración en Meta

1. **Crear cuenta de Meta Business:**
   - Ve a https://business.facebook.com
   - Crea cuenta empresarial

2. **Configurar WhatsApp Business:**
   - https://developers.facebook.com
   - Crear app → WhatsApp → Business
   - Agregar número de teléfono
   - Verificar número

3. **Obtener credenciales:**
   - **Phone Number ID** (desde dashboard)
   - **Access Token** (generar en configuración)
   - **Webhook Verify Token** (tú lo defines)

4. **Configurar Webhook:**
   - URL del webhook: `https://tu-dominio.com/webhook`
   - Verify token: (el que definiste)
   - Suscripciones: `messages`

#### Paso 2: Servidor Webhook (Node.js + Express)

```bash
mkdir whatsapp-business-api
cd whatsapp-business-api
npm init -y
npm install express body-parser axios dotenv
```

**Crear `.env`:**

```env
WHATSAPP_TOKEN=tu_access_token_aqui
PHONE_NUMBER_ID=tu_phone_number_id
WEBHOOK_VERIFY_TOKEN=tu_token_secreto
INBOX_PATH=\\\\192.168.1.100\\Obsidian-Vault\\Mi-Segundo-Cerebro\\00-Inbox
```

**Script completo:**

```javascript
// Script: meta-business-api.js
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(bodyParser.json());

const WHATSAPP_TOKEN = process.env.WHATSAPP_TOKEN;
const PHONE_NUMBER_ID = process.env.PHONE_NUMBER_ID;
const VERIFY_TOKEN = process.env.WEBHOOK_VERIFY_TOKEN;
const INBOX_PATH = process.env.INBOX_PATH;
const PORT = process.env.PORT || 3000;

// Verificación del webhook (Meta lo llama al configurar)
app.get('/webhook', (req, res) => {
    const mode = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];
    
    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
        console.log('✅ Webhook verificado');
        res.status(200).send(challenge);
    } else {
        res.sendStatus(403);
    }
});

// Recibir mensajes
app.post('/webhook', async (req, res) => {
    const body = req.body;
    
    // Confirmar recepción inmediatamente
    res.sendStatus(200);
    
    // Procesar mensaje
    try {
        if (body.object === 'whatsapp_business_account') {
            body.entry.forEach(async (entry) => {
                const changes = entry.changes[0];
                const value = changes.value;
                
                if (value.messages) {
                    const message = value.messages[0];
                    const from = message.from; // Número del remitente
                    const text = message.text?.body || '';
                    const msgId = message.id;
                    
                    console.log(`📨 Mensaje de ${from}: ${text}`);
                    
                    // Solo procesar comandos !obs
                    if (text.startsWith('!obs ')) {
                        const content = text.substring(5).trim();
                        
                        if (content) {
                            // Guardar en Obsidian
                            const timestamp = new Date();
                            const filename = `whatsapp-business-${timestamp.getTime()}.md`;
                            
                            const noteContent = `---
fuente: whatsapp-business-api
remitente: ${from}
fecha: ${timestamp.toISOString()}
message-id: ${msgId}
---

# Captura desde WhatsApp Business

${content}

---
*Enviado desde: +${from}*
*Capturado: ${timestamp.toLocaleString('es-ES')}*
*Vía: Meta Business API*
`;
                            
                            fs.writeFileSync(
                                path.join(INBOX_PATH, filename),
                                noteContent,
                                'utf-8'
                            );
                            
                            // Enviar confirmación
                            await sendWhatsAppMessage(from, '✅ Guardado en Obsidian!');
                            console.log(`✓ Nota guardada: ${filename}`);
                        } else {
                            await sendWhatsAppMessage(from, '❌ Uso: !obs [tu nota]');
                        }
                    }
                }
            });
        }
    } catch (error) {
        console.error('Error procesando webhook:', error);
    }
});

// Función para enviar mensajes
async function sendWhatsAppMessage(to, text) {
    try {
        await axios({
            method: 'POST',
            url: `https://graph.facebook.com/v21.0/${PHONE_NUMBER_ID}/messages`,
            headers: {
                'Authorization': `Bearer ${WHATSAPP_TOKEN}`,
                'Content-Type': 'application/json'
            },
            data: {
                messaging_product: 'whatsapp',
                to: to,
                text: { body: text }
            }
        });
    } catch (error) {
        console.error('Error enviando mensaje:', error.response?.data || error.message);
    }
}

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`🚀 Webhook escuchando en puerto ${PORT}`);
    console.log(`🔗 URL pública: https://tu-dominio.com/webhook`);
});
```

#### Paso 3: Exponer Webhook Públicamente

**Opción A: ngrok (para desarrollo/testing)**

```bash
# Instalar ngrok
choco install ngrok  # Windows
brew install ngrok   # Mac

# Iniciar servidor local
node meta-business-api.js

# En otra terminal, exponer con ngrok
ngrok http 3000

# Copiar URL HTTPS que da ngrok (ej: https://abc123.ngrok.io)
# Usar esa URL + /webhook en la configuración de Meta
```

**Opción B: Servidor propio (producción)**

Requisitos:
- Dominio propio (ej: `tudominio.com`)
- Servidor VPS (DigitalOcean, AWS, etc.)
- Certificado SSL (Let's Encrypt gratis)

```bash
# En tu servidor
cd /opt
git clone tu-repo whatsapp-business-api
cd whatsapp-business-api
npm install

# Configurar .env
nano .env

# Ejecutar con PM2
pm2 start meta-business-api.js --name "whatsapp-business"
pm2 startup
pm2 save

# Configurar Nginx como proxy reverso
# /etc/nginx/sites-available/whatsapp-webhook
server {
    listen 80;
    server_name webhook.tudominio.com;
    
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

# Habilitar SSL con Certbot
sudo certbot --nginx -d webhook.tudominio.com
```

#### Paso 4: Configurar en Meta Dashboard

1. Developers Dashboard → Tu App → WhatsApp → Configuration
2. Webhook:
   - **Callback URL:** `https://webhook.tudominio.com/webhook`
   - **Verify token:** (el mismo que pusiste en `.env`)
3. Webhook fields: Marca `messages`
4. Guardar

#### Paso 5: Probar

```bash
# Enviar mensaje de prueba desde tu WhatsApp:
!obs Esta es mi primera captura con API oficial

# Deberías recibir:
✅ Guardado en Obsidian!

# Y ver en logs:
📨 Mensaje de 1234567890: !obs Esta es mi primera...
✓ Nota guardada: whatsapp-business-1723291234567.md
```

---

### 📊 Comparación Final de las 3 Opciones

| Criterio | whatsapp-web.js | Baileys | Meta Business API |
|----------|----------------|---------|-------------------|
| **Costo** | Gratis | Gratis | Gratis hasta 1K/mes |
| **Estabilidad** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Configuración** | Fácil | Media | Compleja |
| **Aprobación Meta** | No | No | Sí (1-3 días) |
| **Número dedicado** | No | No | Sí |
| **PC siempre activa** | Sí | Sí | No (webhook) |
| **Soporte oficial** | No | No | Sí |
| **Reconexiones** | Manual | Auto | N/A (webhook) |
| **Escalabilidad** | Baja | Media | Alta |
| **Uso recomendado** | Personal | Personal/Pequeño | Empresarial |

### 🎯 Recomendación Según Caso de Uso

**Usa whatsapp-web.js si:**
- ✅ Solo quieres probar rápido
- ✅ Uso personal ocasional
- ✅ No te importa reconectar manualmente

**Usa Baileys si:**
- ✅ Uso personal/profesional serio
- ✅ Necesitas estabilidad
- ✅ Quieres gratis pero confiable
- ✅ Puedes mantener PC encendida

**Usa Meta Business API si:**
- ✅ Negocio/empresa
- ✅ Alto volumen de mensajes
- ✅ Necesitas soporte oficial
- ✅ No quieres mantener PC activa
- ✅ Presupuesto para hosting

---

### Opción 4: YCloud + n8n (Para Casos Empresariales)

**🏭 Recomendada para múltiples flujos empresariales**

**YCloud** es un BSP (Business Solution Provider) oficial de Meta que simplifica el acceso a WhatsApp Business API sin toda la complejidad de configurar directamente con Meta.

#### ¿Qué es YCloud?

- **BSP Oficial de Meta** - API aprobada y soportada
- **Plan Free disponible** - 1,000 conversaciones gratis/mes
- **Múltiples WABAs** - Puedes tener varias cuentas separadas
- **Webhooks integrados** - Sin necesidad de configurar servidor público
- **Documentación en español** - Más fácil de implementar

**Ventajas vs Meta Business API directa:**

| Aspecto | Meta Directa | YCloud |
|---------|--------------|--------|
| Aprobación | 1-3 días | 1 día |
| Configuración | Compleja | Simple |
| Webhook público | Requerido | Incluido |
| Documentación | Solo inglés | Español/Inglés |
| Soporte | Básico | Dedicado |
| Dashboard | Básico | Avanzado |

#### Arquitectura Recomendada: YCloud + n8n + Obsidian

**Flujo completo:**

```
WhatsApp (tu teléfono)
    ↓
    ↓ Envías: !obs Mi idea para el proyecto
    ↓
YCloud (recibe mensaje)
    ↓
    ↓ Webhook a n8n
    ↓
n8n (orquestador)
    ↓
    │--- Filtra por comando (!obs, !tarea, etc.)
    │--- Procesa con Claude/Hermes (opcional)
    │--- Formatea como Markdown
    ↓
Obsidian Inbox (NAS)
    ↓
    ↓ Archivo guardado: whatsapp-[timestamp].md
    ↓
Hermes procesa inbox automáticamente
```

---

#### Paso 1: Configurar YCloud

1. **Crear cuenta:**
   - Ve a https://ycloud.com
   - Regístrate (plan Free disponible)
   - Verifica email

2. **Configurar WhatsApp Business:**
   - Dashboard → WhatsApp → Add Number
   - Ingresa número telefónico
   - Verifica con SMS
   - Espera aprobación (~24 horas)

3. **Obtener credenciales:**
   - API Key (en Settings → API Keys)
   - WABA ID (en WhatsApp dashboard)
   - Phone Number ID

4. **Configurar Webhook:**
   - Settings → Webhooks
   - URL: (la de n8n, ver paso 2)
   - Events: Marcar "messages"
   - Guardar

---

#### Paso 2: Configurar n8n (Orquestador)

**Qué es n8n:**
- Herramienta de automatización visual (tipo Zapier pero open source)
- Gratis si lo alojas tú mismo
- Conecta WhatsApp → Claude/Hermes → Obsidian

**Instalación (Windows):**

```powershell
# Instalar con npm
npm install -g n8n

# Iniciar n8n
n8n start

# Acceder: http://localhost:5678
```

**Instalación (Mac/Linux):**

```bash
npm install -g n8n
n8n start
```

**O con Docker (recomendado para producción):**

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

---

#### Paso 3: Crear Workflow en n8n

**Workflow completo WhatsApp → Obsidian:**

1. **Abrir n8n** (http://localhost:5678)

2. **Crear nuevo workflow:**
   - New Workflow
   - Nombre: "WhatsApp to Obsidian"

3. **Nodo 1: Webhook (Recibir de YCloud)**
   ```
   Node: Webhook
   Method: POST
   Path: /webhook/whatsapp
   
   ✓ Save
   
   Copiar URL generada (ej: http://localhost:5678/webhook/whatsapp)
   → Usarla en YCloud webhook config
   ```

4. **Nodo 2: Filter (Solo comandos !obs)**
   ```
   Node: IF
   Condition: 
     - {{ $json.messages[0].text.body }} 
     - starts with 
     - "!obs"
   ```

5. **Nodo 3: Code (Formatear mensaje)**
   ```
   Node: Code (JavaScript)
   
   const message = $input.first().json.messages[0];
   const text = message.text.body;
   const from = message.from;
   const timestamp = new Date();
   
   // Extraer contenido después de !obs
   const content = text.substring(4).trim();
   
   // Crear nota Markdown
   const noteContent = `---
fuente: whatsapp-ycloud
remitente: ${from}
fecha: ${timestamp.toISOString()}
---

# Captura desde WhatsApp

${content}

---
*Capturado: ${timestamp.toLocaleString('es-ES')}*
*Vía: YCloud + n8n*
`;
   
   const filename = `whatsapp-ycloud-${timestamp.getTime()}.md`;
   
   return [{
     json: {
       filename: filename,
       content: noteContent,
       from: from
     }
   }];
   ```

6. **Nodo 4: Write File (Guardar en Obsidian)**
   ```
   Node: Write Binary File
   
   File Path: \\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro\00-Inbox\{{ $json.filename }}
   
   Data: {{ $json.content }}
   ```

7. **Nodo 5: HTTP Request (Responder a WhatsApp)**
   ```
   Node: HTTP Request
   
   Method: POST
   URL: https://api.ycloud.com/v2/whatsapp/messages
   
   Authentication: Header Auth
   Header Name: X-API-Key
   Header Value: [tu-ycloud-api-key]
   
   Body:
   {
     "to": "{{ $json.from }}",
     "type": "text",
     "text": {
       "body": "✅ Guardado en Obsidian Inbox!"
     }
   }
   ```

8. **Guardar workflow** y activarlo

---

#### Paso 4: Exponer n8n Públicamente (Para Webhooks)

**Opción A: ngrok (desarrollo/testing)**

```bash
# Instalar ngrok
choco install ngrok  # Windows
brew install ngrok   # Mac

# Exponer n8n
ngrok http 5678

# Copiar URL HTTPS
# Ejemplo: https://abc123.ngrok.io

# En YCloud webhook, usar:
# https://abc123.ngrok.io/webhook/whatsapp
```

**Opción B: Cloudflare Tunnel (gratis, permanente)**

```bash
# Instalar cloudflared
choco install cloudflared  # Windows
brew install cloudflared   # Mac

# Crear tunnel
cloudflared tunnel --url http://localhost:5678

# Te da URL permanente:
# https://tu-tunnel.trycloudflare.com

# Webhook en YCloud:
# https://tu-tunnel.trycloudflare.com/webhook/whatsapp
```

**Opción C: n8n Cloud (más simple, de pago)**

- https://n8n.cloud
- Plan desde $20/mes
- Webhook incluido
- No requieres mantener PC encendida

---

#### Paso 5: Workflow Avanzado con Claude/Hermes

**Agregar procesamiento con IA antes de guardar:**

Entre el Nodo 2 (Filter) y Nodo 3 (Code), agregar:

**Nodo 2.5: HTTP Request a Claude/Hermes**

```javascript
Node: HTTP Request

Method: POST
URL: https://api.anthropic.com/v1/messages

Headers:
  x-api-key: [tu-anthropic-key]
  anthropic-version: 2023-06-01
  content-type: application/json

Body:
{
  "model": "claude-haiku-4-5",
  "max_tokens": 500,
  "messages": [{
    "role": "user",
    "content": "Procesa esta captura de WhatsApp y mejora el formato si es necesario. Si es una tarea, agrega checkbox [ ]. Si tiene fecha, extúéla. Texto: {{ $json.messages[0].text.body.substring(4) }}"
  }]
}
```

Luego en Nodo 3, usa la respuesta de Claude como contenido.

---

#### Comandos Múltiples con n8n

Puedes extender el workflow para múltiples comandos:

```
!obs [texto] → Captura simple en inbox
!tarea [texto] → Crea tarea con checkbox
!proyecto [nombre] → Crea nota de proyecto con template
!idea [texto] → Guarda en carpeta Ideas/
!urgente [texto] → Envía notificación + guarda
!foto → Descarga foto adjunta + guarda en Obsidian
!audio → Transcribe audio + guarda texto
```

**Implementación en n8n:**

Reemplazar Nodo 2 (IF) con **Switch** (múltiples rutas):

```
Node: Switch

Mode: Rules

Rules:
1. If {{ $json.messages[0].text.body }} starts with "!obs" → Output 1
2. If {{ $json.messages[0].text.body }} starts with "!tarea" → Output 2
3. If {{ $json.messages[0].text.body }} starts with "!proyecto" → Output 3
4. If {{ $json.messages[0].text.body }} starts with "!idea" → Output 4
```

Cada output lleva a un flujo diferente con su propio template y carpeta destino.

---

#### Ventajas de YCloud + n8n vs Otras Opciones

| Ventaja | Descripción |
|---------|-------------|
| **Múltiples flujos** | Un solo n8n maneja captura, tareas, recordatorios, etc. |
| **Sin código complejo** | Visual, drag & drop, fácil de modificar |
| **Escalable** | Puedes tener 3 WABAs (soporte, marketing, interno) en el mismo n8n |
| **Integraciones** | n8n conecta con 400+ servicios (Drive, Sheets, etc.) |
| **Procesamiento con IA** | Agrega Claude/Hermes en cualquier punto del flujo |
| **Monitoreo** | Ver logs, errores, mensajes procesados en tiempo real |
| **Fallback** | Si Obsidian/NAS no disponible, guarda en backup |

---

#### Costo Real de YCloud

**Plan Free:**
- 1,000 conversaciones/mes gratis
- 1 conversación = 24 horas con mismo usuario
- Para uso personal de captura: suficiente

**Ejemplo:**
- Tú envías 50 mensajes/día con !obs
- Todos son a ti mismo = 1 conversación/día
- 30 días = 30 conversaciones/mes
- **Totalmente gratis dentro del plan**

**Después de 1,000:**
- ~$0.005 - $0.02 por conversación (según país)
- Para 3,000 conversaciones/mes: ~$10-20/mes

---

#### Template de Workflow n8n (Importar)

Puedes descargar el workflow completo listo para importar:

**Archivo:** `whatsapp-ycloud-obsidian.json`

```json
{
  "name": "WhatsApp YCloud to Obsidian",
  "nodes": [
    {
      "name": "Webhook YCloud",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300],
      "webhookId": "whatsapp-ycloud",
      "parameters": {
        "path": "webhook/whatsapp",
        "responseMode": "onReceived",
        "responseData": "firstEntryJson"
      }
    },
    {
      "name": "Filter Commands",
      "type": "n8n-nodes-base.if",
      "position": [450, 300],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.messages[0].text.body }}",
              "operation": "startsWith",
              "value2": "!obs"
            }
          ]
        }
      }
    },
    {
      "name": "Format Note",
      "type": "n8n-nodes-base.code",
      "position": [650, 300],
      "parameters": {
        "jsCode": "// Ver código completo arriba"
      }
    },
    {
      "name": "Save to Obsidian",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [850, 300],
      "parameters": {
        "fileName": "={{ $json.filename }}",
        "dataPropertyName": "content",
        "options": {}
      }
    },
    {
      "name": "Reply Confirmation",
      "type": "n8n-nodes-base.httpRequest",
      "position": [1050, 300],
      "parameters": {
        "url": "https://api.ycloud.com/v2/whatsapp/messages",
        "method": "POST",
        "authentication": "genericCredentialType",
        "sendBody": true,
        "bodyParameters": {
          "to": "={{ $json.from }}",
          "type": "text",
          "text": { "body": "✅ Guardado en Obsidian!" }
        }
      }
    }
  ],
  "connections": {
    "Webhook YCloud": { "main": [[{ "node": "Filter Commands" }]] },
    "Filter Commands": { "main": [[{ "node": "Format Note" }]] },
    "Format Note": { "main": [[{ "node": "Save to Obsidian" }]] },
    "Save to Obsidian": { "main": [[{ "node": "Reply Confirmation" }]] }
  }
}
```

**Importar en n8n:**
1. n8n → Workflows → Import from File
2. Seleccionar `whatsapp-ycloud-obsidian.json`
3. Configurar credenciales (YCloud API key, ruta Obsidian)
4. Activate

---

#### Caso de Uso Avanzado: Múltiples WABAs

Según tu arquitectura anterior, puedes tener:

**WABA 1: Captura Personal (Obsidian)**
- Solo tú
- Comandos: !obs, !tarea, !idea, !proyecto
- Flujo: WhatsApp → YCloud → n8n → Obsidian

**WABA 2: Agente de Soporte**
- Clientes externos
- RAG con Claude sobre documentación
- Flujo: WhatsApp → YCloud → n8n → Claude → Respuesta

**WABA 3: Equipo Interno (Reportes)**
- Whitelist de números
- Captura de depósitos, reportes
- Flujo: WhatsApp → YCloud → n8n → Base de datos

**Un solo n8n maneja los 3 WABAs:**
- Cada WABA tiene su propio webhook
- n8n rutea según webhook origen
- Diferentes credenciales y flujos por WABA

---

### 🔄 Resumen de Integraciones

| Herramienta | Tipo | Dificultad | Beneficio |
|-------------|------|------------|-----------|
| Telegram Bot | Captura rápida | Media | ⭐⭐⭐⭐⭐ |
| Discord | Notificaciones | Fácil | ⭐⭐⭐⭐ |
| Zapier/Make | No-code | Fácil | ⭐⭐⭐⭐⭐ |
| IFTTT | Mobile | Fácil | ⭐⭐⭐⭐ |
| Readwise | Lectura | Fácil | ⭐⭐⭐⭐⭐ |
| Todoist | Tareas | Media | ⭐⭐⭐⭐ |
| Calendar | Calendario | Media | ⭐⭐⭐⭐ |
| Notion | Migración | Alta | ⭐⭐⭐ |
| **WhatsApp Bot** | **Captura mobile** | **Media-Alta** | **⭐⭐⭐⭐⭐** |

---

*Continúa en: APENDICES-H-I.md*
