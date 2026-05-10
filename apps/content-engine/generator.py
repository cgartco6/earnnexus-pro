# apps/content-engine/generator.py
from PIL import Image, ImageDraw, ImageFilter
import random

class PosterArchitect:
    def __init__(self):
        self.brand_neon = (57, 255, 20)
        self.brand_black = (0, 0, 0)

    def generate_dynamic_poster(self, offer_text, price, link):
        """Creates an eye-catching visual without breaking direct-contact laws."""
        # Create unique noise-based background
        bg = Image.new('RGB', (1080, 1350), color=self.brand_black)
        pixels = bg.load()
        for i in range(100): # Random Neon 'Pulse' dots for uniqueness
            x, y = random.randint(0, 1079), random.randint(0, 1349)
            pixels[x, y] = self.brand_neon
        
        # Apply slight blur to make text pop
        bg = bg.filter(ImageFilter.GaussianBlur(radius=2))
        draw = ImageDraw.Draw(bg)
        
        # The Legal Requirement: Identification (NCC 2026 Rule)
        draw.text((50, 1300), "EarnNexus Ltd | Cape Town | Reg: 2024/000/07", fill=(100, 100, 100))
        
        # The Offer
        draw.text((100, 400), offer_text.upper(), fill=self.brand_neon)
        draw.text((100, 600), f"R{price}", fill=(255, 255, 255))
        draw.text((100, 900), "LINK IN BIO TO LEARN MORE", fill=self.brand_neon)
        
        path = f"outputs/posters/poster_{random.getrandbits(32)}.png"
        bg.save(path)
        return path
