#!/usr/bin/env python3
import os
import sys
import time
import socket
import json
import urllib.request
import urllib.error

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
    print(f"{GRAY}  [►] FRAMEWORK: v2.0.0-PRO  //  SUBSYSTEM: ACTIVE   {RESET}")
    print(f"{PURPLE}└──────────────────────────────────────────────────┘{RESET}")

def run_dns_lookup():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: PASSIVE DNS INTELLIGENCE{RESET}")
    print(f" ╚─► Target vectors query external passive route signatures.\n")
    
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    print(f"\n{GRAY} ⚡ Resolving DNS cryptographic signatures...{RESET}")
    try:
        resolved_ip = socket.gethostbyname(clean_target)
        print(f" {GREEN}[✔] Target Correlated ──► IP: {WHITE}{resolved_ip}{RESET}")
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
            else:
                print(f" {RED}[╚═█] Extraction Error: Metadata unreadable.{RESET}")
    except:
        print(f" {RED}[╚═█] Link Failure: Database server connection dropped.{RESET}")

def run_header_extraction():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: HTTP SEC-HEADER EXTRACTION{RESET}")
    print(f" ╚─► Probing runtime application architecture defenses.\n")
    
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]
    final_url = f"http://{clean_target}"

    print(f"\n{GRAY} ⚡ Handshaking remote endpoints at {final_url}...{RESET}\n")
    try:
        req = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            print(f"{PURPLE}┌───[ RAW METADATA EXTRACTED ]{RESET}")
            for key, value in headers.items():
                print(f"{PURPLE}├──{CYAN} {key}{GRAY}: {WHITE}{value}{RESET}")
            print(f"{PURPLE}└──[ END OF VECTOR DATA ]{RESET}")
    except urllib.error.HTTPError as e:
        print(f" {YELLOW}[!] Server Responded with Trapped Status Code: {e.code}{RESET}")
        print(f"{PURPLE}┌───[ EXTRACTED ERROR HEADERS ]{RESET}")
        for key, value in e.headers.items():
            print(f"{PURPLE}├──{CYAN} {key}{GRAY}: {WHITE}{value}{RESET}")
        print(f"{PURPLE}└──[ END OF DATA ]{RESET}")
    except:
        print(f" {RED}[╚═█] Vector Error: Request dropped during handshake.{RESET}")

def run_subdomain_scanner():
    show_banner()
    print(f"\n{CYAN}═╦╝ MODULE: ATTACK SURFACE CLUSTER MAP{RESET}")
    print(f" ╚─► Bruteforcing zone delegation records via host resolution.\n")
    
    target = input(f"{YELLOW} [?] Enter Target Domain (e.g., google.com): {RESET}").strip()
    if not target: return
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    subdomains = ["www", "mail", "ftp", "admin", "blog", "shop", "dev", "api", "secure", "test"]
    print(f"\n{GRAY} ⚡ Bruteforcing common infrastructural sub-allocations...{RESET}\n")
    
    found_count = 0
    print(f"{PURPLE}┌───[ MAPPED ATTACHMENT CHANNELS ]{RESET}")
    for sub in subdomains:
        sub_domain = f"{sub}.{clean_target}"
        try:
            sub_ip = socket.gethostbyname(sub_domain)
            print(f"{PURPLE}├──{GREEN} [LIVE] {WHITE}{sub_domain:<25} {GRAY}─► {CYAN}{sub_ip}{RESET}")
            found_count += 1
        except socket.gaierror:
            continue
            
    print(f"{PURPLE}└───[ SCAN CONCLUDED. CORRELATED: {GREEN}{found_count}{PURPLE} PATHS ]{RESET}")

def main():
    while True:
        show_banner()
        print(f" {PURPLE}🪐 [01] ───►{WHITE} PASSIVE DNS INTELLIGENCE RECORDING{RESET}")
        print(f" {PURPLE}📡 [02] ───►{WHITE} HTTP APP SEC-HEADER EXTRACTION{RESET}")
        print(f" {PURPLE}🔮 [03] ───►{WHITE} SUBDOMAIN ATTACK SURFACE CLUSTER{RESET}")
        print(f" {PURPLE}⚡ [00] ───►{RED} DISCONNECT TERMINAL PIPELINES{RESET}")
        print(f"\n{PURPLE}└──────────────────────────────────────────────────┘{RESET}")
        
        choice = input(f"\n {GREEN}Kaljiosint PRO ~> {RESET}").strip()
        
        if choice in ["1", "01"]:
            run_dns_lookup()
            input(f"\n {GRAY}Press [ENTER] to return to core pipeline...{RESET}")
        elif choice in ["2", "02"]:
            run_header_extraction()
            input(f"\n {GRAY}Press [ENTER] to return to core pipeline...{RESET}")
        elif choice in ["3", "03"]:
            run_subdomain_scanner()
            input(f"\n {GRAY}Press [ENTER] to return to core pipeline...{RESET}")
        elif choice in ["0", "00"]:
            print(f"\n {RED}[!] Shuts down pipeline interfaces safely. Connection Closed.{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n {RED}[X] Path Error: Input vector unauthorized.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
