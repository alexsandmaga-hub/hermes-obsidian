# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a codebase** — it's a documentation project with two parts:

1. A step-by-step Spanish-language guide for wiring together **Obsidian** (notes), **Hermes Agent** (autonomous agent), and **Claude** (LLM) into a personal "second brain" that gives persistent memory across conversations.
2. An actual **Obsidian vault** (`Vault_Homelab_Obsidian/vault/`) that uses this setup to document the user's real homelab — hardware, services, runbooks, and architecture decisions.

There is no build, lint, or test tooling. Everything is Markdown content edited directly; "correctness" here means factual accuracy and consistency with the vault's existing structure and decisions, not passing a check.

## Layout

- `GUIA-COMPLETA-Hermes-Obsidian-Claude.md` — the main guide (14 sections + Apéndice A on NAS setup), written for a beginner with zero technical background.
- `APENDICES-B-C-D-E.md`, `APENDICES-F-G.md`, `APENDICES-H-I.md`, `APENDICES-J-K-L-GLOSARIO.md` — appendices B through L plus a glossary, extending the main guide (templates, plugins, security, cost monitoring, workflows, integrations, Git, migration, Ollama, cheat sheet). `INDICE-APENDICES.md` is the hand-maintained table of contents for these four files — update it if appendix content is added, moved, or renamed.
- `HOMELAB-OBSIDIAN-INTEGRACION.md` — an early analysis/recommendations document for integrating this user's hardware into Obsidian+Hermes. **Partially superseded** — see "Vault storage & sync" below; its Synology Drive Client proposal was not what the vault's own decision log settled on.
- `Vault_Homelab_Obsidian/vault/` — the real Obsidian vault being documented (see full contents condensed below).
- `Vault_Homelab_Obsidian.zip` — a point-in-time snapshot/backup of the vault folder. Treat the unzipped `vault/` folder as the source of truth; don't edit the zip.
- `20260817_114102-Integrate_Obsidian_With_Hermes_And_Claude.md` (and any similarly dated files) — saved chat transcripts/session logs, not maintained reference docs. Read them for history, but don't edit them as if they were guide content.

## Conventions when editing

