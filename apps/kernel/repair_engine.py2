# apps/kernel/repair_engine.py (Windows Optimized)
import subprocess
import time
import os

class WindowsHealer:
    def __init__(self):
        self.services = ["aaa-service", "content-engine", "micro-saas-tool"]

    def heal_cycle(self):
        while True:
            for service in self.services:
                # Use powershell to check container health
                result = subprocess.run(
                    ["powershell", "-Command", f"docker inspect -f '{{{{.State.Running}}}}' {service}"],
                    capture_output=True, text=True
                )
                if "true" not in result.stdout.lower():
                    print(f"[REPAIR] {service} is failing. Re-initializing...")
                    subprocess.run(["docker", "restart", service])
            
            # Evolution check: Adapt if API endpoints change
            time.sleep(30) # Check every 30 seconds

if __name__ == "__main__":
    healer = WindowsHealer()
    healer.heal_cycle()
