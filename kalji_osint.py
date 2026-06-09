#!/usr/bin/env python3
import os
import sys
import time
import socket
import json
import urllib.request
import urllib.error
from datetime import datetime

# Import Telephony Parsing Engines
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print("\n[!] Missing dependency: run 'pip install phonenumbers' in your terminal first.\n")
    sys.exit(1)

# --- FUTURISTIC NEON ANSI PALETTE ---
CYAN    = "\033[38;5;51m"    # Electric Cyan
PURPLE  = "\033[38;5;141m"   # High-Tech Purple
GREEN   = "\033[38;5;84m"    # Operational Green
YELLOW  = "\033[38;5;220m"   # Warning Gold
RED     = "\033[38;5;203m"   # Threat Alert Red
WHITE   = "\033[38;5;231m"   # Clean Data White
GRAY    = "\033[38;5;244m"   # Structural Muted Gray
RESET   = "\033[0m"

def show_banner():
    os.system('clear')
    print(f"{PURPLE}┌──────────────────────────────────────────────────┐{RESET}")
    print(f"{CYAN}    ╦╔═  ╔═╗  ╦    ╦  ╦  ╔═╗  ╔═╗  ╦  ╔╗╔  ╔╦╗    {RESET}")
    print(f"{WHITE}    ╠╩╗  ╠═╣  ║    ║  ║  ║ ║  ╚═╗  ║  ║║║   ║     {RESET}")
    print(f"{CYAN}    ╩ ╩  ╩ ╩  ╩═╝  ╚╝  ╚═╝  ╚═╝  ╩  ╝╚╝   ╩     {RESET}")
    print(f"{PURPLE}├──────────────────────────────────────────────────┤{RESET}")
    print(f"{GRAY}  [►] FRAMEWORK: v3.5.0-PRO  //  SUBSYSTEM: ACTIVE   {RESET}")
    print(f"{PURPLE}└──────────────────────────────────────────────────┘{RESET}")

def export_log(module_name, target, dataset):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_target = target.replace('.', '_').replace('+', '').replace(':', '_')
    filename = f"logs/{module_name.lower()}_{clean_target}_{timestamp}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"==================================================\n")
            file.write(f" KALJIOSINT PRO INTELLIGENCE REPORT              \n")
            file.write(f" GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f" MODULE   : {module_name.upper()}\n")
            file.write(f" TARGET   : {target}\n")
            file.write(f"==================================================\n\n")
            for line in dataset:
                file.write(f"{line}\n")
        print(f"\n{GRAY} [i] Session captured ──► {GREEN}{filename}{RESET}")
    except Exception as e:
        print(f"\n{RED} [X] Exporter Error: Unable to disk-write log telemetry: {e}{RESET}")

def run_dns_lookup():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: PASSIVE DNS INTELLIGENCE{RESET}")
    print(f" ╚─► Target vectors query external passive route signatures.\n")
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    log_data = []
    print(f"\n{GRAY} ⚡ Resolving DNS cryptographic signatures...{RESET}")
    try:
        resolved_ip = socket.gethostbyname(clean_target)
        print(f" {GREEN}[✔] Target Correlated ──► IP: {WHITE}{resolved_ip}{RESET}")
        log_data.append(f"Resolved IP: {resolved_ip}")
    except socket.gaierror:
        print(f" {RED}[╚═█] Core Resolution Failure: Host unrecognized.{RESET}")
        return

    print(f"{GRAY} ⚡ Querying decentralized trace registers...{RESET}")
    api_url = f"http://ip-api.com/json/{resolved_ip}"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data.get("status") == "success":
                print(f"\n{PURPLE}┌───[ TARGET DATA INTEGRITY MATRIX ]{RESET}")
                print(f"{PURPLE}├──{GRAY} ISP        : {WHITE}{data.get('isp')}{RESET}")
                print(f"{PURPLE}├──{GRAY} ASN/ORG    : {WHITE}{data.get('org')}{RESET}")
                print(f"{PURPLE}├──{GRAY} COUNTRY    : {WHITE}{data.get('country')}{RESET}")
                print(f"{PURPLE}└──{GRAY} LOCALITY   : {WHITE}{data.get('city')}{RESET}")
                log_data.extend([f"ISP: {data.get('isp')}", f"Org: {data.get('org')}", f"Country: {data.get('country')}", f"City: {data.get('city')}"])
                export_log("dns", clean_target, log_data)
            else:
                print(f" {RED}[╚═█] Extraction Error: Metadata unreadable.{RESET}")
    except:
        print(f" {RED}[╚═█] Link Failure: Database server connection dropped.{RESET}")

def run_header_extraction():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: HTTP SEC-HEADER EXTRACTION{RESET}")
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]
    final_url = f"http://{clean_target}"

    log_data = []
    print(f"\n{GRAY} ⚡ Handshaking remote endpoints at {final_url}...{RESET}\n")
    try:
        req = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            print(f"{PURPLE}┌───[ RAW METADATA EXTRACTED ]{RESET}")
            for key, value in headers.items():
                print(f"{PURPLE}├──{CYAN} {key}{GRAY}: {WHITE}{value}{RESET}")
                log_data.append(f"{key}: {value}")
            print(f"{PURPLE}└──[ END OF VECTOR DATA ]{RESET}")
            export_log("headers", clean_target, log_data)
    except:
        print(f" {RED}[╚═█] Vector Error: Request dropped during handshake.{RESET}")

