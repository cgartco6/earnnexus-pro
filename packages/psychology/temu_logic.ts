/**
 * Temu-Style Impulse Logic
 * Triggers: Scarcity, Social Proof, and Gamified Discounts.
 */
export const ImpulseTriggers = {
  getUrgencyString: () => {
    const minutes = Math.floor(Math.random() * 15) + 1;
    return `🔥 FLASH DEAL: Expires in ${minutes}m!`;
  },

  getScarcityString: () => {
    const stock = Math.floor(Math.random() * 7) + 2;
    return `⚠️ Only ${stock} slots remaining for today's price.`;
  },

  formatTemuPrice: (original: number, discount: number) => {
    const final = original - (original * (discount / 100));
    return `R${original} -> R${final.toFixed(2)} (SAVE ${discount}%)`;
  }
};
