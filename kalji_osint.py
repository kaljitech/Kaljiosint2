#!/usr/bin/env python3
import os
import sys
import time
import socket
import json
import urllib.request
import urllib.error

# Color palettes
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
RED     = "\033[1;31m"
RESET   = "\033[0m"

def show_banner():
    os.system('clear')
    print(f"{CYAN}" + "="*50)
    print(f"{WHITE}  _  __      _ _ _                 _ _   ")
    print(" | |/ /___ _| (_|_) ___  ___ _ _ _| |_| ")
    print(" | ' </ _` | | | | |/ _ \(_-<| ' \  _| | ")
    print(f" |_|\_\__,_||_|_| \___//___|_||_|\__|_|{RESET}")
    print(f"{CYAN}" + "="*50 + f"{RESET}")

def run_dns_lookup():
    show_banner()
    print(f"\n{CYAN}[+] Passive DNS & IP Lookup Module Activated{RESET}")
    target = input(f"{YELLOW}Enter Target Domain (e.g., google.com): {RESET}").strip()
    
    if not target:
        print(f"{RED}[X] Error: Target domain cannot be empty.{RESET}")
        return

    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]

    print(f"\n{GREEN}[*] Contacting network registries for {clean_target}...{RESET}")
    try:
        resolved_ip = socket.gethostbyname(clean_target)
        print(f" {GREEN}--->{RESET} Found Target IP: {resolved_ip}")
    except socket.gaierror:
        print(f"{RED}[X] Network Error: Could not resolve domain.{RESET}")
        return

    print(f"{GREEN}[*] Requesting geolocation coordinates...{RESET}")
    api_url = f"http://ip-api.com/json/{resolved_ip}"
    
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data.get("status") == "success":
                print(f"\n{CYAN}[ Target Intelligence Matrix ]{RESET}")
                print(f" {GREEN}•{RESET} ISP       : {data.get('isp')}")
                print(f" {GREEN}•{RESET} Company   : {data.get('org')}")
                print(f" {GREEN}•{RESET} Country   : {data.get('country')}")
                print(f" {GREEN}•{RESET} City      : {data.get('city')}")
            else:
                print(f"{RED}[X] Map Error: {data.get('message', 'Failed to read data')}{RESET}")
    except urllib.error.URLError:
        print(f"{RED}[X] Service Offline: Unable to query global trace database.{RESET}")

def run_header_extraction():
    show_banner()
    print(f"\n{CYAN}[+] HTTP Header Extraction Module Activated{RESET}")
    target = input(f"{YELLOW}Enter Target Domain (e.g., google.com): {RESET}").strip()
    
    if not target:
        print(f"{RED}[X] Error: Target domain cannot be empty.{RESET}")
        return

    # Standardize target to use http:// for raw connection tests
    clean_target = target.replace("http://", "").replace("https://", "").split('/')[0]
    final_url = f"http://{clean_target}"

    print(f"\n{GREEN}[*] Sending connection requests to {final_url}...{RESET}\n")
    try:
        req = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            
            print(f"{CYAN}[ Raw Server Headers ]{RESET}")
            # Loop through all server headers and print them
            for key, value in headers.items():
                print(f" {GREEN}•{RESET} {key}: {WHITE}{value}{RESET}")
                
    except urllib.error.HTTPError as e:
        print(f"{YELLOW}[!] Server Responded with Error Code: {e.code}{RESET}")
        print(f"{CYAN}[ Received Headers ]{RESET}")
        for key, value in e.headers.items():
            print(f" {GREEN}•{RESET} {key}: {WHITE}{value}{RESET}")
    except urllib.error.URLError as e:
        print(f"{RED}[X] Connection Failure: Unable to reach the target web server.{RESET}")

def main():
    while True:
        show_banner()
        print(f"\n{WHITE}[01]{RESET} Passive DNS Lookup")
        print(f"{WHITE}[02]{RESET} HTTP Header Extraction")
        print(f"{WHITE}[00]{RESET} Exit")
        print(f"\n{CYAN}" + "="*50 + f"{RESET}")
        
        choice = input(f"\n{GREEN}Kaljiosint ~> {RESET}").strip()
        
        if choice in ["1", "01"]:
            run_dns_lookup()
            input(f"\n{WHITE}Press [ENTER] to return to menu...{RESET}")
        elif choice in ["2", "02"]:
            run_header_extraction()
            input(f"\n{WHITE}Press [ENTER] to return to menu...{RESET}")
        elif choice in ["0", "00"]:
            print(f"\n{RED}[!] Exiting system. Goodbye!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}[X] Invalid Option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
