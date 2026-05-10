// stripe.ts
import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET!, { apiVersion: '2023-10-16' });

export const createGlobalSession = async (priceId: string) => {
  return await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{ price: priceId, quantity: 1 }],
    mode: 'subscription',
    success_url: `${process.env.DOMAIN}/success`,
  });
};
