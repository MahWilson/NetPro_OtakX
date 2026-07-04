# NetPilot Core

**Lightweight Infrastructure Automation and System Audit Framework**

# OtakX Team Members

* Mah Wilson
* Tan Jian Ming
* Fam Qai Zen
* Liow Jia Feng
* Bharath

## Overview

NetPilot Core is a collaborative network automation project developed for the SECR3253 Network Programming course.

This project aims to automate network device configuration and Linux system auditing using:

* Docker
* Ansible
* NETCONF
* GitHub

The goal is to simulate a real-world Infrastructure as Code (IaC) workflow where teams collaboratively manage and automate infrastructure deployment.

This project performs:

### Network Device Automation

* Configure IP addresses
* Create user accounts
* Set banner messages
* Configure interface descriptions
* Configure static routes
* Retrieve device information

### Linux System Audit

* Hostname
* Current date and time
* CPU information
* Memory usage
* Disk usage
* Logged-in users
* Top 5 CPU-consuming processes

---

# Project Architecture

Local machine runs Dockerized Ansible Controller.

Ansible communicates with:

* Cisco Router VM (provided by lecturer)
* Linux VM (Ubuntu)

Flow:

Developer Machine → Docker → Ansible → Cisco/Linux Targets

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
├── reports/
├── scripts/
│   └── setup.sh
├── docs/
├── tests/
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

# Prerequisites

Install:

* Git
* Docker
* Docker Compose
* VirtualBox / VMware
* Cisco VM from lecturer
* Ubuntu VM

---

# Initial Setup

## Step 1 — Create project folder

Create folder:

```bash
mkdir netpilot-core
cd netpilot-core
```

IMPORTANT:

Run all Git commands INSIDE this root folder.

This folder is your Git root.

---

## Step 2 — Initialize Git

Inside project root:

```bash
git init
```

Connect GitHub repo:

```bash
git remote add origin <your-repo-url>
```

Check:

```bash
git remote -v
```

First commit:

```bash
git add .
git commit -m "Initial project setup"
git branch -M main
git push -u origin main
```

---

# Team Setup

Each member:

```bash
git clone <repo-url>
cd netpilot-core
```

Create branch:

```bash
git checkout -b feature/your-feature-name
```

Example:

```bash
git checkout -b feature/router-ip-config
```

Push:

```bash
git push origin feature/router-ip-config
```

Create Pull Request on GitHub.

---

# Docker Setup

## Build container

From project root:

```bash
docker compose build
```

Run:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

Enter container:

```bash
docker exec -it netpilot-controller bash
```

Stop:

```bash
docker compose down
```

---

# Dockerfile Example

Location:

```bash
docker/Dockerfile
```

🧪 Running Playbooks
Router automation (Cisco IOS)
```bash
ansible-playbook playbooks/router_config.yml -i inventory/routers.ini
```

Linux system audit
```bash
ansible-playbook playbooks/linux_audit.yml -i inventory/linux.ini
```

NETCONF retrieval
```bash
ansible-playbook playbooks/netconf_get.yml -i inventory/routers.ini
```

---

# Inventory Setup

## Router inventory

File:

```bash
inventory/routers.ini
```

Example:

```ini
[cisco]
router1 ansible_host=192.168.1.10 ansible_user=admin ansible_password=admin
```

---

## Linux inventory

File:

```bash
inventory/linux.ini
```

Example:

```ini
[linux]
server1 ansible_host=192.168.1.20 ansible_user=ubuntu ansible_password=ubuntu
```

---

# Connectivity Test

Inside Docker container:

Linux test:

```bash
ansible linux -i inventory/linux.ini -m ping
```

Cisco test:

```bash
ansible cisco -i inventory/routers.ini -m ping
```

Retrieve Cisco facts:

```bash
ansible cisco -i inventory/routers.ini -m cisco.ios.ios_facts
```

---

# Run Playbooks

## Router config

Run:

```bash
ansible-playbook playbooks/router_config.yml -i inventory/routers.ini
```

---

## Linux audit

Run:

```bash
ansible-playbook playbooks/linux_audit.yml -i inventory/linux.ini
```

---

## NETCONF retrieval

Run:

```bash
ansible-playbook playbooks/netconf_get.yml -i inventory/routers.ini
```

---

# Git Workflow


Pull latest:

```bash
git pull origin main
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Added router IP automation"
```
Branch Policy:

1. Never push directly to main
2. All features must branch from develop
3. All PRs merge into develop first
4. At least one teammate must test before approval
5. Full integration test required after each merge
6. Only stable develop can merge into main

Push:

```bash
git push origin feature/router-ip-config
```

Merge via Pull Request.

---

# Collaboration Workflow

1. Pull latest changes
2. Create feature branch
3. Implement feature
4. Test feature locally
5. Push branch
6. Open Pull Request
7. Team review
8. Merge to main

---

# Testing Checklist

Before merge:

[ ] Docker builds successfully
[ ] Ansible container runs
[ ] Cisco VM reachable
[ ] Linux VM reachable
[ ] Playbook executes successfully
[ ] Output verified
[ ] Another member reviewed code

---

# Common Commands

Check branches:

```bash
git branch
```

Switch branch:

```bash
git checkout branch-name
```

See commit history:

```bash
git log --oneline
```

See file changes:

```bash
git status
```

Restart Docker:

```bash
docker compose down
docker compose up -d
```

List Ansible hosts:

```bash
ansible all --list-hosts -i inventory/routers.ini
```

Check syntax:

```bash
ansible-playbook playbooks/router_config.yml --syntax-check
```

---

