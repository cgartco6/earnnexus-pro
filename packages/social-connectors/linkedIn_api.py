import requests
import os

class LinkedInConnector:
    """
    Compliance: LinkedIn limits Profile updates to 25 per 24-hour window.
    Focus: B2B Impulse leads.
    """
    def post_insight(self, text, user_urn):
        url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {"Authorization": f"Bearer {os.getenv('LINKEDIN_TOKEN')}"}
        
        payload = {
            "author": f"urn:li:person:{user_urn}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": text},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }
        return requests.post(url, headers=headers, json=payload).json()
