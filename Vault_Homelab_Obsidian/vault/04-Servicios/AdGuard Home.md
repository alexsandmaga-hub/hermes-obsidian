---
tags: [homelab, servicio, red]
---

# AdGuard Home

**Nodo:** Pi 5 #1 (8GB)
**Rol:** DNS de toda la red + bloqueo de anuncios/tracking.

## Notas

- Una vez arriba, cambiar el DNS del router/switch para que toda la red lo use automáticamente.
- Nodo más crítico de todos — si se cae, se pierde DNS para toda la casa. Ver [[Arquitectura General]] sobre Pi #4 como DNS redundante (opción descartada a favor de Home Assistant + Frigate, evaluar si vale la pena un segundo AdGuard en otro nodo liviano).

## Ver también

- [[Arquitectura General]]
