/**
 * EarnNexus Local Revenue Hub: Direct EFT
 * Hardened for South African Banking Standards.
 */

interface BankAccount {
  bankName: string;
  accountHolder: string;
  accountNumber: string;
  branchCode: string;
  accountType: string;
}

export const BankDetails: Record<string, BankAccount> = {
  FNB: {
    bankName: "First National Bank (FNB)",
    accountHolder: process.env.FNB_ACC_HOLDER || "EarnNexus Business",
    accountNumber: process.env.FNB_ACC_NUMBER || "62XXXXXXXXX",
    branchCode: process.env.FNB_BRANCH_CODE || "250655",
    accountType: "Business Cheque",
  },
  AFRICAN_BANK: {
    bankName: "African Bank",
    accountHolder: process.env.AFRICAN_BANK_ACC_HOLDER || "EarnNexus Business",
    accountNumber: process.env.AFRICAN_BANK_ACC_NUMBER || "12XXXXXXXXX",
    branchCode: process.env.AFRICAN_BANK_BRANCH_CODE || "430000",
    accountType: "Transactional",
  }
};

export function generateEFTInstructions(orderId: string, amount: number, bank: 'FNB' | 'AFRICAN_BANK'): string {
  const details = BankDetails[bank];
  return `
    --- PAYMENT INSTRUCTIONS ---
    Please pay R${amount.toFixed(2)} to:
    Bank: ${details.bankName}
    Account Holder: ${details.accountHolder}
    Account Number: ${details.accountNumber}
    Branch Code: ${details.branchCode}
    Reference: ${orderId}

    IMPORTANT: Send Proof of Payment (PDF) to payments@earnnexus.com
    Access will be granted once the funds reflect.
  `;
}
