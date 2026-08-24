---
tags: [homelab, servicio, seguridad]
---

# Vaultwarden

**Nodo:** Pi 5 #1 (8GB)
**Rol:** Gestor de contraseñas — servicio crítico, siempre encendido.

## docker-compose.yml

```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      SIGNUPS_ALLOWED: "false"   # cambiar a "true" solo al crear la primera cuenta
    volumes:
      - ./data:/data
    ports:
      - "8080:80"
```

## Checklist de seguridad

- [ ] `SIGNUPS_ALLOWED` en `false` después de crear la cuenta inicial
- [ ] Backup del volumen `./data` incluido en el job de configs críticas hacia el DS214
- [ ] Expuesto solo vía Cloudflare Tunnel, nunca puerto abierto directo

## Ver también

- [[Arquitectura General]]
- [[Plan de Backups]]
