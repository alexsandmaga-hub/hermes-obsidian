---
tags: [homelab, servicio, mantenimiento]
---

# Diun

**Nodo:** Pi #3 (junto a Beszel/Homepage)
**Rol:** Avisa cuando hay una imagen Docker nueva disponible — sin actualizar automáticamente.

## Por qué esto y no Watchtower

Watchtower actualiza solo, sin avisar — un update malo en un servicio crítico (base de datos, Vaultwarden) puede arruinar todo sin que te enteres a tiempo. Diun solo notifica; la decisión de actualizar sigue siendo manual.

## Disciplina asociada

- Fijar versiones (`imagen:1.2`, nunca `imagen:latest`) en todo lo crítico.
- Actualizar con `docker compose pull && docker compose up -d` a mano, leyendo el changelog antes.

## Ver también

- [[Arquitectura General]]
- [[Registro de Decisiones]]
