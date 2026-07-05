import json
import glob
from pathlib import Path

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
import xml.etree.ElementTree as ET

html += """
<div class='section'>
    <h2>NETCONF Device Data (Structured View)</h2>
"""

for report in netconf_reports:
    hostname = "Unknown"
    interfaces = []
    users = []
    routes = []
    banner = "No banner configured"

    # Helper to strip namespaces from XML element tree recursively
    def safe_parse_xml(xml_str):
        if not xml_str or not isinstance(xml_str, str) or not xml_str.strip().startswith("<"):
            return None
        try:
            root = ET.fromstring(xml_str)
            for el in root.iter():
                if el.tag.startswith('{'):
                    el.tag = el.tag.split('}', 1)[1]
            return root
        except Exception:
            return None

    # 1. Parse Hostname
    host_xml = safe_parse_xml(report.get('device_facts'))
    if host_xml is not None:
        host_el = host_xml.find('.//hostname')
        if host_el is not None and host_el.text:
            hostname = host_el.text

    # 2. Parse Interfaces
    intf_xml = safe_parse_xml(report.get('interface_config'))
    if intf_xml is not None:
        interface_node = intf_xml.find('.//interface')
        if interface_node is not None:
            for intf_type_node in interface_node:
                type_name = intf_type_node.tag
                name_el = intf_type_node.find('name')
                name = name_el.text if name_el is not None else ""
                desc_el = intf_type_node.find('description')
                desc = desc_el.text if desc_el is not None else ""
                
                ip = ""
                mask = ""
                ip_el = intf_type_node.find('.//ip/address/primary/address')
                mask_el = intf_type_node.find('.//ip/address/primary/mask')
                if ip_el is not None:
                    ip = ip_el.text
                if mask_el is not None:
                    mask = mask_el.text
                
                interfaces.append({
                    "name": f"{type_name}{name}",
                    "description": desc,
                    "ip": ip,
                    "mask": mask
                })

    # 3. Parse Users
    user_xml = safe_parse_xml(report.get('user_config'))
    if user_xml is not None:
        for u_node in user_xml.findall('.//username'):
            u_name = u_node.find('name')
            u_priv = u_node.find('privilege')
            if u_name is not None:
                users.append({
                    "name": u_name.text,
                    "privilege": u_priv.text if u_priv is not None else "N/A"
                })

    # 4. Parse Static Routes
    routes_xml = safe_parse_xml(report.get('static_routes'))
    if routes_xml is not None:
        for r_node in routes_xml.findall('.//ip-route-interface-forwarding-list'):
            prefix = r_node.find('prefix')
            mask = r_node.find('mask')
            fwd = r_node.find('.//fwd')
            routes.append({
                "prefix": prefix.text if prefix is not None else "",
                "mask": mask.text if mask is not None else "",
                "gateway": fwd.text if fwd is not None else ""
            })

    # 5. Parse Banner
    banner_xml = safe_parse_xml(report.get('banner_config'))
    if banner_xml is not None:
        b_el = banner_xml.find('.//banner')
        if b_el is not None and b_el.text:
            banner = b_el.text

    # Render structured HTML layout
    html += f"""
    <h3>Device Summary: {report.get('hostname', 'router1')}</h3>
    
    <table border="1" cellpadding="5" style="border-collapse: collapse; background: #fff; width: 100%; margin-bottom: 15px;">
        <tr style="background: #eef;">
            <th>Attribute</th>
            <th>Value</th>
        </tr>
        <tr><td><b>Hostname</b></td><td>{hostname}</td></tr>
        <tr><td><b>Banner MOTD</b></td><td><pre style="margin:0; background:none; color:#333; padding:0;">{banner}</pre></td></tr>
    </table>

    <h4>Interface Configuration</h4>
    """

    if interfaces:
        html += """
        <table border="1" cellpadding="5" style="border-collapse: collapse; background: #fff; width: 100%; margin-bottom: 15px;">
            <tr style="background: #eef;">
                <th>Interface</th>
                <th>Description</th>
                <th>IP Address</th>
                <th>Subnet Mask</th>
            </tr>
        """
        for intf in interfaces:
            html += f"""
            <tr>
                <td>{intf['name']}</td>
                <td>{intf['description'] or 'N/A'}</td>
                <td>{intf['ip'] or 'N/A'}</td>
                <td>{intf['mask'] or 'N/A'}</td>
            </tr>
            """
        html += "</table>"
    else:
        html += "<p>No interface configuration found.</p>"

    html += "<h4>Configured Users</h4>"
    if users:
        html += "<ul>"
        for u in users:
            html += f"<li><b>Username:</b> {u['name']} (Privilege Level: {u['privilege']})</li>"
        html += "</ul>"
    else:
        html += "<p>No custom users found.</p>"

    html += "<h4>Static Routes</h4>"
    if routes:
        html += """
        <table border="1" cellpadding="5" style="border-collapse: collapse; background: #fff; width: 100%; margin-bottom: 15px;">
            <tr style="background: #eef;">
                <th>Network Prefix</th>
                <th>Subnet Mask</th>
                <th>Next Hop (Gateway)</th>
            </tr>
        """
        for r in routes:
            html += f"""
            <tr>
                <td>{r['prefix']}</td>
                <td>{r['mask']}</td>
                <td>{r['gateway']}</td>
            </tr>
            """
        html += "</table>"
    else:
        html += "<p>No static routes configured.</p>"

    html += f"""
    <details style="margin-top: 15px;">
        <summary style="cursor: pointer; color: #0066cc; font-weight: bold;">[+] View Raw XML Responses</summary>
        
        <h5>Device Facts Raw XML</h5>
        <pre>{str(report.get('device_facts', ''))[:2000]}</pre>
        
        <h5>Interface configuration Raw XML</h5>
        <pre>{str(report.get('interface_config', ''))[:2000]}</pre>

        <h5>User configuration Raw XML</h5>
        <pre>{str(report.get('user_config', ''))[:2000]}</pre>

        <h5>Static routes configuration Raw XML</h5>
        <pre>{str(report.get('static_routes', ''))[:2000]}</pre>

        <h5>Banner configuration Raw XML</h5>
        <pre>{str(report.get('banner_config', ''))[:2000]}</pre>

        <h5>Full Running Configuration Raw XML</h5>
        <pre>{str(report.get('running_config', ''))[:3000]}</pre>
    </details>
    <hr style="border: 0; border-top: 1px dashed #ccc; margin: 20px 0;">
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