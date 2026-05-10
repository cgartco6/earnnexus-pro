class TheBrain:
    def __init__(self):
        self.sentiment_score = 1.0 # Base multiplier

    def analyze_market_sentiment(self):
        """AI analyzes global interest in your 3 ventures."""
        # Simulated: If Apex Digital design trends are up 20%, raise price 5%
        trends = {"costbyte": 1.1, "apex": 1.2, "carboniq": 0.9}
        return trends

    def predictive_churn(self, user_activity_logs):
        """If a user hasn't generated a poster in 48hrs, Bronwyn intervenes."""
        for user in user_activity_logs:
            if user['inactive_days'] > 2:
                BronwynAgent.send_reengagement(user['id'])

    def calculate_dynamic_price(self, base_price, brand):
        trends = self.analyze_market_sentiment()
        return base_price * trends.get(brand, 1.0)
