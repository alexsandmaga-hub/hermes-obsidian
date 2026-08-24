# Manual: Instalar el Sistema Operativo en NVMe (M.2) — Raspberry Pi 5 + S2Pi EP-0241

Guía completa desde cero hasta tener la Raspberry Pi 5 booteando su sistema operativo desde el SSD M.2 NVMe montado en el HAT S2Pi P33 (M.2 NVMe M-key & PoE+ HAT, modelo EP-0241).

---

## 0. Antes de empezar

**Necesitas:**
- Raspberry Pi 5
- HAT S2Pi EP-0241 (PoE+ + M.2 NVMe M-key)
- SSD M.2 NVMe compatible (2230 / 2242 / 2260 / 2280 — **no** SATA M.2)
- Cable FFC PCIe de 40mm (incluido con el HAT)
- Una tarjeta microSD con Raspberry Pi OS (temporalmente, para el primer arranque y la configuración)
- Fuente USB-C oficial de Pi 5 (o un HAT PoE+ ya conectado — pero no ambos a la vez)
- PC con lector de tarjetas SD para grabar la imagen inicial

**Importante:** la Raspberry Pi 5 necesita arrancar primero desde microSD para configurar el EEPROM y habilitar el boot desde NVMe. Una vez configurado, puedes prescindir de la SD.

---

## 1. Montaje físico del HAT

1. Apaga la Pi y desconecta toda alimentación.
2. Inserta el SSD M.2 NVMe en el slot M-key del HAT y atorníllalo en el punto de montaje correspondiente a su tamaño (2230/2242/2260/2280).
3. Conecta el cable FFC PCIe de 40mm entre el conector PCIe del HAT y el conector PCIe de la Raspberry Pi 5 (junto al puerto USB-C). Verifica bien la orientación de los contactos — el manual del fabricante marca claramente el lado correcto.
4. Monta el HAT sobre la Pi usando los pilares de cobre M2.5.
5. Si vas a usar PoE: conecta el cable Ethernet a un switch/inyector 802.3af/at compatible. **No conectes el USB-C si el PoE está alimentando la placa** — puede dañar el equipo.
6. Para la primera configuración, te recomiendo alimentar por USB-C normal (sin PoE todavía) hasta confirmar que el NVMe bootea bien.

---

## 2. Preparar la microSD con Raspberry Pi OS

1. En tu PC, descarga e instala **Raspberry Pi Imager**: https://www.raspberrypi.com/software/
2. Graba Raspberry Pi OS (64-bit, versión recomendada) en la microSD.
3. En las opciones avanzadas del Imager (icono de engranaje ⚙️), configura de una vez:
   - Hostname
   - Usuario y contraseña
   - Wi-Fi (si lo necesitas)
   - Habilitar SSH (útil para no necesitar teclado/monitor)
4. Inserta la microSD en la Pi y enciende.

---

## 3. Actualizar el sistema y el firmware/EEPROM

Con la Pi arrancada desde la microSD:

```bash
sudo apt update && sudo apt full-upgrade -y
sudo rpi-eeprom-update
```

Si indica que hay una actualización de firmware disponible:

```bash
sudo rpi-eeprom-update -a
sudo reboot
```

---

## 4. Habilitar PCIe

Edita el archivo de configuración de arranque:

```bash
sudo nano /boot/firmware/config.txt
```

Agrega al final:

```
dtparam=pciex1
```

(Opcional) Si tu SSD y cable soportan Gen 3.0 de forma estable, puedes forzarlo agregando una línea adicional:

```
dtparam=pciex1_gen=3
```

> Por defecto la conexión certifica a Gen 2.0 (5 GT/s). Gen 3.0 (10 GT/s) funciona en la mayoría de los casos, pero pruébalo — si tienes errores o inestabilidad, quita esa línea.

Guarda (`Ctrl+O`, `Enter`) y sal (`Ctrl+X`).

---

## 5. Habilitar detección PCIe y arranque desde NVMe en el EEPROM

```bash
sudo rpi-eeprom-config --edit
```

Agrega o modifica estas líneas:

```
PCIE_PROBE=1
BOOT_ORDER=0xf416
```

> El `6` en `BOOT_ORDER` habilita el arranque desde NVMe. El orden completo define la secuencia de dispositivos que la Pi intenta al bootear.

Guarda y sal. Reinicia:

```bash
sudo reboot
```

---

## 6. Verificar que el SSD NVMe es detectado

Después del reinicio:

```bash
lsblk
lspci -vvv
```

Deberías ver el dispositivo, típicamente como `/dev/nvme0n1`. Si `lspci` no muestra nada, revisa el cable FFC (orientación/asiento) y que el paso 4 se guardó correctamente.

---

## 7. Particionar y formatear el NVMe

```bash
sudo fdisk /dev/nvme0n1
```

Dentro de `fdisk`, en este orden:

```
p        (muestra la tabla actual)
n        (nueva partición)
p        (partición primaria)
1        (número de partición)
Enter    (primer sector, por defecto)
Enter    (último sector, por defecto = usa todo el disco)
w        (escribe los cambios y sale)
```

