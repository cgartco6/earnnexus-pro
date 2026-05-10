# apps/content-engine/humanizer.py
import random

class LeoAgent:
    """The Architect: Creating human-like discovery content."""
    
    TONES = [
        "Founder-led: 'I built this because I was tired of the status quo...'",
        "Hype: 'Cape Town isn't ready for this level of automation.'",
        "Educational: 'Here is exactly how the ZAR portal handles your Rands.'"
    ]

    def create_caption(self, product_name):
        base = random.choice(self.TONS)
        cta = "Check the link in our bio for the full breakdown. 🚀"
        return f"{base}\n\nIntroducing {product_name}. {cta}\n#CapeTech #GenesisLaunch #ZAR"

    def interact_on_post(self):
        """Simulates human interaction in the comment section of our own posts."""
        comments = ["Game changer!", "Is this live in Paarden Eiland?", "Love the neon vibe."]
        return random.choice(comments)
