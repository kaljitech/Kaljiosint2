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
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/
