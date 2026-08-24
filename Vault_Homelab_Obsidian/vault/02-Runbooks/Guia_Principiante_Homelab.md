# Guía para principiantes absolutos: tu primer homelab

*"Like a virgen" — cero suposiciones, todo explicado.*

---

## 0. Antes de tocar nada: el diccionario básico

Vas a ver estas palabras un millón de veces. Aquí están explicadas como si nunca las hubieras escuchado:

| Palabra | Qué es, en cristiano |
|---|---|
| **VPS** | Una computadora que rentas en internet (eso es tu Contabo). No es tuya físicamente, vive en un centro de datos. |
| **Homelab** | Tus propias computadoras, en tu casa, haciendo lo que antes hacía el VPS o un SaaS que pagabas. |
| **Docker** | Un programa que mete cada aplicación en su propia "cajita" aislada (contenedor), para que no se peleen entre sí ni ensucien tu sistema. |
| **Contenedor** | Una de esas cajitas. Un contenedor = una app corriendo (ej: un contenedor de n8n, otro de Vaultwarden). |
| **Imagen** | La "receta" que Docker usa para crear un contenedor. Se descarga de internet (Docker Hub). |
| **docker-compose.yml** | Un archivo de texto que le dice a Docker qué contenedores levantar y cómo conectarlos. Es literalmente una receta de cocina en texto. |
| **Puerto** | Una "puerta numerada" por la que una app recibe conexiones. Ej: n8n usa el puerto 5678 por defecto. |
| **Dominio** | Tu nombre en internet (ej: tudominio.com). Lo compraste en Hostinger. |
| **Subdominio** | Una "sección" de tu dominio, ej: `n8n.tudominio.com` o `vault.tudominio.com`. Puedes tener decenas gratis. |
| **DNS** | La "libreta de contactos" de internet: traduce `tudominio.com` a una dirección IP real. |
| **Nameservers** | Quién controla esa libreta de contactos. Ahora mismo probablemente los controla Hostinger. |
| **IP fija / reserva DHCP** | Que un dispositivo en tu red SIEMPRE tenga la misma dirección local (ej: 192.168.1.11), para no perderlo. |
| **SSH** | Cómo te conectas por terminal a una computadora remota (tu Pi, tu VPS) para darle comandos sin necesitar teclado/pantalla propios. |
| **Reverse proxy** | Un "recepcionista" que recibe todas las peticiones web y las reparte al contenedor correcto según el subdominio. |
| **Cloudflare Tunnel** | Una forma de exponer tus servicios de casa a internet SIN abrir puertos en tu router (más seguro). |

No necesitas memorizar esto. Vuelve aquí cuando te pierdas.

---

## 1. Tu situación actual (y por qué está bien como está)

Ahora mismo tienes:
- **n8n corriendo en Contabo** (tu VPS) — funcionando, no lo vamos a tocar todavía.
- **Dominio en Hostinger** — donde compraste `tudominio.com` y ahí vive la configuración de DNS que apunta a Contabo.

**Esto se queda exactamente igual por ahora.** Vamos a construir tu homelab en casa como algo *adicional*, no como un reemplazo inmediato. Cuando todo esté sólido y probado, ahí decides si algún día quieres migrar n8n a tu Pi local — pero eso es opcional y para mucho más adelante.

### ¿Por qué no migrar n8n ya mismo?

Porque quieres aprender esto por primera vez, y mezclar "estoy aprendiendo Docker" con "no puedo tocar esto porque mis clientes/flujos dependen de que funcione" es la receta perfecta para el estrés. Practica en las Pi primero con servicios que no importan si se caen, y cuando ya domines el proceso, ahí migras lo importante con calma.

---

## 2. El plan de esta semana (nada más, no pienses en las 3 Pi todavía)

Objetivo único: **una Pi funcionando con Docker y tu primer contenedor arriba.** Eso es todo. Nada de NAS, nada de n8n nuevo, nada de túneles.

### Día 1 — Conectarte a tu Pi

Ya sabes hacer esto (lo hicimos juntos con la primera Pi). Abre tu terminal (PuTTY, o la terminal de Mac/Linux) y conéctate:

```bash
ssh pi4gb_1@192.168.1.165
```

(usa el usuario e IP reales de tu Pi — ajusta según lo que tengas)

### Día 1 — Instalar Docker (copia y pega, línea por línea, revisando que cada una termine bien antes de la siguiente)

```bash
sudo apt update && sudo apt upgrade -y
```

Espera a que termine (puede tardar varios minutos). Luego:

```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
```

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
sudo apt update
```

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```bash
sudo usermod -aG docker $USER
```

**Ahora cierra la sesión SSH por completo y vuelve a conectarte** (esto es obligatorio, si no, el siguiente paso falla):

```bash
exit
```

Y vuelve a entrar:

```bash
ssh pi4gb_1@192.168.1.165
```

### Día 1 — Verificar que funcionó

```bash
docker --version
```

Debe mostrarte un número de versión (ej: `Docker version 27.x.x`). Si sale error, dime exactamente qué dice y lo resolvemos.

```bash
docker run --rm hello-world
```

Si ves un mensaje que empieza con `Hello from Docker!`, **ya tienes Docker funcionando**. Este es tu primer logro real — tómate un café.

---

### Día 2 — Tu primer contenedor de verdad (Homepage, un dashboard simple)

Vamos con algo visual y satisfactorio: un dashboard que se ve bonito y no puede romper nada importante.

**Crea una carpeta para el proyecto** (recuerda: una carpeta por servicio, siempre):

```bash
mkdir -p ~/homelab/homepage
cd ~/homelab/homepage
```

**Crea el archivo de configuración** (esto es la "receta" de la que hablamos):

```bash
nano docker-compose.yml
```

Se abre un editor de texto en la terminal. Pega esto (clic derecho → pegar, o `Ctrl+Shift+V` según tu terminal):

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    restart: unless-stopped
    ports:
      - "3000:3000"
```