def run_subdomain_scanner():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: ATTACK SURFACE CLUSTER MAP{RESET}")
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    subdomains = ["www", "mail", "ftp", "admin", "blog", "shop", "dev", "api", "secure", "test"]
    log_data = []
    found_count = 0
    print(f"{PURPLE}┌───[ MAPPED ATTACHMENT CHANNELS ]{RESET}")
    for sub in subdomains:
        sub_domain = f"{sub}.{clean_target}"
        try:
            sub_ip = socket.gethostbyname(sub_domain)
            print(f"{PURPLE}├──{GREEN} [LIVE] {WHITE}{sub_domain:<25} {GRAY}─► {CYAN}{sub_ip}{RESET}")
            log_data.append(f"[LIVE] {sub_domain} -> {sub_ip}")
            found_count += 1
        except socket.gaierror:
            continue
    print(f"{PURPLE}└───[ SCAN CONCLUDED. CORRELATED: {GREEN}{found_count}{PURPLE} PATHS ]{RESET}")
    export_log("subdomains", clean_target, log_data)

def run_port_scanner():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: COVERT INTERFACE PORT PROBER{RESET}")
    target = input(f"{YELLOW} [?] Enter Target Domain or IP: {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    try:
        target_ip = socket.gethostbyname(clean_target)
        print(f" {GREEN}[✔] Target Address Matrix Locked ──► {WHITE}{target_ip}{RESET}\n")
    except socket.gaierror:
        print(f" {RED}[╚═█] Connection Error: Host identity untraceable.{RESET}")
        return

    critical_ports = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-ALT"}
    log_data = [f"Target IP: {target_ip}"]
    print(f"{PURPLE}┌───[ HOST EDGE PORT MAP ]{RESET}")
    for port, service in critical_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        if s.connect_ex((target_ip, port)) == 0:
            print(f"{PURPLE}├──{GREEN} [OPEN] {WHITE}PORT {port:<5} ─► {CYAN}{service}{RESET}")
            log_data.append(f"[OPEN] Port {port} ({service})")
        else:
            print(f"{PURPLE}├──{GRAY} [CLOSED] PORT {port:<5} ─► {service}{RESET}")
        s.close()
    print(f"{PURPLE}└───[ PORT PROBE PIPELINE CONCLUDED ]{RESET}")
    export_log("ports", clean_target, log_data)

def run_phone_parser():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: TELEPHONY CARRIER MATRIX{RESET}")
    raw_number = input(f"{YELLOW} [?] Enter Number (with Country Code, e.g., +260...): {RESET}").strip()
    if not raw_number: return

    print(f"\n{GRAY} ⚡ Checking international telecommunication records...{RESET}")
    try:
        phone_obj = phonenumbers.parse(raw_number, None)
        if not phonenumbers.is_valid_number(phone_obj):
            print(f" {RED}[╚═█] Validation Error: String does not match structural allocation grids.{RESET}")
            return
        country_zone = geocoder.description_for_number(
