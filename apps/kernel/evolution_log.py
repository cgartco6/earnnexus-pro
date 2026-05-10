import json
from datetime import datetime

LOG_FILE = "evolution_history.json"

def log_adaptation(module, change_type, reason):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "module": module,
        "change": change_type,
        "reason": reason
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

# Example: log_adaptation("AI-Bridge", "Swapped to Claude 3.5", "OpenAI Rate Limit")
