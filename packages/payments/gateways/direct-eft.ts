/**
 * Direct EFT Gateway (Non-API Verification)
 * Standardized instructions for FNB and African Bank.
 */

export const DirectEFTInstructions = {
  fnb: {
    account_name: "EarnNexus Business",
    account_number: "62XXXXXXXXX",
    branch_code: "250655",
    bank: "First National Bank"
  },
  african_bank: {
    account_name: "EarnNexus Business",
    account_number: "12XXXXXXXXX",
    branch_code: "430000",
    bank: "African Bank"
  },
  process: (orderId: string) => {
    return `
      PLEASE NOTE: 
      1. Use Reference: ${orderId}
      2. Send Proof of Payment to: payments@earnnexus.com
      3. Access is automatically granted once our agent verifies the deposit.
    `;
  }
};
