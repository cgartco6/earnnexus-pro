# apps/content-engine/scheduler.py
import datetime
import pytz # Requires: pip install pytz
import time

class GlobalScheduler:
    def __init__(self):
        # Target Markets for Global Expansion
        self.markets = {
            "SA": "Africa/Johannesburg",
            "UK": "Europe/London",
            "US_EAST": "America/New_York",
            "UAE": "Asia/Dubai"
        }

    def is_peak_impulse_time(self, timezone_str):
        """
        Calculates if the current time in the target market is 
        between 18:00 and 22:00 (Prime scrolling time).
        """
        tz = pytz.timezone(timezone_str)
        local_time = datetime.datetime.now(tz)
        return 18 <= local_time.hour <= 22

    def dispatch_cycle(self):
        """The Heartbeat loop for the Marketing Engine."""
        print("🌍 Global Scheduler: Monitoring Market Windows...")
        while True:
            for market, tz in self.markets.items():
                if self.is_peak_impulse_time(tz):
                    print(f"🚀 Peak Time in {market}! Dispatching localized posters...")
                    # Trigger the specific Social Connector (TikTok/Meta)
                    # Logic to pull localized assets (e.g. USD posters vs ZAR posters)
            
            time.sleep(900) # Check every 15 minutes

if __name__ == "__main__":
    GlobalScheduler().dispatch_cycle()
