import json
import glob
from pathlib import Path
import html as html_esc
import xml.etree.ElementTree as ET
import xml.dom.minidom

def prettify_xml(xml_str):
    if not xml_str or not isinstance(xml_str, str) or not xml_str.strip().startswith("<"):
        return xml_str
    try:
        dom = xml.dom.minidom.parseString(xml_str.strip())
        pretty_str = dom.toprettyxml(indent="  ")
        return "\n".join([line for line in pretty_str.splitlines() if line.strip()])
    except:
        return xml_str

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"
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

def extract_xml_value(xml_string, tag):
    try:
        root = ET.fromstring(xml_string)
        for elem in root.iter():
            local_name = elem.tag.split('}', 1)[1] if '}' in elem.tag else elem.tag
            if local_name == tag:
                return elem.text
    except:
        return None
    return None


# Load report data
linux_reports = load_json_files("*_audit.json")
netconf_reports = load_json_files("*_netconf.json")
router_reports = load_json_files("*_config.json")


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


# NETCONF Section
html += "<div class='section'><h2>NETCONF Device Data</h2>"

for report in netconf_reports:

    hostname = report.get("hostname", "Unknown Device")

    device_facts = report.get("device_facts", "")
    interface_states = report.get("interface_states", "")
    interface_config = report.get("interface_config", "")
    running_config = report.get("running_config", "")

    # Helper to check if XML payload has real children
    def has_real_data(xml_str):
        if not xml_str or not isinstance(xml_str, str) or not xml_str.strip().startswith("<"):
            return False
        try:
            root = ET.fromstring(xml_str)
            return len(list(root)) > 0
        except:
            return False

    # Choose primary source
    primary_source = running_config if has_real_data(running_config) else None
    
    xml_host = device_facts if has_real_data(device_facts) else (primary_source or device_facts)
    xml_intf = interface_config if has_real_data(interface_config) else (primary_source or interface_config)

    # Extract useful structured values
    device_hostname = extract_xml_value(xml_host, "hostname")
    device_version = extract_xml_value(xml_host, "version")
    mac_address = extract_xml_value(xml_intf, "mac-address")

    # Format fallback text values
    disp_hostname = device_hostname if device_hostname else "Not configured"
    disp_version = device_version if device_version else "Unknown version"
    disp_mac = mac_address if mac_address else "Not found/DHCP interface"

    # Prettify and HTML escape raw XML strings so they display correctly in pre blocks
    def process_raw_xml(xml_str, fallback):
        if not xml_str or not isinstance(xml_str, str) or not xml_str.strip():
            return fallback
        pretty = prettify_xml(xml_str)
        return html_esc.escape(pretty[:5000])

    esc_states = process_raw_xml(interface_states, "No interface states data")
    esc_config = process_raw_xml(interface_config, "No interface config data")
    esc_running = process_raw_xml(running_config, "No running config data")

    html += f"""
    <h3>{hostname}</h3>

    <h4>Device Summary</h4>
    <pre>
Hostname: {disp_hostname}
Version : {disp_version}
    </pre>

    <h4>Interface Info</h4>
    <pre>
MAC Address: {disp_mac}
    </pre>

    <h4>Interface States</h4>
    <pre>{esc_states}</pre>

    <h4>Interface Configuration</h4>
    <pre>{esc_config}</pre>

    <h4>Running Configuration</h4>
    <pre>{esc_running}</pre>
    """

html += "</div>"


# Router Section
html += "<div class='section'><h2>Cisco Router Configuration Backup</h2>"

for report in router_reports:
    html += f"<h3>{report.get('hostname')}</h3>"

    router_info = report.get('router_info', [])

    titles = [
        "Show Version",
        "Interface Status",
        "User Configuration",
        "Banner Configuration",
        "Interface Description",
        "Static Routes"
    ]

    for i, output in enumerate(router_info):
        title = titles[i] if i < len(titles) else f"Command {i+1}"

        # FIX: flatten safely
        if isinstance(output, list):
            content = "\n".join(str(x) for x in output)
        else:
            content = str(output)

        html += f"""
        <h4>{title}</h4>
        <pre>{content}</pre>
        """

html += "</div>"


html += """
</body>
</html>
"""


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML report generated: {OUTPUT_FILE}")