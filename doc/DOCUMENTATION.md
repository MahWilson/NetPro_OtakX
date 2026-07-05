# NetPilot Core – Development Documentation

> **Project Status:** 🚧 In Active Development
>
> This document serves as the technical documentation for the NetPilot Core project. It records the project's architecture, development environment, implementation progress, testing workflow, known issues, and future roadmap. All contributors should update this document whenever significant changes are made.

---

# Project Overview

## Project Name

**NetPilot Core**

## Description

NetPilot Core is a lightweight network automation platform developed for managing Cisco IOS XE routers and Linux servers using Infrastructure as Code (IaC) principles. The project leverages Docker to standardize the development environment and Ansible to automate network configuration, Linux auditing, and NETCONF-based data retrieval.

The project is designed with a modular architecture so that additional capabilities, such as AI-assisted configuration validation, natural language explanations, and REST API integration, can be incorporated in future iterations.

---

# Project Objectives

Current MVP Objectives

* ✅ Standardize development environment using Docker
* ✅ Configure GitHub repository and branching workflow
* ✅ Build modular project structure
* ✅ Configure Ansible controller
* ✅ Connect to Cisco CSR1000v through SSH
* ✅ Connect to Linux VM through SSH
* ✅ Execute Router Automation playbook
* ✅ Execute Linux Audit playbook
* 🚧 Complete NETCONF integration
* 🚧 Generate JSON reports automatically
* 🚧 Generate consolidated analysis reports
* 🚧 Integration and iterative testing
* ⏳ Frontend and Backend integration

---

# Repository Structure

```
netpilot-core/
│
├── docker/
│   └── Dockerfile
│
├── inventory/
│   ├── routers.ini
│   ├── linux.ini
│   └── netconf.ini
│
├── playbooks/
│   ├── router_config.yml
│   ├── linux_audit.yml
│   └── netconf_get.yml
│
├── templates/
│   ├── banner.j2
│   └── interface_desc.j2
│
├── reports/
│   ├── router/
│   ├── linux/
│   └── netconf/
│
├── scripts/
│   ├── setup.sh
│   └── generate_report.py
│
├── docs/
│
├── requirements.yml
│
├── docker-compose.yml
│
└── README.md
```

---

# Technology Stack

| Component            | Technology     |
| -------------------- | -------------- |
| Programming Language | Python 3.8     |
| Automation           | Ansible 2.9.9  |
| Containerization     | Docker         |
| Version Control      | Git + GitHub   |
| Network Device       | Cisco CSR1000v |
| Network Protocol     | SSH            |
| Network Management   | NETCONF        |
| Linux Management     | SSH            |
| Template Engine      | Jinja2         |
| SSH Library          | Paramiko       |
| NETCONF Library      | ncclient       |
| Reporting            | JSON           |
| Report Generator     | Python         |

---

# Development Environment

## Host Machine

Windows 11

## Development Platform

Docker Desktop

## Container

```
netpilot-controller
```

Working Directory

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
Cisco CSR1000v
```

Operating System

```
IOS XE 16.09.05
```

Management IP

```
192.168.56.101
```

Connection

```
SSH (Port 22)
```

NETCONF

```
Port 830
```

---

## Linux Server

Management Method

```
SSH
```

Purpose

* Linux auditing
* System information collection
* Security validation

---

# Inventory Files

Current inventories

```
inventory/

routers.ini
linux.ini
netconf.ini
```

Purpose

**routers.ini**

* Router automation

**linux.ini**

* Linux audit

**netconf.ini**

* NETCONF communication

---

# Playbooks

## router_config.yml

### Purpose

Automates Cisco router configuration through SSH.

### Current Features

* Configure login banner
* Configure interface description
* Verify connectivity
* Execute CLI commands
* Save running configuration
* Export command output
* Generate JSON report

### Status

✅ Working

---

## linux_audit.yml

### Purpose

Collects Linux system information for auditing.

### Current Features

* Hostname
* Operating System
* Kernel Version
* CPU Information
* Memory Information
* Disk Usage
* Network Interfaces
* Logged-in Users
* Running Services
* Generate JSON report

### Status

✅ Working

---

## netconf_get.yml

### Purpose

Retrieve device information using NETCONF.

### Current Features

* Device Information
* Interface States
* Interface Configuration
* Running Configuration
* Generate JSON report

### Status

🚧 Currently under compatibility testing

Known issue involves Ansible 2.9 compatibility with modern NETCONF collections.

---

# Templates

Current Jinja2 templates

```
templates/

banner.j2
interface_desc.j2
```

Purpose

### banner.j2

Generates standard login banner.

### interface_desc.j2

Generates interface descriptions dynamically.

---

# Report Generation

Each playbook exports structured JSON output.

```
reports/

router/
linux/
netconf/
```

A Python reporting script aggregates these reports.

```
python3 scripts/generate_report.py
```

Future enhancement

* HTML report
* Dashboard
* Charts
* Historical comparison

---

# Docker Environment

Purpose

Provide identical development environments across all team members.

Benefits

* Consistent Python versions
* Consistent Ansible version
* Consistent dependencies
* Eliminates "works on my machine" issues

Container

```
netpilot-controller
```

Build

```
docker compose build
```

Run

```
docker compose up -d
```

Enter Container

```
docker exec -it netpilot-controller bash
```

---

# Testing Workflow

## Initial Setup

```
git clone https://github.com/MahWilson/NetPro_OtakX.git

cd NetPro_OtakX

