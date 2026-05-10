# apps/aaa-service/eft_verify.py
import re

def process_bank_notification(email_body):
    """
    Parses incoming FNB/African Bank payment notification emails.
    Links the payment to a user account using the Reference Code.
    """
    # Regex for SA Bank Reference numbers (usually 6-8 digits)
    ref_pattern = r"REF:\s?([A-Z0-9]{6,10})"
    amount_pattern = r"R\s?(\d+\.\d{2})"
    
    ref = re.search(ref_pattern, email_body)
    amount = re.search(amount_pattern, email_body)

    if ref and amount:
        return {"reference": ref.group(1), "amount": float(amount.group(1))}
    return None