- Everything is written in Spanish — match that for all guide and vault content.
- Vault notes use YAML frontmatter (`tags: [...]`) and Obsidian `[[Wikilink]]` syntax for cross-references, not standard Markdown links.
- Vault folders are numbered by category (`00-Inicio` … `07-Decisiones`) — keep new notes in the matching numbered folder rather than inventing new top-level folders.
- `07-Decisiones/Registro de Decisiones.md` is a single running ADR log (not one file per decision, despite what the top-level guide's template suggests) — each entry is `## Título` / `**Decisión:**` / `**Por qué:**`. Append new entries in that same format rather than starting a new pattern.
- `vault/00-Inicio/Home.md` is the vault's single entry point (MOC) — if you add a note, service, or vault section, link it from here too.

---

## Homelab reference (condensed from the full vault)

### Hardware, fixed roles, and what runs where

Roles are deliberately **fixed per node, not a homogeneous cluster** (see Decisions below). Full inventory:

| Node | Specs | Role | Services hosted |
|---|---|---|---|
| Mac Mini | 32GB RAM, 512GB SSD | IA / "Jarvis" agents | Ollama/Open WebUI, Nextcloud, SearXNG (private meta-search for the agents) |
| PC personal | — | Client only | — |
| MSI Cubi NUC AI+ | Core Ultra 9 288V, 32GB, Arc 140V, dual 2.5G LAN | Firewall/router + media transcoding (1 M.2 slot, soldered RAM — **not** a second Mac Mini) | pfSense/OPNsense, Jellyfin (hardware transcode incl. AV1 via Arc 140V) |
| ThinkCentre M920q | i7/i9 8th–9th gen, up to 64GB, NIC I219-LM | Proxmox — VMs / "local VPS" | AppFlowy, Cal.com, Cap, Chatwoot, Docuseal, Gitea/Forgejo, Umami/Plausible (chosen over M720q for the I219-LM NIC, which avoids the I219-V's known Proxmox networking bugs, and a higher CPU ceiling) |
| Pi 5 #1 (8GB) | NVMe 512GB via S2Pi EP-0241 HAT, PoE | DNS + secrets + remote access — **operativa** | AdGuard Home (DNS, most critical node in the homelab), Vaultwarden (Cloudflare Tunnel only, never a direct open port), Tailscale subnet router |
| Pi 5 #2 (16GB) | NVMe 512GB, PoE | Automation | n8n + Postgres (local instance, separate from Contabo), Listmonk, Postiz |
| Pi 5 #3 (16GB) | NVMe 512GB, PoE | Monitoring | Homepage, Beszel, Diun (update notifications, no auto-update), Dozzle (container logs via browser) |
| Pi 5 #4 | **No NVMe** (frees the single PCIe port) + AI HAT+ 13 TOPS (Hailo-8L) | Security/home automation | Home Assistant + Frigate NVR |
| NAS Synology DS723+ | 2-bay, RAID 1, DSM 7 | Primary storage | Nextcloud, Jellyfin library, Synology Photos, Docker volumes, `homelab-docs/` (the Obsidian vault) |
| NAS Synology DS214 | 2-bay, old ARM (~2013), DSM 6 | Backup only, via Hyper Backup (no Btrfs → no Snapshot Replication) | Photos copy #2, critical configs, vault backup |
| Drobo | BeyondRAID (proprietary; **vendor closed in 2023** — never store anything critical here) | Frigate cold video archive only | — |
| Contabo VPS | — | Production | n8n (current, production workflows), future public store |
| Hostinger | — | Domain DNS | — |
| Cámaras Hikvision | Native RTSP | Frigate source | `rtsp://user:pass@IP:554/Streaming/Channels/101` (main, recording) / `102` (substream, continuous detection) |
| Cámaras Blink | Cloud-only, no RTSP | HA integration only (never Frigate) | Notifications/state via official cloud integration — a community RTSP bridge exists but has ~30s delay and still depends on the cloud, not worth it |

**fail2ban** runs on every node with SSH reachable (Pis, M920q, MSI Cubi NUC) — standardized everywhere since it's cheap and every exposed SSH is a potential entry point.

### Network topology

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
      (10G / 2.5G)              (PoE, for the Pi's)
       │     │      │      │      │    │    │    │
   Mac Mini  PC   MSI Cubi M920q Pi #1 Pi #2 Pi #3 Pi #4
   (IA)   personal  NUC  (Proxmox)(DNS)(n8n)(mon)(HA/Frigate)
              │                    │
          NAS #1                NAS #2
        (Primario)              (Réplica)
```

### Architecture decisions (from `07-Decisiones/Registro de Decisiones.md`)

This is the authoritative ADR log — check it before proposing an architecture change, and append to it (same format) when a new decision is made.

- **Fixed roles, not a k3s-style cluster.** The Mac Mini is far more powerful than any Pi; treating nodes as equal would waste that advantage.
- **n8n stays on Contabo for now.** Don't mix "learning Docker" with "can't break this, my flows depend on it." Migrate only once the homelab process is mastered. A second, local n8n instance on Pi #2 is a separate thing for homelab-only automations.
- **The public store lives on Contabo, never on the home Pis.** Uptime, a real fixed IP, and PCI-DSS compliance are all easier on professional infra.
- **MSI Cubi NUC = network/media, not heavy compute.** Only 1 M.2 slot (no storage expansion) and soldered RAM — its real strength is dual 2.5G LAN and the Arc 140V for transcoding, not virtualization.
- **Pi #4 skips the NVMe HAT in favor of the AI HAT+.** The Pi 5 has only one physical PCIe connector; Frigate doesn't need fast storage badly enough to fight for that port.
- **Blink never feeds Frigate** — no native RTSP, and the community bridge's ~30s delay and cloud dependency aren't worth it for real-time detection. Hikvision feeds Frigate directly (full native RTSP).
- **DS214 is Hyper Backup only, no Snapshot Replication** — it's old enough (~2013, ARM) it likely can't do Btrfs, which Snapshot Replication requires. Hyper Backup gets the same practical result over ext4.
- **Photos: 2 copies, not 3** — DS723+ + DS214 was judged sufficient; the Drobo is freed up for something else.
- **Drobo = Frigate's cold video archive**, specifically because security-camera video is what grows the most over time — isolating it keeps it from competing with photos/Nextcloud/Jellyfin on the main NAS. Because Drobo (the company) closed in 2023 and BeyondRAID is proprietary, nothing critical goes here.
- **The Obsidian vault lives on the DS723+, synced via the Nextcloud plugin** — no new storage was bought for it since a vault is megabytes, not terabytes, and Nextcloud was already going to run anyway. *(This is the setting that matters if `Vault_Homelab_Obsidian/vault/` is ever actually migrated onto the NAS — it supersedes the Synology Drive Client proposal in `HOMELAB-OBSIDIAN-INTEGRACION.md`.)*
- **Remote access: Tailscale subnet router on Pi #1** (`--advertise-routes=192.168.1.0/24`), not Cloudflare Tunnel for everything. Sensitive admin panels (Proxmox, DSM) should never go through a public tunnel the way public-facing services (Vaultwarden, n8n) do; a subnet router gives remote access to the whole home network from one login instead.
- **ThinkCentre M920q over M720q** — same price/chassis, but the I219-LM NIC avoids the M720q's I219-V known Proxmox networking bugs, and it has a higher CPU ceiling (up to i9-9900).
- **No second NUC bought for AI** — the Mac Mini stays the sole AI/"Jarvis" node, since AI inference depends on GPU/unified memory that a GPU-less NUC wouldn't meaningfully add to.
- **Reviewed Erik Taveras' (AutoDev Community) all-in-one-PC architecture (34 services/90 containers on one box) and rejected it** in favor of keeping the distributed architecture — a single box is a single point of failure with a shared CPU/RAM ceiling; the distributed setup gives fault isolation and more room to grow. Adopted from his guide: Diun, Dozzle, fail2ban, SearXNG, Gitea/Forgejo, Postiz, Docuseal. Rejected: automatic Watchtower updates (already decided against — see Diun below), and the all-in-one-PC model itself.
- **Diun over Watchtower** — Watchtower auto-updates silently, which can wreck a critical service (database, Vaultwarden) with a bad update before anyone notices. Diun only notifies; updates stay manual (`docker compose pull && docker compose up -d`, after reading the changelog). Associated discipline: pin versions (`image:1.2`, never `:latest`) on anything critical.

### Backups — 3-2-1 plan (`05-Backups/Plan de Backups.md`)

```
DS723+ (RAID 1, primary — active)
  ├── Photos (Synology Photos) ──── Hyper Backup → DS214 (copy #2, deemed sufficient)
  ├── Nextcloud
  ├── Jellyfin library
  ├── Docker volumes (Pi's)         ← RAID 1 only, no external copy (explicitly accepted risk)
  └── homelab-docs/ (Obsidian vault) ── Hyper Backup → DS214 (light, nearly free)

Drobo → Frigate cold video archive (Hikvision clips), outside the automatic backup flow
```

Key point to keep in mind when reasoning about data safety here: **RAID 1 is not a backup** — it protects against one physical disk failing, but not against ransomware, accidental deletion, controller failure, or a house-level disaster (fire/flood/theft), since both RAID copies are still the same physical box.

### Runbooks & troubleshooting knowledge

**Troubleshooting methodology (`03-Troubleshooting/Metodologia de Troubleshooting.md`)** — always work bottom-up, never skip a layer:
1. Physical link: `ip link show <iface>` → look for `state UP`.
2. IP assigned: `ip addr show <iface>` → a `169.254.x.x` address means DHCP isn't working (link-local self-assignment).
3. Network service healthy: `nmcli device status`, `systemctl status <service>`.
4. Real internet: `ping -c 4 8.8.8.8` (network only) then `ping -c 4 google.com` (network + DNS).
5. Container/app running: `docker ps`, `docker compose logs -f`.
6. Service responding on its port: `curl http://localhost:PUERTO`.

**Known incident, resolved (`03-Troubleshooting/Incidente - LAN sin internet Pi 1.md`):** Pi #1 had link but no IPv4 over Ethernet right after mounting the PoE HAT (had `169.254.x.x`/link-local only). Root cause: slow DHCP negotiation on the port's first connection, likely the switch needing extra time to negotiate PoE and data link simultaneously. Fix: `sudo nmcli connection up "Wired connection 1"` forced a fresh DHCP request that completed. **Lesson for the next Pi**: if PoE gives no real IP immediately, force a `nmcli connection up` reconnect before suspecting cabling or the switch.

**Pi 5 NVMe boot (`02-Runbooks/Manual_Instalacion_OS_NVMe_Pi5.md`, HAT: S2Pi EP-0241)** — key gotchas, not the full step list:
- Must boot once from microSD first to update the EEPROM/firmware and enable NVMe boot before it can boot from NVMe directly.
- **Never connect USB-C power while PoE is powering the board** — can damage the hardware.
- Enable PCIe in `/boot/firmware/config.txt` with `dtparam=pciex1`; Gen 3 (`dtparam=pciex1_gen=3`) is optional and can be unstable depending on the cable/SSD — drop it if you see instability.
- EEPROM: `PCIE_PROBE=1` and `BOOT_ORDER=0xf416` (the `6` enables NVMe boot) via `sudo rpi-eeprom-config --edit`.
- Easiest path from an already-configured SD card is cloning with `rpi-clone`, not a clean reinstall.
- A bad `/etc/fstab` entry can prevent boot entirely — always `sudo mount -a` and verify before rebooting after editing it.

**Beginner rollout roadmap (`02-Runbooks/Guia_Principiante_Homelab.md`)** — the intended order for standing up services on a fresh Pi, one every 2-3 days, never all at once: Docker → Homepage (first container, low-stakes dashboard) → Vaultwarden → AdGuard Home → Portainer → Cloudflare Tunnel → (only then, optionally) local n8n. Explicit reassurance baked into this doc: nothing done on the home Pis can break the Contabo n8n, since they're fully separate machines. Cloudflare Tunnel migration note: moving the domain's nameservers from Hostinger to Cloudflare later does **not** break the existing Contabo DNS record — it gets recreated identically inside Cloudflare, and new subdomains for home services get added alongside it.

---

## Vault storage & sync

Current decision (see ADR log above): the vault stays on **NAS DS723+**, synced via the **Nextcloud plugin** — not the Synology Drive Client path proposed in `HOMELAB-OBSIDIAN-INTEGRACION.md`/`GUIA-COMPLETA-Hermes-Obsidian-Claude.md`. Treat the Nextcloud-sync decision as current; treat the Synology Drive Client instructions in those guide files as background reading only, not the plan to implement.

## Pending (per `vault/00-Inicio/Home.md` checklist — nothing below is done except Pi #1)

- Pi #2, #3, #4 — not yet built
- Mac Mini, MSI Cubi NUC, ThinkCentre M920q — not configured/purchased
- NAS DS723+ / DS214 — roles not configured
- Drobo — not assigned to Frigate cold storage yet
- Tailscale — decided (subnet router) but not installed on Pi #1 yet
- Vault migration to the NAS — not started; the vault still lives locally under this Warp folder
- Hermes install & `hermes memory setup` — not done
- WhatsApp → n8n → Obsidian capture flow — not implemented
- Dataview dashboard (`00-Inicio/Dashboard.md`) — not created

## External projects that will consume this infrastructure

- **Santa Diabla** (priority #2) — blog, store, podcast, future dating site. Uses: Chatwoot (support), Cal.com (podcast guest scheduling), Listmonk (newsletter, phase 2), Postiz (podcast promotion), Umami/Plausible (privacy-first analytics — a deliberate fit with the project's privacy angle), Docuseal (contracts), Gitea/Forgejo (private repo).
- **Academia de Poker** (#3) — Cal.com (coaching sessions), Cap (screen recording for hand-strategy lessons).
- **Mitos y Leyendas** (#4) — faceless channel + merchandising. Postiz (scheduling posts alongside each video, can automate via n8n on new-YouTube-upload).
- **Amazon** — e-commerce/affiliates.

`AppFlowy` (Notion alternative, on the M920q) is meant to track all four projects in one place. None of these projects are built yet; the planned unified vault structure reserves a folder per project under `01-Proyectos/` for when they are.
