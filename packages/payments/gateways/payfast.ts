export const PayFast = {
  process: async (amount: number, user: string) => {
    const data = {
      merchant_id: process.env.PAYFAST_ID,
      amount: amount.toFixed(2),
      item_name: "EarnNexus Pro Access",
      email_address: user
    };
    // Generate signature and redirect to PayFast for ZAR/EFT
    return `https://www.payfast.co.za/eng/process?merchant_id=${data.merchant_id}&amount=${data.amount}`;
  }
};
