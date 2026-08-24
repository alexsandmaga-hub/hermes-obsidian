# 🏠 Integración Homelab + Obsidian + Hermes

## 📊 Resumen de tu Arquitectura Actual

### Hardware Inventory
| Nodo | Specs | Rol Asignado | Estado |
|------|-------|--------------|--------|
| **Mac Mini** | 32GB RAM, 512GB SSD | IA (Ollama/Open WebUI) + Nextcloud | Pendiente |
| **MSI Cubi NUC AI+** | Core Ultra 9, 32GB, Arc 140V | Firewall + Jellyfin/Plex | Pendiente |
| **ThinkCentre M920q** | i7/i9 8/9 gen, hasta 64GB | Proxmox (VMs staging) | Pendiente |
| **Pi 5 #1** | 8GB, NVMe 512GB, PoE | DNS (AdGuard) + Vaultwarden + CF Tunnel | ✅ Operativa |
| **Pi 5 #2** | 16GB, NVMe 512GB, PoE | n8n + Postgres | Pendiente |
| **Pi 5 #3** | 16GB, NVMe 512GB, PoE | Monitoreo (Homepage, Beszel) | Pendiente |
| **Pi 5 #4** | Sin NVMe + AI HAT 13 TOPS | Home Assistant + Frigate NVR | Pendiente |
| **NAS DS723+** | 2 bahías, RAID 1, DSM 7 | Primario (Nextcloud, Jellyfin, Docker) | Pendiente |
| **NAS DS214** | 2 bahías, ARM, DSM 6 | Backup (Hyper Backup) | Pendiente |
| **Drobo** | BeyondRAID | Archivo frío Frigate | Pendiente |

### Servicios Activos Planeados
- **n8n** - Actualmente en Contabo VPS (no migrará pronto)
- **Vaultwarden** - Gestor de contraseñas
- **AdGuard Home** - DNS + Ad blocking
- **Jellyfin** - Media server
- **Nextcloud** - Nube personal
- **Synology Photos** - Fotos
- **Frigate + Home Assistant** - NVR + Domótica
- **Tailscale** - VPN mesh
- **Chatwoot** - Soporte clientes
- **Cal.com** - Calendario
- **Listmonk** - Newsletters
- Y 10 servicios más...

