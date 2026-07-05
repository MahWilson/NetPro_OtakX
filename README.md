```md
# NetPilot Core

**Lightweight Infrastructure Automation and System Audit Framework**

---

# OtakX Team Members

- Mah Wilson  
- Tan Jian Ming  
- Fam Qai Zen  
- Liow Jia Feng  
- Bharath  

---

# Overview

NetPilot Core is a collaborative network automation project developed for the **SECR3253 Network Programming** course.

This project simulates a real-world **Infrastructure as Code (IaC)** workflow using:

- Docker
- Ansible
- NETCONF
- GitHub

It enables automated network configuration and Linux system auditing.

---

# Project Features

## Network Automation (Cisco IOS)

- Configure IP addresses  
- Create user accounts  
- Configure login banners  
- Set interface descriptions  
- Configure static routes  
- Retrieve device information  
- NETCONF-based data collection  

---

## Linux System Audit

- Hostname  
- Date and time  
- CPU usage  
- Memory usage  
- Disk usage  
- Logged-in users  
- Top CPU-consuming processes  

---

# Architecture

```

Developer Machine
↓
Docker (Ansible Controller)
↓
Ansible Automation Layer
↓
Cisco CSR1000v VM + Linux VM

````

---

# Project Structure

```bash
netpilot-core/
├── docker/
│   └── Dockerfile
├── inventory/
│   ├── routers.ini
│   └── linux.ini
├── playbooks/
│   ├── router_config.yml
│   ├── linux_audit.yml
│   └── netconf_get.yml
├── templates/
│   ├── banner.j2
│   └── interface_desc.j2
├── scripts/
│   └── generate_report.py
├── reports/
├── docs/
├── tests/
├── docker-compose.yml
├── requirements.txt
└── README.md
````

---

# Testing Workflow

## 1. Clone Repository

```bash
mkdir netpilot-core
cd netpilot-core
git clone https://github.com/MahWilson/NetPro_OtakX.git
cd NetPro_OtakX
```

---

## 2. Build Docker Environment

```bash
docker compose build
docker compose up -d
```

---

## 3. Enter Container

```bash
docker exec -it netpilot-controller bash
```

Disable host key checking (input in the docker container instance):

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD=True
```

---

## 4. Run Linux Audit

```bash
ansible-playbook -i inventory/linux.ini playbooks/linux_audit.yml
```

---

## 5. Run NETCONF Playbook

```bash
ansible-playbook -i inventory/netconf.ini playbooks/netconf_get.yml
```

---

## 6. Run Router Automation

```bash
ansible-playbook -i inventory/routers.ini playbooks/router_config.yml
```

---

## 7. Generate Final Report

From host machine (PowerShell / WSL):

```bash
python3 scripts/generate_report.py
```

This generates a consolidated JSON report from all playbook outputs.

---

# Expected Output Files

* Linux audit JSON report
* NETCONF device data JSON
* Router configuration JSON
* Final consolidated report

---

# Prerequisites

* Git
* Docker
* Docker Compose
* VirtualBox / VMware
* Cisco CSR1000v VM
* Ubuntu VM

---

# Docker Setup

## Build & Run

```bash
docker compose build
docker compose up -d
```

## Enter Container

```bash
docker exec -it netpilot-controller bash
```

## Stop Environment

```bash
docker compose down
```

---

# Git Workflow

## Feature Branch Workflow

```bash
git pull origin main
git checkout -b feature/your-feature
git add .
git commit -m "your message"
git push origin feature/your-feature
```

Then create a Pull Request → merge into `develop` → then `main`.

---

# Rules

1. Never push directly to `main`
2. All features must be in a branch
3. Merge into `develop` first
4. Test before merging
5. Keep `main` stable

---



# Connectivity Test

```bash
ansible all -i inventory/routers.ini -m ping
ansible cisco -i inventory/routers.ini -m cisco.ios.ios_facts
```

---

# Common Commands

```bash
git status
git log --oneline
git branch
git checkout <branch>
```

```bash
docker ps
docker compose restart
```

---

# Known Issues

## NETCONF / SSH Host Key

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
```

---

## Cisco Legacy Crypto

CSR1000v may require:

* diffie-hellman-group14-sha1
* ssh-rsa fallback

---

# Testing Checklist

* [ ] Docker builds successfully
* [ ] Containers start correctly
* [ ] Cisco reachable
* [ ] Linux reachable
* [ ] Playbooks execute
* [ ] JSON output generated
* [ ] Reports generated successfully

---

# Status

| Module            | Status |
| ----------------- | ------ |
| Docker            | ✅      |
| Router Automation | ✅      |
| Linux Audit       | ✅     |
| NETCONF           | ✅     |
| Reporting         | ✅     |

---

# Notes

This document is actively maintained and updated as the system evolves.

```

