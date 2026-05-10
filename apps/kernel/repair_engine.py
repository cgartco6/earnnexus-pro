import subprocess, time, os

class WindowsHealer:
    def __init__(self):
        self.services = ["aaa-service", "content-engine", "micro-saas-tool", "portal"]

    def heal_cycle(self):
        print("🛠️  Self-Healing Kernel Active [Windows 10 Pro]")
        while True:
            for service in self.services:
                result = subprocess.run(
                    ["powershell", "-Command", f"docker inspect -f '{{{{.State.Running}}}}' {service}"],
                    capture_output=True, text=True
                )
                if "true" not in result.stdout.lower():
                    print(f"⚠️  Repairing {service}...")
                    subprocess.run(["docker", "restart", service])
            time.sleep(30)

if __name__ == "__main__":
    WindowsHealer().heal_cycle()
