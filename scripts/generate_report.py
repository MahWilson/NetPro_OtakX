import json
import glob
from pathlib import Path

REPORT_DIR = Path("../reports")
OUTPUT_FILE = REPORT_DIR / "report.html"


def load_json_files(pattern):
    data = []
    for file in REPORT_DIR.glob(pattern):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data.append(json.load(f))
        except Exception as e:
            print(f"Error reading {file}: {e}")
    return data


# Load report data
linux_reports = load_json_files("*_audit.json")
netconf_reports = load_json_files("*_netconf.json")
router_reports = load_json_files("*_router_backup.json")


html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>NetPilot Core Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background: #f5f5f5;
        }

        h1 {
            color: #222;
        }

        .section {
            background: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }

        pre {
            background: #111;
            color: #00ff88;
            padding: 10px;
            overflow-x: auto;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>NetPilot Core Unified Report</h1>
"""


# Linux Audit Section
html += "<div class='section'><h2>Linux System Audit</h2>"

for report in linux_reports:
    html += f"""
    <h3>{report.get('hostname')}</h3>
    <p><b>Date:</b> {report.get('datetime')}</p>
    <p><b>CPU:</b> {report.get('cpu_model')}</p>
    <p><b>Cores:</b> {report.get('cpu_cores')}</p>

    <h4>Memory</h4>
    <pre>{"\n".join(report.get('memory', []))}</pre>

    <h4>Disk</h4>
    <pre>{"\n".join(report.get('disk', []))}</pre>

    <h4>Logged-in Users</h4>
    <pre>{"\n".join(report.get('logged_in_users', []))}</pre>

    <h4>Top Processes</h4>
    <pre>{"\n".join(report.get('top_processes', []))}</pre>
    """

html += "</div>"


