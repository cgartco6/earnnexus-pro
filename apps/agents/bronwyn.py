class BronwynAgent:
    @staticmethod
    def notifyUnlock(user_id, product):
        msg = f"Bronwyn here! 🌟 Your payment is verified. Your {product} suite is UNLOCKED."
        # Trigger WhatsApp/Email API
        print(msg)

    @staticmethod
    def cross_upsell(user_id, current_brand):
        """If they bought Costbyte, offer Apex Digital."""
        offers = {"costbyte": "Apex Digital", "apex": "Carboniq", "carboniq": "Costbyte"}
        next_step = offers.get(current_brand)
        return f"Bronwyn: Since you love {current_brand}, you'll need {next_step} for total dominance."