Guarda y sal: `Ctrl+O`, luego `Enter`, luego `Ctrl+X`.

**Levántalo:**

```bash
docker compose up -d
```

Este comando descarga la imagen (tarda un poco la primera vez) y prende el contenedor.

**Verifica que está corriendo:**

```bash
docker ps
```

Deberías ver una línea con `homepage` y `Up X seconds`.

**Ábrelo en tu navegador** (desde tu computadora, no desde la Pi):

```
http://192.168.1.165:3000
```

(usa la IP real de tu Pi)

Si ves una pantalla de bienvenida de Homepage — **felicidades, acabas de levantar tu primer servicio self-hosted.**

---

## 3. Comandos que vas a usar todo el tiempo (tu chuleta)

```bash
docker ps                      # Ver qué contenedores están corriendo
docker compose up -d           # Levantar los servicios de la carpeta actual
docker compose down            # Apagar los servicios de la carpeta actual
docker compose logs -f         # Ver qué está pasando en tiempo real (Ctrl+C para salir)
docker compose restart         # Reiniciar los servicios
```

**Regla de oro:** siempre corre estos comandos parado DENTRO de la carpeta del servicio que quieres controlar (`cd ~/homelab/homepage` antes de `docker compose down`, por ejemplo).

---

## 4. Qué sigue (roadmap sin apuro, un servicio a la vez)

No hagas todo esto en un día. Un servicio nuevo cada 2-3 días, para que realmente entiendas cada uno antes de sumar el siguiente.

1. ✅ Docker instalado
2. ✅ Homepage (dashboard)
3. **Vaultwarden** (gestor de contraseñas) — el siguiente paso natural, mismo patrón que Homepage
4. **AdGuard Home** (DNS + bloqueo de anuncios en toda tu red)
5. **Portainer** (una interfaz visual para administrar Docker sin escribir comandos — te va a encantar una vez que ya entiendas lo básico)
6. Recién ahí: Cloudflare Tunnel, para exponer algo a internet de forma segura
7. Recién ahí: pensamos en n8n local, si decides que quieres migrarlo

## 5. Tu próximo servicio: Vaultwarden (cuando estés listo)

Mismo patrón exacto que Homepage:

```bash
mkdir -p ~/homelab/vaultwarden
cd ~/homelab/vaultwarden
nano docker-compose.yml
```

```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      SIGNUPS_ALLOWED: "true"
    volumes:
      - ./data:/data
    ports:
      - "8080:80"
```

```bash
docker compose up -d
```

Ábrelo en `http://192.168.1.165:8080` y crea tu primera cuenta.

> Nota: dejé `SIGNUPS_ALLOWED: "true"` para que puedas crear tu cuenta la primera vez. Una vez tengas tu cuenta creada, cámbialo a `"false"` y corre `docker compose up -d` de nuevo para que nadie más pueda crear cuentas.

---

## 6. Sobre Hostinger y Contabo — qué va a pasar más adelante (solo para que lo tengas en el radar)

Cuando llegues al paso de Cloudflare Tunnel (semana 2-3, no ahora), lo que vas a hacer es:

1. Crear cuenta gratis en Cloudflare.
2. Cambiar los **nameservers** de tu dominio (en el panel de Hostinger) para que apunten a Cloudflare en vez de a Hostinger.
3. **Esto NO rompe tu n8n de Contabo** — vas a recrear el mismo registro DNS que apunta a Contabo, ahora dentro de Cloudflare, y va a seguir funcionando exactamente igual.
4. Vas a agregar registros NUEVOS (subdominios nuevos) que apunten a tu túnel de casa — esos son los que van a servir Vaultwarden, Homepage, etc.

Es decir: nada se rompe, solo cambias quién controla la libreta de contactos (de Hostinger a Cloudflare), y le sumas páginas nuevas a esa libreta.

**No hagas esto todavía.** Cuando llegues a ese punto, avísame y lo hacemos juntos paso a paso, con capturas de pantalla como hicimos con la red.

---

## 7. Si algo sale mal (y algo va a salir mal, es normal)

- **Copia el error exacto** (captura de pantalla, como has hecho hasta ahora) y mándamelo.
- No borres nada por miedo — casi todo se puede diagnosticar y arreglar.
- `docker compose logs -f` es tu mejor amigo para saber qué está pasando dentro de un contenedor que no arranca.
- Nunca vas a romper tu n8n de Contabo tocando tu Pi — están completamente separados, en máquinas distintas.

---

## Resumen de hoy mismo, sin scroll

1. `ssh` a tu Pi
2. Instalar Docker (bloque de 9 comandos de arriba)
3. `docker run --rm hello-world` para confirmar
4. Crear carpeta + `docker-compose.yml` de Homepage
5. `docker compose up -d`
6. Abrir `http://TU_IP:3000` en el navegador

Eso es literalmente todo lo que necesitas hacer hoy. Cuando lo tengas, mándame captura y seguimos con Vaultwarden.
