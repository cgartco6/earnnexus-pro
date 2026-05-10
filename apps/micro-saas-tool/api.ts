import { stripe } from "@packages/payments";

export async function POST(req: Request) {
  const { userId, prompt } = await req.json();
  
  // 1. Check if user has an active subscription
  const isSubscribed = await stripe.checkSubscription(userId);
  if (!isSubscribed) return new Response("Subscription Required", { status: 402 });

  // 2. Execute High-Value AI Logic
  const result = await CoreAI.generateSEOReport(prompt);
  return Response.json(result);
}
