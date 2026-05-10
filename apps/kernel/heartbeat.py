import time, requests, logging

SERVICES = {
    "AAA": "http://localhost:8000/health",
    "Content": "http://localhost:8001/health",
    "Portal": "http://localhost:3000"
}

def monitor():
    while True:
        for name, url in SERVICES.items():
            try:
                r = requests.get(url, timeout=5)
                if r.status_code != 200: raise Exception("Unhealthy")
                logging.info(f"❤️ {name} is alive.")
            except Exception as e:
                logging.error(f"💀 {name} FAILURE: {e}")
                # Trigger repair_engine.py here
        time.sleep(60)

if __name__ == "__main__":
    monitor()
