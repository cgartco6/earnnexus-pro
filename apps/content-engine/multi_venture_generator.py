import os
import random
from PIL import Image, ImageDraw

class MultiVentureArchitect:
    def __init__(self):
        self.ventures = {
            "Costbyte": {
                "color": (57, 255, 20), # Neon Green
                "tagline": "AUTOMATE YOUR REVENUE",
                "focus": "FinTech/SaaS"
            },
            "Apex Digital": {
                "color": (0, 255, 255), # Cyan / Apex Blue
                "tagline": "NEXT-GEN DESIGN & DEV",
                "focus": "Creative Agency"
            },
            "Carboniq": {
                "color": (255, 20, 147), # Deep Pink / Carbon Contrast
                "tagline": "THE FUTURE OF ASSETS",
                "focus": "Asset Management"
            }
        }

    def generate_batch(self):
        for brand_name, config in self.ventures.items():
            print(f"🎨 Leo Agent: Designing for {brand_name}...")
            self.create_poster(brand_name, config)

    def create_poster(self, brand, config):
        # Base Canvas (Black)
        img = Image.new('RGB', (1080, 1350), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Brand-Specific Neon Accent
        draw.rectangle([0, 0, 1080, 20], fill=config["color"])
        
        # Dynamic Text
        draw.text((100, 300), brand.upper(), fill=config["color"])
        draw.text((100, 500), config["tagline"], fill=(255, 255, 255))
        draw.text((100, 1200), "LINK IN BIO | EARNNEXUS ECOSYSTEM", fill=config["color"])
        
        output_dir = f"outputs/posters/{brand.lower().replace(' ', '_')}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        img.save(f"{output_dir}/genesis_ad_{random.getrandbits(16)}.png")

if __name__ == "__main__":
    architect = MultiVentureArchitect()
    architect.generate_batch()
