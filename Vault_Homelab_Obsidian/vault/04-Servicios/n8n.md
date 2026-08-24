---
tags: [homelab, servicio, n8n]
---

# n8n

**Nodo:** Pi 5 #2 (16GB) — futuro. Actualmente vive en Contabo, sin planes inmediatos de migrar.
**Rol:** Automatizaciones — inventario, notificaciones, webhooks de la tienda virtual.

## Estado actual

- Corriendo en Contabo (VPS), conectado al dominio de Hostinger.
- **No tocar hasta que el homelab esté sólido** — decisión explícita de no mezclar aprendizaje con producción.

## Plan de acceso remoto (cuando se monte localmente)

Ver [[Arquitectura General]] — acceso vía Cloudflare Tunnel + Cloudflare Access como capa extra de login, dado que n8n maneja credenciales sensibles de APIs.

## docker-compose.yml base (referencia futura)

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
    volumes:
      - ./data:/home/node/.n8n
    depends_on:
      - postgres
  postgres:
    image: postgres:16
    restart: unless-stopped
    environment:
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=CAMBIAR_ESTO
      - POSTGRES_DB=n8n
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
```

## Ver también

- [[Plan Tienda Virtual]]
- [[Arquitectura General]]
