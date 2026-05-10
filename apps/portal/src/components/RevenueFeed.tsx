export default function RevenueFeed({ data }) {
  return (
    <div className="p-6 bg-zinc-950 border border-neon-green rounded-lg shadow-[0_0_15px_rgba(57,255,20,0.3)]">
      <h2 className="text-[#39FF14] font-mono text-xl mb-4">LIVE REVENUE (ZAR/USD)</h2>
      <div className="space-y-3">
        <div className="flex justify-between border-b border-zinc-800 pb-2">
          <span>Stripe (Global)</span>
          <span className="text-white">${data.stripe_total}</span>
        </div>
        <div className="flex justify-between border-b border-zinc-800 pb-2 text-[#39FF14]">
          <span>PayFast (SA EFT)</span>
          <span>R {data.payfast_total}</span>
        </div>
      </div>
    </div>
  );
}
