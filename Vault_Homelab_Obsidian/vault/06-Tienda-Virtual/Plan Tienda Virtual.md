---
tags: [homelab, ecommerce, tienda]
---

# Plan de Tienda Virtual

## Decisión clave (no negociable)

**La tienda pública vive en Contabo (VPS), no en las Raspberry Pi de casa.**

Razones:
- Uptime — el internet residencial se puede caer.
- IP fija real — un VPS tiene IP pública dedicada.
- Seguridad/cumplimiento — PCI-DSS es más fácil de cumplir en infraestructura profesional.
- Ya está funcionando ahí (n8n ya corre en Contabo).

## Lo que sí va en el homelab

- [[n8n]] orquestando: nuevo pedido → actualizar inventario → notificar → generar factura
- Base de datos de analítica/backups replicada hacia los NAS
- Dashboards internos (Homepage/Grafana) — no públicos

## Plataforma de tienda — opciones evaluadas

| Opción | Cuándo tiene sentido |
|---|---|
| WooCommerce (WordPress) | Rápido de montar, mucha documentación en español |
| Medusa.js | Headless, conectable con n8n vía API sin plugins intermedios |
| Saleor | Similar a Medusa, más robusto, curva mayor |
| Shopify (SaaS) | Simplicidad total, sin mantener servidores propios |

**Recomendación inicial:** WooCommerce si se busca velocidad; Medusa.js si el perfil es más técnico.

## Flujo (una vez montado)

```
Cliente compra en tudominio.com (Contabo)
        │ webhook
        v
n8n (Contabo)
        │
        ├── Actualiza inventario
        ├── Notifica por Telegram/correo
        └── Genera registro en base de datos local
        v
Backup automático hacia NAS Synology
```

## Ver también

- [[Arquitectura General]]
- [[n8n]]
