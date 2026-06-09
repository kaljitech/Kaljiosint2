#!/usr/bin/env python3
import os
import sys

# Colors to make our terminal look high-end
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"
GREEN   = "\033[1;32m"
RED     = "\033[1;31m"
RESET   = "\033[0m"

def show_menu():
    # Clear the screen first
    os.system('clear')
    
    # Print a beautiful design banner
    print(f"{CYAN}" + "="*50)
    print(f"{WHITE}  _  __      _ _ _                 _ _   ")
    print(" | |/ /___ _| (_|_) ___  ___ _ _ _| |_| ")
    print(" | ' </ _` | | | | |/ _ \(_-<| ' \  _| | ")
    print(f" |_|\_\__,_|_|_|_|_|\___//___|_||_|\__|_|{RESET}")
    print(f"{CYAN}" + "="*50 + f"{RESET}")
    
    # Print the options
    print(f"\n{WHITE}[01]{RESET} Passive DNS Lookup")
    print(f"{WHITE}[00]{RESET} Exit")
    print(f"\n{CYAN}" + "="*50 + f"{RESET}")

def main():
    while True:
        show_menu()
        choice = input(f"\n{GREEN}Kaljiosint ~> {RESET}").strip()
        
        if choice == "1" or choice == "01":
            print(f"\n{CYAN}[*] DNS Lookup Engine coming in the next step...{RESET}")
            input(f"\n{WHITE}Press [ENTER] to return to menu...{RESET}")
        elif choice == "0" or choice == "00":
            print(f"\n{RED}[!] Exiting system. Goodbye!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}[X] Invalid Option!{RESET}")
            import time
            time.sleep(1)

if __name__ == "__main__":
    main()
