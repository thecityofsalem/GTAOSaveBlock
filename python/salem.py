import subprocess
import time
import os
os.system('')

# color setting bcs colorama bad
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def detect():
    result = subprocess.run(
        ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=GTAOSAVEBLOCK'],
        capture_output=True,
        text=True
    )
    return "No rules match" not in result.stdout

try:
    while True:
        if detect():
            status = f"{GREEN}Nosave On{RESET}"
        else:
            status = f"{RED}Nosave Off{RESET}"
        print(f"\r{status}\033[K", end='', flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting")