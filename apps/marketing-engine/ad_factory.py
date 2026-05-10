# apps/marketing-engine/ad_factory.py
from PIL import Image, ImageDraw

class AdFactory:
    def create_impulse_ad(self, product_name, price, link):
        """Generates high-conversion square images for social media."""
        # 1. Base: High-contrast Neon Green/Black
        img = Image.new('RGB', (1080, 1080), color=(0, 0, 0))
        d = ImageDraw.Draw(img)
        
        # 2. Add 'Temu-style' Scarcity
        d.text((50, 50), "GENESIS LAUNCH: 90% OFF", fill=(57, 255, 20))
        d.text((50, 400), f"{product_name}", fill=(255, 255, 255))
        d.text((50, 600), f"ONLY R {price}", fill=(57, 255, 20))
        d.text((50, 900), "CLICK LINK IN BIO", fill=(255, 255, 255))
        
        ad_path = f"assets/ads/{product_name}_ad.png"
        img.save(ad_path)
        return ad_path
