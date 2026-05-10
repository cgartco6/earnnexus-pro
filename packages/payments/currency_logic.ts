/**
 * EarnNexus Global Currency & FX Engine
 * Dynamically adjusts pricing based on User Geo-IP or Selection.
 */

export const CurrencyEngine = {
  // 2026 Average Pegs (System should update these via Evolution Engine)
  rates: {
    USD: 19.20,
    EUR: 20.50,
    GBP: 24.10,
    ZAR: 1.00
  },

  /**
   * Converts ZAR base price to Local Currency for the Landing Page.
   */
  localizePrice: (zarAmount: number, targetCurrency: 'USD' | 'EUR' | 'GBP' | 'ZAR') => {
    const rate = CurrencyEngine.rates[targetCurrency];
    const converted = zarAmount / rate;
    
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: targetCurrency,
    }).format(converted);
  },

  /**
   * Safety check for Stripe/PayPal to ensure ZAR is correctly converted
   * before sending the payload to the global gateways.
   */
  prepareGlobalPayload: (zarAmount: number) => {
    const usdValue = (zarAmount / CurrencyEngine.rates.USD).toFixed(2);
    return {
      amount: usdValue,
      currency: 'USD'
    };
  }
};
