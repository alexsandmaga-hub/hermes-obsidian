---
tags: [homelab, troubleshooting, incidente, resuelto]
---

# Incidente: Pi #1 sin internet por LAN

**Estado:** ✅ Resuelto
**Nodo afectado:** Pi 5 #1 (8GB)

## Síntoma

Después de montar el HAT S2Pi con PoE, la Pi encendía y tenía luz de link en el puerto, pero no había internet por el cable de red — solo funcionaba por Wi-Fi.

## Diagnóstico paso a paso

1. `ip link show eth0` → `state UP` — el link físico estaba bien.
2. `ip addr show eth0` → solo mostraba una IP `inet6 fe80::...` (link-local IPv6), sin ninguna `inet 192.168.x.x`.
3. Se probó `dhclient` → no estaba instalado (Raspberry Pi OS moderno usa NetworkManager, no dhcpcd/dhclient por defecto).
4. `nmcli device status` → confirmó que el sistema usa NetworkManager.
5. `ip addr show eth0` mostró en un momento `inet 169.254.26.231/16` — dirección IPv4LL (autoasignada), confirmando que el DHCP no estaba respondiendo a tiempo.
6. Se revisó el switch (UniFi USW Flex 2.5G 8 PoE) vía su interfaz web — el puerto 1 mostraba PoE++ entregado, link a GbE, pero "IP Address: Unknown" y "24H Internet Activity: 0 B", mientras otros puertos sí mostraban tráfico normal. Esto confirmó que el switch/red estaban bien — el problema era específico de la negociación DHCP de esa Pi.
7. Se forzó una reconexión: `sudo nmcli connection up "Wired connection 1"`.
8. Tras esto, `nmcli connection show "Wired connection 1"` mostró `GENERAL.STATE: activated` con `IP4.ADDRESS[1]: 192.168.1.165/24` — IP real asignada por DHCP.
9. Confirmado con `ping -c 4 8.8.8.8` y `ping -c 4 google.com` — 0% de pérdida en ambos.

## Causa raíz

Negociación DHCP lenta en la primera conexión del puerto — probablemente relacionada con el switch tardando unos segundos extra en negociar PoE y el link de datos al mismo tiempo la primera vez. El comando `nmcli connection up` forzó una nueva solicitud que sí completó a tiempo.

## Lección para la próxima Pi

Si al conectar por PoE no aparece IP real de inmediato, no asumir que es un problema de cableado o del switch — primero forzar `nmcli connection up "Wired connection 1"` y volver a revisar antes de sospechar de hardware.

## Ver también

- [[Metodologia de Troubleshooting]]
- [[Manual Instalacion OS NVMe Pi5]]