docker compose build

docker compose up -d

docker exec -it netpilot-controller bash
```

Disable Host Key Checking

```
export ANSIBLE_HOST_KEY_CHECKING=False
```

Execute Playbooks

```
ansible-playbook -i inventory/routers.ini playbooks/router_config.yml

ansible-playbook -i inventory/linux.ini playbooks/linux_audit.yml

ansible-playbook -i inventory/netconf.ini playbooks/netconf_get.yml
```

Generate Report

```
python3 scripts/generate_report.py
```

---

# Git Workflow

The project follows a Git Flow-inspired workflow.

```
main
│
└── development
      │
      ├── feature/router
      ├── feature/linux
      ├── feature/netconf
      ├── feature/backend
      └── feature/frontend
```

Development Process

1. Create feature branch
2. Implement feature
3. Commit changes
4. Push feature branch
5. Open Pull Request
6. Review changes
7. Resolve merge conflicts if necessary
8. Merge into development
9. Perform integration testing
10. Merge development into main after successful validation

---

# Known Issues

## SSH Host Key Verification

Issue

Unknown SSH host key prevents initial connection.

Temporary Solution

```
export ANSIBLE_HOST_KEY_CHECKING=False
```

Status

✅ Resolved

---

## Legacy SSH Algorithms

Cisco CSR1000v uses legacy cryptographic algorithms.

Workaround

```
diffie-hellman-group14-sha1
```

Status

✅ Resolved

---

## NETCONF Compatibility

Current Issue

Ansible 2.9.9 is incompatible with the latest Galaxy collections, causing errors such as:

```
known_hosts_lookup is not defined
```

Current Status

🚧 Under investigation

Planned Solution

* Pin compatible collection versions
* Maintain compatibility with Cisco NetAcad lab environment

---

## Jinja2 Compatibility Warning

Issue

```
environmentfilter
```

Cause

Older Ansible version with newer Jinja2.

Impact

No functional impact.

Status

Low Priority

---

# Architecture Decisions

## Decision 001

Docker will be used as the standard development environment.

Reason

Ensures every team member uses identical tooling and dependencies.

---

## Decision 002

Ansible 2.9.9 will remain the primary automation engine.

Reason

Required for compatibility with Cisco NetAcad labs.

---

## Decision 003

JSON will be the standard reporting format.

Reason

Machine-readable, lightweight, and easily processed for analytics and dashboards.

---

## Decision 004

All automation will be implemented as modular playbooks.

Reason

Simplifies testing, maintenance, and future feature expansion.

---

# Current Development Progress

| Module                  | Status                   |
| ----------------------- | ------------------------ |
| GitHub Repository       | ✅ Completed              |
| Git Workflow            | ✅ Completed              |
| Docker Environment      | ✅ Completed              |
| Docker Compose          | ✅ Completed              |
| Project Structure       | ✅ Completed              |
| Router Inventory        | ✅ Completed              |
| Linux Inventory         | ✅ Completed              |
| NETCONF Inventory       | ✅ Completed              |
| Router Automation       | ✅ Completed              |
| Linux Audit             | ✅ Completed              |
| Jinja Templates         | ✅ Completed              |
| JSON Report Generation  | ✅ Completed              |
| Python Report Generator | ✅ Completed              |
| NETCONF Playbook        | 🚧 Compatibility Testing |
| Backend API             | ⏳ Planned                |
| Frontend Dashboard      | ⏳ Planned                |
| AI Validation           | ⏳ Future Work            |

---

# Team Responsibilities

| Member       | Responsibility                                     |
| ------------ | -------------------------------------------------- |
| Project Lead | Architecture, Docker, GitHub, Integration, Testing |
| Member 2     | Router Automation                                  |
| Member 3     | Linux Automation                                   |
| Member 4     | Backend API Development                            |
| Member 5     | Frontend Dashboard                                 |

---

# Milestone 1 (Completed)

* Docker environment established
* GitHub repository configured
* Branching strategy implemented
* Router connectivity verified
* Linux connectivity verified
* Router automation operational
* Linux audit operational
* JSON report generation implemented

Status

✅ Completed

---

# Milestone 2 (Current)

* Complete NETCONF compatibility
* Consolidate report generation
* Backend API development
* Integration testing
* Pull Request validation

Status

🚧 In Progress

---

# Milestone 3 (Future)

* REST API
* React Dashboard
* AI-assisted configuration validation
* AI explanation engine
* Configuration compliance checking
* Historical report comparison

---

# Future Enhancements

Planned features include:

* AI-powered configuration validation
* Natural language explanation of configuration changes
* Network compliance checking
* Configuration rollback
* Configuration diff viewer
* Multi-router automation
* Role-Based Access Control (RBAC)
* Dashboard visualization
* REST API
* Real-time monitoring
* Configuration backup scheduling

---

# Change Log

## 2026-07

* Dockerized development environment
* Implemented Git branching workflow
* Completed router automation playbook
* Completed Linux audit playbook
* Added Jinja2 templates
* Added JSON report generation
* Implemented automated report generation script
* Added NETCONF playbook (compatibility testing)
* Improved repository structure
* Standardized testing workflow

---

# Notes

This project is developed as part of a university network automation assignment while following software engineering best practices such as Infrastructure as Code (IaC), containerized development, version control with feature branching, modular playbook design, and iterative integration testing. The architecture is intentionally modular to support future enhancements, including backend APIs, web dashboards, and AI-assisted network automation capabilities.