Formatea la partición:

```bash
sudo mkfs.ext4 /dev/nvme0n1p1
```

---

## 8. Clonar el sistema de la microSD al NVMe (opción recomendada)

En lugar de reinstalar todo desde cero, la forma más simple es clonar el sistema ya configurado de la SD al NVMe con **rpi-clone**:

```bash
sudo apt install -y git
git clone https://github.com/geerlingguy/rpi-clone.git
cd rpi-clone
sudo cp rpi-clone rpi-clone-setup /usr/local/sbin
sudo rpi-clone nvme0n1
```

Sigue las instrucciones en pantalla (confirma el destino con `Enter`/`yes` cuando te lo pida). Esto copia el sistema completo, incluyendo el particionado boot/root correcto, al NVMe.

### Alternativa: instalación limpia directa en el NVMe

Si prefieres una instalación nueva en vez de clonar:

1. Apaga la Pi, retira la microSD y conéctala a tu PC.
2. Usa **Raspberry Pi Imager** para grabar el sistema operativo directamente en el SSD NVMe (conectado a tu PC vía un adaptador USB-NVMe externo), configurando usuario/Wi-Fi/SSH igual que en el paso 2.
3. Vuelve a montar el NVMe en el HAT de la Pi.

---

## 9. Configurar el orden de arranque para priorizar NVMe

Si clonaste con `rpi-clone`, el `BOOT_ORDER=0xf416` del paso 5 ya prioriza NVMe sobre SD. Para comprobar:

```bash
vcgencmd bootloader_config
```

Verifica que `BOOT_ORDER` incluya el `6` (NVMe) antes que `1` (SD).

---

## 10. Arrancar sin la microSD

1. Apaga la Pi.
2. Retira la tarjeta microSD.
3. Enciende. La Pi debería arrancar directamente desde el NVMe.

Confirma que estás corriendo desde el NVMe:

```bash
lsblk -o NAME,MOUNTPOINT,SIZE,MODEL
df -h /
```

`/` (raíz) debe apuntar a `/dev/nvme0n1p2` (o similar), no a `/dev/mmcblk0`.

---

## 11. (Opcional) Montar un segundo NVMe o partición de datos adicional

Si quieres usar un espacio adicional del NVMe como almacenamiento de datos (no como sistema):

```bash
sudo fdisk /dev/nvme0n1     # crea partición adicional si aplica
sudo mkfs.ext4 /dev/nvme0n1p1
mkdir ~/mydata
sudo mount -t ext4 /dev/nvme0n1p1 /home/pi/mydata -v
```

Para automontaje persistente:

```bash
sudo vim.tiny /etc/fstab
```

Agrega:

```
/dev/nvme0n1p1  /home/pi/mydata  ext4  defaults,noatime  0 0
```

Guarda, y prueba **sin reiniciar todavía**:

```bash
sudo mount -a
df -Th
```

Confirma que aparece montado en `/home/pi/mydata`. **Si el fstab está mal escrito y reinicias, la Pi puede no arrancar.** Verifica antes de reiniciar.

---

## 12. Activar PoE (una vez que el NVMe ya bootea bien)

1. Apaga la Pi y desconecta el USB-C por completo.
2. Conecta el cable Ethernet a un switch/inyector 802.3af/at compatible.
3. Enciende — la Pi debería alimentarse solo por el cable de red (5.1V/4.5A vía el header PoE de 4 pines del HAT).
4. **Nunca conectes el USB-C mientras el PoE está en uso** — el fabricante advierte que esto puede dañar el equipo.

---

## Resolución de problemas comunes

| Síntoma | Posible causa | Solución |
|---|---|---|
| `lspci` no detecta el SSD | Cable FFC mal asentado o al revés | Revisa orientación del cable, reasienta con cuidado |
| No arranca desde NVMe | `BOOT_ORDER` no configurado o EEPROM desactualizado | Repite pasos 3 y 5, verifica con `vcgencmd bootloader_config` |
| Sistema inestable en Gen 3.0 | Cable/SSD no soporta esa velocidad de forma confiable | Quita `dtparam=pciex1_gen=3` y usa Gen 2.0 |
| No bootea tras editar `/etc/fstab` | Ruta o UUID incorrectos | Arranca desde microSD, monta el NVMe manualmente y corrige `/etc/fstab` |
| Pi no enciende con PoE | Switch/inyector no es 802.3af/at, o cable Ethernet de mala calidad | Verifica el estándar del switch y usa Cat5e/Cat6 en buen estado |

---

## Referencia rápida de comandos

```bash
# Actualizar sistema y firmware
sudo apt update && sudo apt full-upgrade -y
sudo rpi-eeprom-update -a

# Habilitar PCIe (config.txt)
dtparam=pciex1

# Habilitar boot NVMe (EEPROM)
PCIE_PROBE=1
BOOT_ORDER=0xf416

# Clonar SD -> NVMe
sudo rpi-clone nvme0n1

# Verificar
lsblk
lspci -vvv
vcgencmd bootloader_config
```

**Más información del HAT:** https://wiki.52pi.com/index.php?title=EP-0241
