import os
from PIL import Image, ImageDraw

class VentureEngine:
    def __init__(self):
        self.ventures = {
            "Costbyte": {"color": "#39FF14", "link": "cb.link", "pitch": "Automate Revenue"},
            "Apex Digital": {"color": "#00FFFF", "link": "apex.link", "pitch": "Design the Future"},
            "Carboniq": {"color": "#FF1493", "link": "cq.link", "pitch": "Asset Mastery"}
        }

    def generate_all(self):
        for name, data in self.ventures.items():
            img = Image.new('RGB', (1080, 1350), color=(0,0,0))
            draw = ImageDraw.Draw(img)
            # Create Brand Identity
            draw.text((100, 400), name, fill=data['color'])
            draw.text((100, 600), data['pitch'], fill=(255,255,255))
            draw.text((100, 1000), f"VISIT: {data['link']}", fill=data['color'])
            
            save_path = f"outputs/posters/{name.lower()}_genesis.png"
            img.save(save_path)
            print(f"✅ Generated {name} marketing asset.")

if __name__ == "__main__":
    VentureEngine().generate_all()
