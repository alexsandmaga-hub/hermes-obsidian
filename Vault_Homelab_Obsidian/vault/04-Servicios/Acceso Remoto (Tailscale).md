---
tags: [homelab, servicio, red, acceso-remoto]
---

# Acceso Remoto (Tailscale)

**Nodo:** Pi #1 (siempre encendido, ya es el nodo de red/DNS)
**Método:** Subnet router — un solo punto de entrada da acceso a toda la red de casa, sin instalar Tailscale en cada equipo.

## Por qué subnet router y no exponer cada servicio individualmente

Proxmox, el panel del NAS, y otros paneles administrativos son demasiado sensibles para exponer vía Cloudflare Tunnel (a diferencia de Vaultwarden/n8n, que sí están pensados para acceso público). Un VPN que da acceso a toda la LAN resuelve esto de una sola vez, para todo, sin exponer nada directo a internet.

## Setup

```bash
curl -fsSL https://tailscale.com/install.sh | sh

echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

sudo tailscale up --advertise-routes=192.168.1.0/24
```

Luego aprobar la ruta en [login.tailscale.com/admin/machines](https://login.tailscale.com/admin/machines).

## Uso

Con la app de Tailscale instalada en el celular/laptop de viaje, cualquier IP de `192.168.1.x` es accesible directamente — Proxmox (`:8006`), Homepage, DSM del NAS, lo que sea, exactamente como si estuvieras en casa.

## Ver también

- [[Arquitectura General]]
- [[Registro de Decisiones]]
