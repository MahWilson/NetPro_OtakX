<div align="center">

<img src="https://img.shields.io/badge/NetPilot-Core-0d6efd?style=for-the-badge&logo=ansible&logoColor=white" alt="NetPilot Core"/>

# ≡ƒ¢░∩╕Å NetPilot Core

**Lightweight Infrastructure Automation & System Audit Framework**

*Built for SMEs, university labs, and training environments ΓÇö engineered to real-world DevOps standards.*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Ansible](https://img.shields.io/badge/Ansible-2.15+-EE0000?style=flat-square&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![NETCONF](https://img.shields.io/badge/NETCONF-RFC%206241-4CAF50?style=flat-square&logo=cisco&logoColor=white)](https://tools.ietf.org/html/rfc6241)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

---

[Overview](#-overview) ┬╖ [Architecture](#-architecture) ┬╖ [Getting Started](#-getting-started) ┬╖ [Features](#-features) ┬╖ [Git Workflow](#-git-workflow) ┬╖ [Contributing](#-contributing) ┬╖ [Troubleshooting](#-troubleshooting)

</div>

---

## ≡ƒôû Overview

**NetPilot Core** is a portfolio-quality infrastructure automation and audit framework developed as a university Network Programming assignment. It is intentionally designed to resemble a real-world DevOps/NetOps project ΓÇö demonstrating industry practices while remaining achievable for undergraduate coursework.

### What it does

| Capability | Description |
|---|---|
| ≡ƒöº **Router Automation** | Automated Cisco CSR1000v configuration via Ansible (interfaces, routes, users, banners) |
| ≡ƒôè **Linux Auditing** | Structured system health reports (CPU, RAM, disk, processes, users) |
| ≡ƒöî **NETCONF Automation** | RFC 6241-compliant device interrogation using `ncclient` |
| ≡ƒº⌐ **Jinja2 Templating** | Dynamic, reusable configuration rendering |
| ≡ƒÉ│ **Dockerized Execution** | Reproducible Ansible controller ΓÇö identical across all contributors' machines |
| ≡ƒôï **Infrastructure-as-Code** | Every configuration change tracked, versioned, and peer-reviewed |

### Core Design Principles

> **Real-world architecture ┬╖ Reproducibility ┬╖ Collaboration ┬╖ Maintainability ┬╖ Modularity ┬╖ Portfolio quality**

---

## ≡ƒÅù∩╕Å Architecture

### Local Development Environment

Every contributor runs the **exact same local environment**:

```
Host Machine (Windows / macOS / Linux)
Γöé
Γö£ΓöÇΓöÇ VS Code                          ΓåÉ IDE
Γö£ΓöÇΓöÇ Git & GitHub                     ΓåÉ Version control
Γöé
Γö£ΓöÇΓöÇ Docker Desktop
Γöé    ΓööΓöÇΓöÇ netpilot-controller          ΓåÉ Ansible, Python, ncclient, netmiko
Γöé         ΓööΓöÇΓöÇ /workspace (bind mount) ΓåÉ Live project files
Γöé
ΓööΓöÇΓöÇ VirtualBox
     Γö£ΓöÇΓöÇ Cisco CSR1000v  (192.168.56.101)  ΓåÉ Automation target
     ΓööΓöÇΓöÇ Ubuntu Server   (192.168.56.102)  ΓåÉ Audit target
```

### Network Topology (Host-Only Adapter)

| Host | IP Address | Role |
|---|---|---|
| Host Machine | `192.168.56.1` | Developer workstation |
| Cisco CSR1000v | `192.168.56.101` | Router automation target |
| Ubuntu Server | `192.168.56.102` | Linux audit target |

> The Docker controller communicates with the VirtualBox VMs over the host-only network. Docker standardizes the **controller only** ΓÇö not the network devices.

---

## ≡ƒôü Repository Structure

```
netpilot-core/
Γö£ΓöÇΓöÇ docker/
Γöé   ΓööΓöÇΓöÇ Dockerfile              # Ansible controller image
Γö£ΓöÇΓöÇ inventory/
Γöé   Γö£ΓöÇΓöÇ hosts.yml               # Inventory definition
Γöé   ΓööΓöÇΓöÇ group_vars/             # Group-level variables
Γö£ΓöÇΓöÇ playbooks/
Γöé   Γö£ΓöÇΓöÇ router_config.yml       # Cisco CSR1000v automation
Γöé   Γö£ΓöÇΓöÇ linux_audit.yml         # Ubuntu system audit
Γöé   ΓööΓöÇΓöÇ netconf_facts.yml       # NETCONF device interrogation
Γö£ΓöÇΓöÇ roles/
Γöé   Γö£ΓöÇΓöÇ router/                 # Router automation role
Γöé   Γöé   Γö£ΓöÇΓöÇ tasks/
Γöé   Γöé   Γö£ΓöÇΓöÇ templates/
Γöé   Γöé   Γö£ΓöÇΓöÇ vars/
Γöé   Γöé   ΓööΓöÇΓöÇ handlers/
Γöé   Γö£ΓöÇΓöÇ linux_audit/            # Linux audit role
Γöé   ΓööΓöÇΓöÇ netconf/                # NETCONF role
Γö£ΓöÇΓöÇ templates/
Γöé   Γö£ΓöÇΓöÇ router_config.j2        # Router Jinja2 template
Γöé   Γö£ΓöÇΓöÇ audit_report.j2         # HTML audit report template
Γöé   ΓööΓöÇΓöÇ interface.j2            # Interface configuration template
Γö£ΓöÇΓöÇ scripts/
Γöé   ΓööΓöÇΓöÇ setup.sh                # One-command contributor onboarding
Γö£ΓöÇΓöÇ docs/
Γöé   Γö£ΓöÇΓöÇ architecture.md
Γöé   Γö£ΓöÇΓöÇ playbook-guide.md
Γöé   ΓööΓöÇΓöÇ netconf-guide.md
Γö£ΓöÇΓöÇ tests/
Γöé   ΓööΓöÇΓöÇ integration/            # Integration test playbooks
Γö£ΓöÇΓöÇ reports/                    # Generated audit reports (gitignored)
Γö£ΓöÇΓöÇ docker-compose.yml
Γö£ΓöÇΓöÇ requirements.txt            # Python dependencies
Γö£ΓöÇΓöÇ .gitignore
Γö£ΓöÇΓöÇ CONTRIBUTING.md
ΓööΓöÇΓöÇ README.md
```

---

## ≡ƒÜÇ Getting Started

### Prerequisites

Ensure the following are installed on your machine:

| Tool | Version | Notes |
|---|---|---|
| [Git](https://git-scm.com/) | 2.x+ | Version control |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Latest | Container runtime |
| [VirtualBox](https://www.virtualbox.org/) | 7.x | Hosts the VMs |
| [VS Code](https://code.visualstudio.com/) | Latest | Recommended IDE |

### VirtualBox VM Setup

Before running the project, ensure both VMs are configured and reachable:

**Cisco CSR1000v (`192.168.56.101`)**
- Enable SSH access on the router
- Ensure NETCONF is enabled (`netconf-yang`)
- Add your SSH credentials to `inventory/group_vars/routers.yml`

**Ubuntu Server (`192.168.56.102`)**
- Ensure SSH access is enabled
- Add your SSH credentials to `inventory/group_vars/linux.yml`

> See [`docs/architecture.md`](docs/architecture.md) for full VM setup instructions.

---

### Quick Start (Onboarding)

```bash
# 1. Clone the repository
git clone https://github.com/MahWilson/NetPro_OtakX.git
cd NetPro_OtakX

# 2. Run the one-command setup script
bash scripts/setup.sh

# 3. Verify the controller is running
docker compose ps

# 4. Enter the controller container
docker compose exec controller bash

# 5. Run your first playbook
ansible-playbook playbooks/linux_audit.yml
```

> `scripts/setup.sh` handles Docker verification, image building, container startup, and health checks automatically.

---

### Manual Setup (Step-by-Step)

```bash
# Build the Ansible controller image
docker compose build

# Start the controller container
docker compose up -d

# Enter the running controller
docker compose exec controller bash

# Inside the container ΓÇö verify Ansible
ansible --version

# Test connectivity to all hosts
ansible all -m ping
```

---

## Γ£¿ Features

### ≡ƒöº Router Automation (Cisco CSR1000v)

Automates full router configuration via Ansible:

```bash
# Apply full router configuration
ansible-playbook playbooks/router_config.yml

# Configure specific components only
ansible-playbook playbooks/router_config.yml --tags interfaces
ansible-playbook playbooks/router_config.yml --tags routes
ansible-playbook playbooks/router_config.yml --tags users
ansible-playbook playbooks/router_config.yml --tags banner
```

**What gets automated:**
- Interface IP configuration
- Static routing
- Local user accounts
- Login banners
- All playbooks are **idempotent** ΓÇö safe to run multiple times

---

### ≡ƒôè Linux System Audit

Collects and reports structured system health information:

```bash
# Run full audit and generate report
ansible-playbook playbooks/linux_audit.yml
```

**Audit scope:**
- Hostname and system metadata
- CPU utilization
- RAM and swap usage
- Disk usage per mount point
- Running processes
- Currently logged-in users

Reports are generated as structured HTML files in `reports/`.

---

### ≡ƒöî NETCONF Automation

Queries Cisco CSR1000v using NETCONF/YANG via `ncclient`:

```bash
# Retrieve device facts
ansible-playbook playbooks/netconf_facts.yml

# Query specific data
ansible-playbook playbooks/netconf_facts.yml --tags interfaces
ansible-playbook playbooks/netconf_facts.yml --tags running-config
```

**Capabilities demonstrated:**
- Device capability negotiation
- Running configuration retrieval
- Interface state retrieval
- YANG model querying

---

## ≡ƒùé∩╕Å Inventory Configuration

Edit `inventory/hosts.yml` to match your environment:

```yaml
all:
  children:
    routers:
      hosts:
        csr1000v:
          ansible_host: 192.168.56.101
          ansible_user: admin
          ansible_network_os: ios
          ansible_connection: network_cli
    linux:
      hosts:
        ubuntu_server:
          ansible_host: 192.168.56.102
          ansible_user: ubuntu
          ansible_connection: ssh
```

> **Never commit plaintext passwords.** Use Ansible Vault for sensitive variables:
> ```bash
> ansible-vault create inventory/group_vars/vault.yml
> ```

---

## ≡ƒÉ│ Docker Reference

### Common Commands

```bash
# Build the controller image
docker compose build

# Start containers (detached)
docker compose up -d

# Enter the controller shell
docker compose exec controller bash

# View container logs
docker compose logs -f controller

# Stop all containers
docker compose down

# Rebuild from scratch
docker compose down && docker compose build --no-cache && docker compose up -d
```

### What the Controller Contains

| Package | Purpose |
|---|---|
| `ansible` | Automation engine |
| `python3` | Runtime |
| `ncclient` | NETCONF client |
| `netmiko` | SSH network device automation |
| `paramiko` | SSH library |
| `jinja2` | Template rendering |

The project directory is bind-mounted into the container at `/workspace` ΓÇö changes on your host are immediately reflected inside the container.

---

## ≡ƒöÇ Git Workflow

This project follows an open-source collaboration model. **Every contributor owns the entire codebase.**

### Branch Strategy

```
feature/your-feature-name
        Γåô
    Pull Request  (peer review required)
        Γåô
      develop     (integration testing)
        Γåô
       main       (always demo-ready Γ£à)
```

### Protected Branches

| Branch | Rule |
|---|---|
| `main` | Never push directly ΓÇö PRs only, always stable |
| `develop` | Integration branch ΓÇö merge feature PRs here first |
| `feature/*` | Your working branch |

### Standard Workflow

```bash
# Start from develop
git checkout develop
git pull origin develop

# Create your feature branch
git checkout -b feature/your-feature-name

# Make your changes, commit regularly
git add .
git commit -m "feat: describe what you changed"

# Push your branch
git push origin feature/your-feature-name

# Open a Pull Request on GitHub ΓåÆ target: develop
```

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Use for |
|---|---|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code restructuring |
| `test:` | Test additions |
| `chore:` | Maintenance tasks |

**Examples:**
```
feat: add static route configuration to router role
fix: correct interface naming in CSR1000v template
docs: add NETCONF setup guide to docs/
refactor: extract banner task into dedicated handler
```

---

## ≡ƒæÑ Team & Feature Ownership

| Feature Area | Lead | GitHub | Description |
|---|---|---|---|
| **Router Automation** | ΓÇö | ΓÇö | Interface config, routes, users, banners, idempotency |
| **Linux Audit** | Jian Ming | [@Jianming03](https://github.com/Jianming03) | Hostname, CPU, RAM, disk, processes, users, reports |
| **NETCONF** | ΓÇö | ΓÇö | Device facts, running config, interfaces, ncclient |
| **Integration & Docs** | ΓÇö | ΓÇö | Inventory, templates, README, consistency |

> Feature leads **own** their area but every contributor can ΓÇö and should ΓÇö open PRs on any feature.

---

## ≡ƒº¬ Testing

### Connectivity Check

```bash
# Inside the controller container
ansible all -m ping
ansible routers -m ping
ansible linux -m ping
```

### Dry Run (Check Mode)

```bash
# Preview changes without applying them
ansible-playbook playbooks/router_config.yml --check
ansible-playbook playbooks/linux_audit.yml --check
```

### Integration Tests

```bash
# Run full integration test suite
ansible-playbook tests/integration/test_all.yml
```

### Idempotency Verification

```bash
# Run any playbook twice ΓÇö the second run should report zero changes
ansible-playbook playbooks/router_config.yml
ansible-playbook playbooks/router_config.yml   # Expect: changed=0
```

---

## ≡ƒôä Contributing

We welcome all contributors. Please follow these steps:

1. **Fork or branch** ΓÇö never push directly to `main` or `develop`
2. **Follow the Git workflow** described above
3. **Write idempotent playbooks** ΓÇö every task must be safe to re-run
4. **Test before submitting a PR** ΓÇö run `ansible all -m ping` and a dry run
5. **Review teammates' code** ΓÇö all PRs require at least one approval
6. **Keep playbooks modular** ΓÇö use roles, variables, and templates

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full contribution guide.

---

## ≡ƒöº Troubleshooting

### Docker Issues

**Problem:** `docker compose up` fails  
**Solution:** Ensure Docker Desktop is running and WSL2 backend is enabled (Windows)

**Problem:** Container cannot reach VMs  
**Solution:** Verify VirtualBox Host-Only adapter is configured at `192.168.56.0/24`

```bash
# Check network reachability from the host
ping 192.168.56.101
ping 192.168.56.102
```

---

### Ansible Issues

**Problem:** `ansible all -m ping` fails  
**Solution:** Verify SSH is enabled on target VMs and credentials in `inventory/group_vars/` are correct

**Problem:** `UNREACHABLE` error for CSR1000v  
**Solution:** Ensure the router is powered on in VirtualBox and has SSH enabled:
```
CSR1000v# conf t
CSR1000v(config)# ip ssh version 2
CSR1000v(config)# line vty 0 4
CSR1000v(config-line)# login local
CSR1000v(config-line)# transport input ssh
```

---

### NETCONF Issues

**Problem:** `ncclient` connection refused  
**Solution:** Enable NETCONF on the Cisco router:
```
CSR1000v(config)# netconf-yang
```

---

### Ansible Vault

```bash
# Encrypt a secrets file
ansible-vault encrypt inventory/group_vars/vault.yml

# Edit an encrypted file
ansible-vault edit inventory/group_vars/vault.yml

# Run playbook with vault password
ansible-playbook playbooks/router_config.yml --ask-vault-pass
```

---

## ≡ƒôÜ Documentation

| Document | Description |
|---|---|
| [`docs/architecture.md`](docs/architecture.md) | Full system architecture and VM setup guide |
| [`docs/playbook-guide.md`](docs/playbook-guide.md) | Playbook usage reference |
| [`docs/netconf-guide.md`](docs/netconf-guide.md) | NETCONF and ncclient usage guide |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidelines |

---

## ≡ƒ¢ú∩╕Å Roadmap

- [x] Docker environment and controller setup
- [x] Inventory configuration
- [ ] Router automation (interfaces, routes, users, banner)
- [ ] Linux system auditing with structured reports
- [ ] NETCONF device interrogation
- [ ] Jinja2 template-driven configuration rendering
- [ ] Integration testing suite
- [ ] Full documentation
- [ ] GitHub Actions CI (optional)
- [ ] Final polishing and demo preparation

---

## ≡ƒô£ License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**NetPilot Core** ΓÇö *University Network Programming Group Project*

Universiti Teknologi Malaysia (UTM) ┬╖ Year 3 Semester 2 ┬╖ 2025/2026

*Built with Γ¥ñ∩╕Å by the OtakX team*

[![GitHub](https://img.shields.io/badge/GitHub-MahWilson%2FNetPro__OtakX-181717?style=flat-square&logo=github)](https://github.com/MahWilson/NetPro_OtakX)

</div>