### Proyectos que Usarán la Infraestructura
1. **Santa Diabla** (Prioridad #2) - Blog, tienda, podcast, sitio de citas
2. **Academia de Poker** (Prioridad #3)
3. **Mitos y Leyendas** (Prioridad #4) - Canal faceless + merchandising
4. **Amazon** - Proyecto e-commerce/afiliados

---

## 🎯 Recomendaciones para Integración con Obsidian + Hermes

### 1. Estructura de Bóveda Recomendada

Tu actual estructura es **EXCELENTE**. Solo necesita pequeños ajustes:

```
Mi-Segundo-Cerebro/  (Bóveda principal)
├── 01-Proyectos/
│   ├── HomeLab/                    ← Aquí va tu vault actual
│   │   ├── 00-Inicio/
│   │   ├── 01-Arquitectura/
│   │   ├── 02-Runbooks/
│   │   ├── 03-Troubleshooting/
│   │   ├── 04-Servicios/
│   │   ├── 05-Backups/
│   │   ├── 06-Tienda-Virtual/
│   │   ├── 07-Decisiones/
│   │   └── Attachments/
│   │
│   ├── Santa-Diabla/
│   │   ├── Blog/
│   │   ├── Tienda/
│   │   ├── Podcast/
│   │   └── Sitio-Citas/
│   │
│   ├── Academia-Poker/
│   ├── Mitos-y-Leyendas/
│   └── Amazon/
│       ├── Productos/
│       ├── Análisis-Mercado/
│       ├── Contenido/
│       └── Métricas/
│
├── 02-Areas/
│   ├── Desarrollo/
│   ├── Infraestructura/
│   └── Negocios/
│
├── 03-Recursos/
│   ├── Documentación-Técnica/
│   ├── Guías-Docker/
│   └── Referencias-API/
│
└── 00-Inbox/                       ← Capturas desde WhatsApp/Telegram
    └── (aquí llegan las capturas rápidas)
```

### 2. Dónde Almacenar la Bóveda

**Recomendación:** NAS DS723+ (cuando esté configurado)

**Ubicación exacta:**
```
\\192.168.1.100\Obsidian-Vault\Mi-Segundo-Cerebro
```

**Por qué:**
- ✅ RAID 1 = redundancia
- ✅ Accesible desde todas tus máquinas
- ✅ Synology Drive Client = sync automático PC/Mac
- ✅ Hyper Backup hacia DS214 = doble backup
- ✅ Snapshot Replication = versiones

**Mientras tanto (DS723+ pendiente):**
- Almacena localmente en tu PC
- Usa Obsidian Git plugin → GitHub
- Cuando DS723+ esté listo, migras

---

## 🔗 Integraciones Específicas para Tu Homelab

### Integración 1: WhatsApp → n8n → Obsidian

Ya tienes **n8n en Contabo**, ¡perfecto para esto!

**Flujo propuesto:**

```
WhatsApp (YCloud/Baileys)
    ↓
n8n (Contabo) - Webhook
    ↓
Procesa mensaje con Claude (Haiku 4.5)
    ↓
Determina categoría:
    ├─ !homelab → Guarda en HomeLab/00-Inicio/
    ├─ !santa → Guarda en Santa-Diabla/
    ├─ !poker → Guarda en Academia-Poker/
    ├─ !amazon → Guarda en Amazon/
    └─ !obs → Guarda en 00-Inbox/
    ↓
Escribe archivo en NAS DS723+ vía SMB/WebDAV
    ↓
Responde confirmación a WhatsApp
```

**Ventajas:**
- ✅ n8n ya está en producción (Contabo)
- ✅ No depende de tu internet casero
- ✅ Puede escribir directamente al NAS vía SMB
- ✅ Claude procesa y categoriza automáticamente

**Script n8n a agregar:**

Nodo adicional para escribir al NAS:

```javascript
// Nodo: Write to NAS
Node: Execute Command (SSH to NAS)

// O mejor: HTTP Request a Nextcloud API
Method: PUT
URL: https://nextcloud.tudominio.com/remote.php/dav/files/usuario/Mi-Segundo-Cerebro/00-Inbox/{{ $json.filename }}
Auth: Basic (usuario Nextcloud)
Body: {{ $json.content }}
```

---

### Integración 2: Servicios del Homelab → Obsidian

**Automatizar documentación de servicios:**

Cada vez que instalas un servicio nuevo, n8n crea automáticamente una nota en `04-Servicios/`:

**Workflow n8n:**

```
Trigger: Manual (cuando instalas servicio)
    ↓
Input: Nombre del servicio, nodo, puertos, variables
    ↓
Claude genera nota markdown con template
    ↓
Guarda en 04-Servicios/[NombreServicio].md
    ↓
Actualiza Home.md con enlace [[NombreServicio]]
```

**Template automático:**

```markdown
---
tags: [homelab, servicio, {servicio}]
---

# {Servicio}

**Nodo:** {nodo}
**Puerto:** {puerto}
**Estado:** Activo
**Instalado:** {fecha}

## Docker Compose

```yaml
{docker-compose generado}
```

## Acceso

- URL local: http://{ip}:{puerto}
- URL pública: https://{servicio}.tudominio.com (vía Tailscale/CF Tunnel)

## Credenciales

Ver Vaultwarden: {link-vaultwarden}

## Troubleshooting

Ver [[Metodologia de Troubleshooting]]

## Logs

```bash
docker logs {container} -f
```
```

---

### Integración 3: Hermes + Homelab

**Comandos de Hermes para tu Homelab:**

```bash
# Buscar info sobre un servicio
hermes query "¿Cómo configuré n8n?"
→ Lee 04-Servicios/n8n.md

# Generar runbook
hermes create runbook \
  --servicio "Nextcloud" \
  --template "02-Runbooks/template.md"

# Analizar decisiones
hermes analyze \
  --folder "07-Decisiones" \
  --pregunta "¿Por qué elegí Jellyfin sobre Plex?"

# Troubleshooting asistido
hermes troubleshoot \
  --servicio "AdGuard Home" \
  --error "DNS no resuelve"
→ Lee 03-Troubleshooting/ y sugiere pasos

# Actualizar inventario
hermes update \
  --file "01-Arquitectura/Arquitectura General.md" \
  --campo "Pi 5 #2" \
  --estado "operativa"
```

---

### Integración 4: Monitoreo → Obsidian

**Dashboard en Obsidian con Dataview:**

Crea `00-Inicio/Dashboard.md`:

````markdown
# 📊 Dashboard del Homelab

## Estado de Nodos

```dataview
TABLE rol, estado, switch
FROM "01-Proyectos/HomeLab/01-Arquitectura"
WHERE contains(file.name, "Arquitectura")
```

## Servicios por Nodo

```dataview
LIST
FROM "01-Proyectos/HomeLab/04-Servicios"
WHERE estado = "activo"
GROUP BY nodo
```

## Últimas Decisiones

```dataview
TABLE fecha, decisión, razón
FROM "01-Proyectos/HomeLab/07-Decisiones"
SORT fecha DESC
LIMIT 5
```

## Backups Pendientes

```dataview
TASK
FROM "01-Proyectos/HomeLab/05-Backups"
WHERE !completed
```
````

---

## 🚀 Plan de Implementación Paso a Paso

### Fase 1: Fundación (Ahora - 2 semanas)

- [ ] **Configurar NAS DS723+**
  - Crear carpeta compartida `Obsidian-Vault`
  - Instalar Synology Drive Server
  - Configurar permisos

- [ ] **Migrar vault actual al NAS**
  - Copiar `Vault_Homelab_Obsidian/vault/*` → `Mi-Segundo-Cerebro/01-Proyectos/HomeLab/`
  - Configurar Obsidian apuntando al NAS
  - Probar sync entre PC y Mac

- [ ] **Setup básico Hermes**
  - Instalar Hermes
  - Configurar CLAUDE.md con contexto de homelab
  - Probar comandos básicos

### Fase 2: Automatización (Semanas 3-4)

- [ ] **Integrar n8n (Contabo) con NAS**
  - Workflow: WhatsApp → n8n → NAS
  - Probar escritura de archivos vía WebDAV/Nextcloud
  - Implementar comandos (!homelab, !santa, !poker, !amazon)

- [ ] **Template automático de servicios**
  - Workflow n8n para generar notas de servicios
  - Probar con 2-3 servicios de prueba

- [ ] **Configurar backups**
  - Git auto-commit con Obsidian Git plugin
  - Hyper Backup hacia DS214
  - Snapshot Replication cada 6 horas

### Fase 3: Optimización (Semanas 5-6)

- [ ] **Claude procesamiento avanzado**
  - n8n → Claude categoriza automáticamente
  - Extrae metadatos (tags, fechas, prioridades)
  - Sugiere enlaces entre notas

- [ ] **Dashboard Dataview**
  - Vista consolidada de todos los proyectos
  - Estado de nodos en tiempo real (vía API)
  - Alertas de backups pendientes

- [ ] **Integración con otros servicios**
  - Home Assistant → Obsidian (logs de eventos)
  - Frigate → Obsidian (resumen de detecciones)
  - n8n → Obsidian (registro de workflows ejecutados)

---

## ⚠️ Consideraciones Importantes

### 1. n8n en Contabo vs Local

**Tu decisión de mantener n8n en Contabo es CORRECTA** para:
- ✅ Tienda virtual (producción)
- ✅ Webhooks públicos (YCloud, Stripe, etc.)
- ✅ Automatizaciones críticas de negocio

**Considera n8n local (Pi 5 #2) para:**
- ✅ Automatizaciones del homelab (no críticas)
- ✅ Procesamiento de WhatsApp personal
- ✅ Tareas que interactúan con servicios locales

**Recomendación:** Dos instancias de n8n
- **n8n Contabo** → Producción (tienda, negocio)
- **n8n Pi #2** → Homelab (automatizaciones caseras, capturas Obsidian)

### 2. Seguridad del NAS

Si expones el NAS para escritura desde n8n (Contabo), asegura:

```yaml
# Opción A: VPN (Recomendado)
Contabo → Tailscale VPN → NAS (red privada)

# Opción B: WebDAV con auth
Contabo → HTTPS + Basic Auth → Nextcloud WebDAV → NAS

# Opción C: API dedicada
Pi local → API REST → recibe desde n8n Contabo → escribe en NAS
```

### 3. Sincronización Multi-dispositivo

**Windows PC + Mac** accediendo al mismo vault en NAS:

```
Windows PC
    ↓
Synology Drive Client
    ↓
NAS DS723+ (fuente de verdad)
    ↓
Synology Drive Client
    ↓
Mac
```

**Configuración:**
- Modo: "Two-way sync"
- Conflict resolution: "Keep both versions"
- Obsidian: Disable auto-sync, use Synology Drive

### 4. Performance

NAS DS723+ vía 2.5Gb ethernet = **EXCELENTE** para Obsidian

**Tiempos esperados:**
- Abrir bóveda: < 2 segundos
- Guardar nota: Instantáneo
- Sync entre dispositivos: < 5 segundos
- Búsqueda full-text: < 1 segundo

---

## 🎨 Recomendaciones Adicionales

### 1. Plugin Obsidian para Homelab

**Plugins esenciales para tu caso:**

```
✅ Dataview - Dashboards dinámicos
✅ Templater - Templates de servicios
✅ Obsidian Git - Backup automático
✅ Excalidraw - Diagramas de red
✅ Tasks - Seguimiento de tareas de mantenimiento
✅ Calendar - Vista de timeline de cambios
✅ Homepage - Dashboard como inicio
```

### 2. CLAUDE.md Personalizado

Crea en raíz de vault:

```markdown
# Contexto del Homelab

Eres un asistente especializado en mi homelab personal.

## Hardware
- 4 Raspberry Pi 5 con roles específicos
- Mac Mini para IA (Ollama)
- NAS Synology DS723+ (primario) + DS214 (backup)
- MSI Cubi NUC AI+ para firewall
- ThinkCentre M920q para Proxmox

## Servicios
Ver carpeta 04-Servicios/ para lista completa

## Proyectos
1. Santa Diabla (prioridad #2)
2. Academia de Poker (#3)
3. Mitos y Leyendas (#4)
4. Amazon (e-commerce/afiliados)

## Cuando analices:
- Prioriza uptime y simplicidad
- Respeta decisión de prod en Contabo
- Sugiere soluciones basadas en hardware real
- Referencia documentos existentes con [[enlaces]]

## Ubicación de archivos
- Runbooks: 02-Runbooks/
- Troubleshooting: 03-Troubleshooting/
- Decisiones: 07-Decisiones/
```

### 3. Automatización de Decisiones

Cada vez que tomes una decisión de arquitectura:

**Template:** `07-Decisiones/YYYY-MM-DD-Titulo.md`

```markdown
---
fecha: {fecha}
decision: {título}
tags: [decisión, homelab]
---

# {Título de la Decisión}

## Contexto
¿Qué problema se está resolviendo?

## Opciones Evaluadas
1. Opción A - Pros/Contras
2. Opción B - Pros/Contras

## Decisión
Elegimos [X] porque...

## Consecuencias
- Positivas:
- Negativas:

## Revisión
Revisar esta decisión en: {fecha + 6 meses}
```

**Workflow n8n automático:**

Cada 6 meses, n8n:
1. Lee todas las decisiones
2. Filtra las que deben revisarse
3. Crea tarea en Obsidian: "Revisar decisión: [X]"
4. Notifica por Telegram

---

## 📈 Métricas de Éxito

Sabrás que la integración funciona bien cuando:

- [  ] Puedes capturar ideas desde WhatsApp y aparecen en Obsidian en < 10 segundos
- [  ] Hermes responde preguntas sobre servicios leyendo la documentación actualizada
- [  ] Instalas un servicio nuevo y la nota se genera automáticamente
- [  ] Tus 4 proyectos (Santa Diabla, Poker, Mitos, Amazon) están documentados y enlazados al homelab
- [  ] El NAS se cae y recuperas todo desde backup en < 30 minutos
- [  ] Trabajas indistintamente desde PC o Mac sin conflictos
- [  ] Dataview te muestra dashboard actualizado en tiempo real

---

## 🔗 Enlaces Útiles

**En tu guía principal:**
- Ver: `GUIA-COMPLETA-Hermes-Obsidian-Claude.md`
- Apéndice A: Configuración NAS Synology
- Apéndice G: Integración WhatsApp (YCloud + n8n)
- Apéndice F: Workflows avanzados

**En tu vault de Homelab:**
- `00-Inicio/Home.md` - Dashboard principal
- `01-Arquitectura/Arquitectura General.md` - Inventario
- `04-Servicios/n8n.md` - Config actual

---

## ✅ Próximos Pasos Recomendados

**Esta semana:**
1. Lee tu vault actual extraída
2. Decide si integras TODO en una bóveda o mantienes separado
3. Configura NAS DS723+ siguiendo Apéndice A de la guía

**Próxima semana:**
1. Migra vault al NAS
2. Instala Hermes y prueba comandos básicos
3. Configura n8n local en Pi #2 (paralelo al de Contabo)

**Mes 1:**
1. Implementa WhatsApp → n8n → Obsidian
2. Crea templates automáticos de servicios
3. Setup Dataview dashboards

**¿Dudas o necesitas ayuda con algún paso específico?** 🚀
