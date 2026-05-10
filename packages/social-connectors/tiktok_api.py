import requests
import os

class TikTokConnector:
    def __init__(self):
        self.base_url = "https://open.tiktokapis.com/v2"
        self.access_token = os.getenv("TIKTOK_ACCESS_TOKEN")

    def post_ad(self, video_path, caption):
        """
        Uses 2026 Direct Post API with mandatory AI-Generated Content (AIGC) labeling.
        Limit: 4 posts/day (Governor enforced).
        """
        endpoint = f"{self.base_url}/post/publish/video/init/"
        headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}
        
        payload = {
            "post_info": {
                "title": f"{caption} #ad #nexus",
                "privacy_level": "PUBLIC_TO_EVERYONE",
                "is_aigc": True, # Required for 2026 compliance
                "brand_organic_toggle": True
            },
            "source_info": {
                "source": "PULL_FROM_URL",
                "video_url": video_path
            }
        }
        
        response = requests.post(endpoint, headers=headers, json=payload)
        return response.json()
