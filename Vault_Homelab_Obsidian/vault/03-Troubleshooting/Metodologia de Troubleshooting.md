---
tags: [homelab, troubleshooting, metodologia]
---

# Metodología de troubleshooting

Cuando algo no funciona, seguir este orden — de abajo hacia arriba, capa por capa. Nunca saltar pasos.

## 1. ¿Hay conexión física?
```bash
ip link show <interfaz>
```
Buscar `state UP`. Si no hay luz en el puerto o dice `DOWN`, es un problema de cable/switch.

## 2. ¿Hay una IP asignada?
```bash
ip addr show <interfaz>
```
Buscar `inet 192.168.x.x`. Si aparece `169.254.x.x`, no hay DHCP funcionando — el dispositivo se autoasignó una IP link-local.

## 3. ¿El servicio de red está corriendo bien?
```bash
nmcli device status
systemctl status <servicio>
```

## 4. ¿Hay conectividad real a internet?
```bash
ping -c 4 8.8.8.8      # prueba solo la red
ping -c 4 google.com    # prueba también DNS
```

## 5. ¿El contenedor/app específica está corriendo?
```bash
docker ps
docker compose logs -f
```

## 6. ¿El servicio responde en su puerto?
```bash
curl http://localhost:PUERTO
```

## Regla de oro

Nunca saltar pasos. Empezar siempre en el paso 1, aunque se esté seguro de que el cable está bien — verificar de abajo hacia arriba ahorra tiempo, no lo contrario.

## Ver también

- [[Incidente - LAN sin internet Pi 1]]
