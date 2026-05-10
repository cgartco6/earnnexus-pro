import time
import subprocess
import requests
import os
from datetime import datetime

# Config
SERVICES = {
    "PORTAL": "http://localhost:3000",
    "CONTENT_ENGINE": "http://localhost:8001/health"
}

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("evolution_history.json", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def check_services():
    for name, url in SERVICES.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                raise Exception(f"Status Code {response.status_code}")
        except Exception as e:
            log_event(f"💀 CRITICAL: {name} is down! Triggering Repair Engine...")
            repair_service(name)

def repair_service(name):
    # Command to restart specific Docker container
    container_name = name.lower().replace("_", "-")
    try:
        subprocess.run(["docker", "restart", container_name], check=True)
        log_event(f"✅ REPAIR: {name} has been restarted.")
    except Exception as e:
        log_event(f"❌ FAILURE: Could not restart {name}. Manual intervention required.")

if __name__ == "__main__":
    log_event("Kernel Online. Monitoring Genesis Stack...")
    while True:
        check_services()
        time.sleep(60) # Pulse every minute
