// PayFast Integration for ZAR Transactions
export const PayFastProvider = {
  async generatePaymentUrl(amount: number, userEmail: string, orderId: string) {
    const merchantId = process.env.PAYFAST_MERCHANT_ID;
    const merchantKey = process.env.PAYFAST_MERCHANT_KEY;
    const returnUrl = "https://earnnexus.co.za/dashboard/success";
    
    // Direct EFT is enabled by default in PayFast
    const data = {
      merchant_id: merchantId,
      merchant_key: merchantKey,
      amount: amount.toFixed(2),
      item_name: "EarnNexus Monthly Access",
      email_address: userEmail,
      m_payment_id: orderId,
      return_url: returnUrl,
    };

    const signature = this.generateSignature(data);
    return `https://www.payfast.co.za/eng/process?${new URLSearchParams({ ...data, signature })}`;
  },

  generateSignature(data: any) {
    // Implement MD5 hashing with your PayFast Passphrase here
    return "hashed_signature_string";
  }
};
