export default function RevenueFeed({ earnings }) {
  return (
    <div className="bg-black text-[#39FF14] p-6 rounded-lg border border-[#39FF14]">
      <h2 className="text-2xl font-mono mb-4 uppercase tracking-tighter">Live Revenue Stream</h2>
      <div className="space-y-2">
        {earnings.map((e) => (
          <div key={e.id} className="flex justify-between border-b border-[#39FF14]/20 pb-2">
            <span>{e.source}</span>
            <span className="font-bold">R {e.amount}</span>
          </div>
        ))}
      </div>
      <button className="mt-6 w-full bg-[#39FF14] text-black py-2 font-bold hover:bg-white transition-colors">
        WITHDRAW TO BANK
      </button>
    </div>
  );
}
