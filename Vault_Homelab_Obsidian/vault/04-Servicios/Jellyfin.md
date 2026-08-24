---
tags: [homelab, servicio, multimedia]
---

# Jellyfin (Netflix local)

**Nodo:** MSI Cubi NUC AI+ — aprovecha el Arc 140V para transcodificación por hardware (incluye AV1).
**Almacenamiento:** librería de películas/series vive en NAS DS723+, montada por NFS/SMB hacia el NUC.

## Por qué en el NUC y no en el Mac Mini o el NAS

El NUC tiene la mejor GPU integrada del homelab para transcodificación de video — el Mac Mini se reserva para IA (Ollama), y el NAS no tiene GPU para esto.

## Ver también

- [[Arquitectura General]]
- [[Plan de Backups]]
