import requests
import os

class MetaConnector:
    def __init__(self):
        self.graph_url = "https://graph.facebook.com/v21.0" # 2026 API Version
        self.token = os.getenv("META_GRAPH_TOKEN")

    def post_to_instagram(self, image_url, caption):
        """
        Post to IG Reels/Feed. 
        Limit: 25 Feed posts / 25 Reels per 24hrs.
        """
        # Step 1: Create Media Container
        container_url = f"{self.graph_url}/me/media"
        params = {
            'image_url': image_url,
            'caption': caption,
            'access_token': self.token
        }
        res = requests.post(container_url, params=params).json()
        
        # Step 2: Publish Container
        creation_id = res.get('id')
        publish_url = f"{self.graph_url}/me/media_publish"
        return requests.post(publish_url, params={'creation_id': creation_id, 'access_token': self.token}).json()
