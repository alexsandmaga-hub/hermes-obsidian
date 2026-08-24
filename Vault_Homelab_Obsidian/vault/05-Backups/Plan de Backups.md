---
tags: [homelab, backups]
---

# Plan de Backups (regla 3-2-1)

## Arquitectura de storage

```
DS723+ (RAID 1, primario — activo)
  ├── Fotos (Synology Photos) ──── Hyper Backup → DS214 (copia #2, suficiente)
  ├── Nextcloud
  ├── Librería Jellyfin
  ├── Volúmenes Docker (Pi's)         ← solo protegido por RAID 1, sin copia externa (decisión aceptada)
  └── homelab-docs/ (bóveda Obsidian) ── Hyper Backup → DS214 (liviano, casi gratis)

Drobo → archivo frío de video de Frigate (cámaras Hikvision), fuera del flujo de backup automático
```

## Por qué Hyper Backup y no Snapshot Replication

El DS214 es un modelo antiguo (ARM, ~2013) que probablemente no soporta Btrfs — Snapshot Replication requiere Btrfs en ambos extremos. Hyper Backup funciona con ext4 sin problema y logra el mismo resultado práctico.

## Importante: RAID 1 no es backup

El RAID 1 del DS723+ protege contra falla de un disco físico, pero NO contra ransomware, borrado accidental, falla del controlador, o desastre físico en la casa (incendio/inundación/robo) — en esos casos se pierden ambas copias del RAID a la vez, porque siguen siendo la misma caja física.

## Decisiones tomadas

- Fotos: 2 copias (DS723+ + DS214) — suficiente, no se usa el Drobo para esto.
- Configs críticas (Vaultwarden, docker-compose.yml, workflows de n8n, bóveda de Obsidian): incluidas en el job liviano hacia el DS214.
- Volúmenes Docker de los servicios (Jellyfin metadata, etc.): solo RAID 1, sin copia externa — riesgo aceptado explícitamente porque es reemplazable.

## Ver también

- [[Arquitectura General]]
- [[Synology Photos]]
