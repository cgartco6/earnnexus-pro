class OutreachAgent:
    def __init__(self, niche):
        self.niche = niche

    def find_leads(self):
        # Scrapes LinkedIn/Google for businesses in SA needing AI
        return [{"name": "Paarden Island Logistics", "gap": "No AI Support"}]

    def draft_proposal(self, lead):
        return f"Proposal for {lead['name']}: Implementing ZAR-based AI Support."
