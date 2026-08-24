---
tags: [homelab, decisiones, adr]
---

# Registro de decisiones

Historial de por qué se decidió cada cosa — para no repetir la discusión ni gastar tokens re-explicando contexto.

## Roles fijos, no cluster homogéneo
**Decisión:** cada nodo tiene un rol fijo según su fortaleza real, no un cluster tipo k3s.
**Por qué:** el Mac Mini es mucho más potente que las Pi — un cluster homogéneo desperdiciaría esa ventaja.

## n8n se queda en Contabo por ahora
**Decisión:** no migrar n8n al homelab todavía.
**Por qué:** evitar mezclar "estoy aprendiendo Docker" con "no puedo romper esto, mis flujos dependen de que funcione". Migrar solo cuando el proceso ya se domine.

## Tienda virtual pública en Contabo, no en casa
**Decisión:** el e-commerce público vive en el VPS, nunca en las Pi.
**Por qué:** uptime, IP fija real, cumplimiento de seguridad (PCI-DSS) más fácil en infraestructura profesional.

## MSI Cubi NUC = red/multimedia, no cómputo pesado tipo Mac
**Decisión:** el NUC corre firewall (pfSense/OPNsense) + Jellyfin, no se usa como "segundo Mac Mini".
**Por qué:** solo tiene 1 slot M.2 (sin expansión de storage) y RAM soldada — su fortaleza real es la doble LAN 2.5G y el Arc 140V para transcodificación, no virtualización pesada.

## Pi #4: Home Assistant + Frigate, sin NVMe
**Decisión:** el Pi #4 no lleva el HAT S2Pi de NVMe — lleva el AI HAT+ (Hailo) en su lugar.
**Por qué:** la Pi 5 solo tiene un conector PCIe físico, y ambos HATs lo necesitan. Frigate no requiere tanto almacenamiento rápido como para justificar pelear ese puerto.

## Blink no entra a Frigate
**Decisión:** Blink se integra a Home Assistant solo vía su API en la nube (notificaciones/estado), nunca a Frigate.
**Por qué:** Blink no ofrece RTSP/streaming en vivo nativo — el bridge de la comunidad tiene ~30s de delay y sigue dependiendo de la nube.

## Hikvision sí entra a Frigate
**Decisión:** las cámaras Hikvision alimentan Frigate directamente vía RTSP.
**Por qué:** soporte RTSP nativo completo, sin workarounds.

## DS723+ primario, DS214 solo backup vía Hyper Backup
**Decisión:** no se usa Snapshot Replication entre los dos NAS.
**Por qué:** el DS214 es de ~2013 (ARM), probablemente no soporta Btrfs (requisito de Snapshot Replication). Hyper Backup funciona con ext4 y logra el mismo resultado.

## Fotos: 2 copias, no 3
**Decisión:** el Drobo no se usa para backup de fotos.
**Por qué:** 2 copias (DS723+ + DS214) se consideraron suficientes; se prefirió liberar el Drobo para otro uso.

## Drobo = archivo de video de Frigate
**Decisión:** el Drobo se dedica al archivo frío de clips de cámaras de seguridad.
**Por qué:** el video de seguridad es lo que más crece con el tiempo — separarlo evita que compita por espacio con fotos/Nextcloud/Jellyfin en el NAS principal. Nota de precaución: Drobo es una empresa cerrada (2023) con formato RAID propietario (BeyondRAID) — por eso no se usa para nada crítico.

## Bóveda de Obsidian vive en el DS723+, sincronizada vía Nextcloud
**Decisión:** no se compra almacenamiento nuevo para documentación.
**Por qué:** una bóveda de Obsidian pesa megabytes, no terabytes — se aprovecha infraestructura ya existente (NAS + Nextcloud que ya iba a correr de todos modos).

## Acceso remoto: Tailscale subnet router, no Cloudflare Tunnel para todo
**Decisión:** Tailscale instalado en el Pi #1, anunciando toda la red local (192.168.1.0/24) como subnet router.
**Por qué:** paneles administrativos sensibles (Proxmox, DSM del NAS) no deben exponerse vía túnel público como los servicios de cara al público (Vaultwarden, n8n). Un subnet router da acceso remoto a toda la red de casa desde un solo punto de viaje, sin exponer nada directo a internet.

## ThinkCentre M920q en vez de M720q
**Decisión:** se eligió el M920q como nodo de Proxmox.
**Por qué:** mismo precio prácticamente, mismo chasis, pero con NIC Intel I219-LM (sin las fallas de red conocidas del I219-V del M720q bajo Proxmox) y techo de CPU más alto (hasta i9-9900).

## No se compró un segundo NUC para IA
**Decisión:** el Mac Mini se queda como único nodo de IA/Jarvis — no se agregó un NUC dedicado adicional.
**Por qué:** la inferencia de IA depende de la GPU/memoria unificada; un NUC sin GPU dedicada no habría aportado más poder real de IA, solo redundancia costosa.

## Revisión de la arquitectura de Erik Taveras (AutoDev Community)
**Decisión:** se mantiene la arquitectura distribuida (Pi's + Mac Mini + NUC + M920q + doble NAS) en vez de migrar a un solo servidor tipo "todo en una PC" como el de Erik (34 servicios/90 contenedores en una sola máquina).
**Por qué:** el modelo de una sola PC tiene un techo estructural — un solo punto de falla y un techo de CPU/RAM compartido entre todo. La arquitectura distribuida ya resuelto en este homelab da aislamiento de fallas y más margen de crecimiento real.
**Piezas adoptadas de su guía:** Diun (notificación de updates sin auto-actualizar), Dozzle (logs centralizados), fail2ban (protección SSH), SearXNG (búsqueda privada para los agentes de IA/Jarvis), Gitea/Forgejo (control de versiones propio para los 3 proyectos web), Postiz (programación de redes sociales), Docuseal (firma electrónica self-hosted).
**Piezas descartadas:** Watchtower en automático (mismo motivo que ya se había decidido evitar); todo-en-una-PC como modelo general.

## Ver también

- [[Arquitectura General]]
- [[Home]]
