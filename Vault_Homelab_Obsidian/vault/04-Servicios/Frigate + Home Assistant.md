---
tags: [homelab, servicio, seguridad, camaras]
---

# Frigate + Home Assistant

**Nodo:** Pi 5 #4 (sin NVMe — libera el único puerto PCIe para el AI HAT)
**Acelerador:** AI HAT+ 13 TOPS (Hailo-8L) — suficiente para Frigate con varias cámaras
**Cámaras:** Hikvision (soporte RTSP nativo completo — compatible)
**Archivo de video:** Drobo (clips más viejos, separado del NAS principal)

## Por qué no NVMe en esta Pi

La Raspberry Pi 5 solo tiene un conector PCIe físico. El HAT S2Pi (NVMe+PoE) y el AI HAT compiten por el mismo puerto — se eligió el AI HAT para esta Pi específica, usando microSD o SSD por USB para el sistema operativo en su lugar.

## URL RTSP típica de Hikvision

```
rtsp://usuario:contraseña@IP_DE_LA_CAMARA:554/Streaming/Channels/101
```
- Canal `101` = stream principal (alta resolución, para grabación)
- Canal `102` = substream (más liviano, recomendado para detección continua)

## Blink — por qué NO entra a Frigate

Blink no ofrece RTSP ni streaming en vivo nativo. Existe un bridge de la comunidad que simula RTSP a partir de clips descargados de la nube de Blink, pero tiene ~30s de delay y sigue dependiendo de la nube — no vale la pena para detección en tiempo real. Blink se integra a Home Assistant solo para notificaciones/estado vía su integración oficial en la nube.

## Ver también

- [[Arquitectura General]]
- [[Plan de Backups]]
