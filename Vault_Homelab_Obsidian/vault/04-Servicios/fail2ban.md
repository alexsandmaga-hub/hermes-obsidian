---
tags: [homelab, servicio, seguridad]
---

# fail2ban

**Nodo:** Todos los nodos con SSH accesible (Pi's, M920q, MSI Cubi NUC)
**Rol:** Bloquea automáticamente IPs que intentan fuerza bruta por SSH.

## Por qué en todos los nodos, no solo uno

Cada nodo con su propio SSH expuesto (aunque sea solo dentro de la LAN/Tailscale) es un punto de entrada potencial — fail2ban es de instalación rápida y bajo costo, vale la pena estandarizarlo en todos.

## Ver también

- [[Registro de Decisiones]]
- [[Acceso Remoto (Tailscale)]]
