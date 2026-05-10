/**
 * Aegis Impulse Buy Triggers
 * Based on high-velocity retail psychology (Temu/Amazon style).
 */

export const ImpulseTriggers = {
  getSocialProof: () => {
    const numbers = [142, 89, 256, 12];
    const city = ["Cape Town", "London", "Dubai", "New York"];
    return `${numbers[Math.floor(Math.random() * 4)]} people in ${city[Math.floor(Math.random() * 4)]} just joined.`;
  },

  getScarcityTimer: () => {
    return "OFFER ENDS IN: 14:59"; // Hardcoded to reset on refresh for psychology
  },

  getDiscountLabel: (zarPrice: number) => {
    const original = zarPrice * 2.5; // Artificial 'Original' price for anchor bias
    return `Was R${original.toFixed(0)} -> NOW R${zarPrice}`;
  }
};
