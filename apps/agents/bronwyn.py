class BronwynAgent:
    def __init__(self):
        self.name = "Bronwyn"
        self.personality = "Professional, helpful, and grounded."

    def notify_success(self, user_email):
        message = (
            f"Hi there! This is {self.name} from the EarnNexus team. "
            "I've just verified your payment. Your dashboard is now fully unlocked! "
            "You can now start marketing and downloading your assets immediately."
        )
        # Logic to send via WhatsApp/Email/In-App
        print(f"📧 Bronwyn sent success message to {user_email}")

    def handle_support(self, query):
        # AI logic to handle "How do I start?" or "Where is my file?"
        return f"Bronwyn: I'd be happy to help you with {query}..."
