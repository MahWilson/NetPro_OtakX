# NetPilot Core – Development Documentation

> **Project Status:** 🚧 In Development
>
> This document serves as the living technical documentation for the NetPilot Core project.
> It should be updated whenever significant architectural, implementation, or deployment changes are made.

---

# Project Overview

## Project Name
NetPilot Core

## Description

NetPilot Core is an AI-assisted network automation platform designed to simplify network management using automation tools such as Ansible, NETCONF, SSH, and future AI-assisted validation.

The project aims to provide a modular platform capable of:

- Automated device configuration
- Network auditing
- Configuration backup
- Configuration validation
- Future AI-assisted explanation and analysis
- Support for Cisco IOS devices and Linux servers

---

# Objectives

Current MVP objectives:

- [ ] Deploy development environment using Docker
- [ ] Establish Ansible controller
- [ ] Connect to Cisco CSR1000v
- [ ] Connect to Linux VM
- [ ] Execute Ansible playbooks
- [ ] Perform configuration backup
- [ ] Perform Linux audit
- [ ] Integrate NETCONF
- [ ] Integration & Iterative Testing
- [ ] Final Version Testing

---

# Repository Structure

```
netpilot-core/

docker/
inventory/
playbooks/
roles/
scripts/
ansible/
docs/
```

---

# Current Technology Stack

| Component | Technology |
|------------|------------|
| Automation | Ansible |
| Network | Cisco IOS XE |
| Protocol | SSH |
| Future Protocol | NETCONF |
| Containerization | Docker |
| Version Control | GitHub |

---

# Development Environment

## Host OS

Windows 11

## Docker

Container Name

```
netpilot-controller
```

Working directory

```
/app
```

Python

```
3.8.x
```

Ansible

```
2.9.9
```

---

# Lab Environment

## Cisco Router

Device

```
CSR1000v
```

Management IP

```
192.168.56.101
```

Transport

```
SSH
```

---

## Linux Server

(To be completed)

---

# Inventory Structure

Current inventory:

```
inventory/

routers.ini
linux.ini
```

---

# Playbooks

## router_config.yml

Purpose

- Verify router connectivity
- Execute show commands
- Validate automation pipeline

Current functionality

- show version
- show ip interface brief

Status

✅ Working

---

## linux_audit.yml

Purpose

Perform basic Linux auditing.

Status

🚧 In Progress

---

# Docker Environment

Status

✅ Running

Current Image

(To be updated)

Container

```
netpilot-controller
```

---

# Known Issues

## SSH Host Key Verification

Issue

Paramiko blocks first-time SSH connection because the CSR1000v host key is unknown.

Temporary Fix

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD=True
```

Future Improvement

Configure Docker image to automatically trust lab devices.

Status

Resolved

---

## Legacy Cisco SSH Algorithms

Cisco CSR1000v supports legacy key exchange algorithms.

Current workaround

```
diffie-hellman-group14-sha1
```

Status

Resolved

---

## Jinja2 Warning

```
environmentfilter
```

Cause

Old Ansible with newer Jinja2.

Impact

No functional impact.

Status

Low Priority

---

# Decisions Log

## Decision 001

Docker will be used to standardize the development environment.

Reason

Ensure all developers use identical tooling.

---

## Decision 002

Ansible 2.9 will be maintained for compatibility with Cisco NetAcad labs.

Reason

Avoid compatibility issues with CSR1000v automation.

---

# Development Progress

| Module | Status |
|----------|---------|
| Docker | ✅ |
| GitHub | ✅ |
| Project Structure | ✅ |
| Router Inventory | ✅ |
| Router SSH | ✅ |
| Router Automation | ✅ |
| Linux Inventory | 🚧 |
| Linux Audit | 🚧 |
| NETCONF | ⏳ |

---

# Team Responsibilities

| Member | Responsibility | Status |
|----------|----------------|---------|
| Project Lead | Docker, Architecture, Integration | In Progress |
| Member 2 | Router Automation | |
| Member 3 | Linux Automation | |
| Member 4 | Backend API | |
| Member 5 | Frontend UI | |

---

# Current Milestone

Milestone 1

- Docker operational
- GitHub repository created
- Router connectivity established
- Initial playbooks functional

Status

✅ Completed

---

# Next Milestone

- Linux automation
- NETCONF integration
- Configuration backup
- Backend API

---

# Change Log

## YYYY-MM-DD

- Initial documentation created.

---

# Notes

This document is intended to evolve throughout the project lifecycle.
All contributors are encouraged to update it whenever significant changes are made.