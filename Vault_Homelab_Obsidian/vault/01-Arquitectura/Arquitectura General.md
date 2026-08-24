---
tags: [homelab, arquitectura]
---

# Arquitectura General

![[arquitectura.png]]

## Inventario de hardware

| Nodo | Specs | Rol | Switch |
|---|---|---|---|
| Mac Mini | 32GB RAM, 512GB SSD | Agentes de IA, Ollama/Open WebUI, Nextcloud | QNAP QSW-L2110-10T |
| PC personal | — | Cliente | QNAP QSW-L2110-10T |
| MSI Cubi NUC AI+ | Core Ultra 9 288V, 32GB, Arc 140V, dual 2.5G LAN | Firewall/router (pfSense/OPNsense) + Jellyfin/Plex | QNAP QSW-L2110-10T |
| ThinkCentre M920q | i7/i9 8va-9na gen, hasta 64GB RAM, NIC I219-LM | Proxmox — VMs de staging, "VPS local" | QNAP QSW-L2110-10T |
| Pi 5 #1 | 8GB, S2Pi EP-0241 (PoE+NVMe 512GB) | DNS (AdGuard) + Vaultwarden + Cloudflare Tunnel | UniFi PoE |
| Pi 5 #2 | 16GB, S2Pi EP-0241 (PoE+NVMe 512GB) | n8n + Postgres | UniFi PoE |
| Pi 5 #3 | 16GB, S2Pi EP-0241 (PoE+NVMe 512GB) | Monitoreo (Homepage, Beszel) | UniFi PoE |
| Pi 5 #4 | Sin NVMe (libera PCIe) + AI HAT+ 13 TOPS | Home Assistant + Frigate NVR | UniFi PoE |
| NAS Synology DS723+ | 2 bahías, RAID 1, DSM 7 | Primario — Nextcloud, Jellyfin, Fotos, Docker volumes, docs | — |
| NAS Synology DS214 | 2 bahías, ARM antiguo, DSM 6 | Backup vía Hyper Backup (fotos + configs críticas) | — |
| Drobo | BeyondRAID (propietario, empresa cerrada) | Archivo frío de video de Frigate | — |
| Contabo VPS | — | n8n actual + futura tienda pública | Internet |
| Hostinger | — | Dominio (DNS) | Internet |
| Cámaras Hikvision | RTSP nativo | Fuente de video para Frigate | Red local |
| Cámaras Blink | Solo nube, sin RTSP | Integración HA vía nube (notificaciones/estado, no Frigate) | Internet |

## Por qué roles fijos y no cluster homogéneo

El Mac Mini tiene mucha más potencia que cualquier Pi — un cluster tipo k3s trataría a todos los nodos como iguales y desperdiciaría esa ventaja. Repartir cargas según la fuerza real de cada equipo es más eficiente, y da resiliencia: si el Mac se cae, DNS/red/backups siguen vivos en las Pi.

## Topología de red

```
                    Internet (2.5Gb)
                          │
                   ┌──────┴──────┐
                   │   Router    │
                   └──────┬──────┘
                          │
              ┌───────────┴────────────┐
              │                        │
      QNAP QSW-L2110-10T        UniFi PoE Switch
      (10G / 2.5G)              (PoE, para las Pi)
       │     │      │      │      │    │    │    │
   Mac Mini  PC   MSI Cubi M920q Pi #1 Pi #2 Pi #3 Pi #4
   (IA)   personal  NUC  (Proxmox)(DNS)(n8n)(mon)(HA/Frigate)
              │                    │
          NAS #1                NAS #2
        (Primario)              (Réplica)
```

## Ver también

- [[Manual Instalacion OS NVMe Pi5]]
- [[Plan de Backups]]
- [[Metodologia de Troubleshooting]]
