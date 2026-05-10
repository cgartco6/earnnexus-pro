// apps/portal/src/components/AdApproval.tsx
export default function AdApproval({ pendingAds }) {
  const handleApprove = (adId) => {
    // Triggers the Governor to schedule the post
  };

  return (
    <div className="bg-black p-4 border border-[#39FF14]">
      <h2 className="text-[#39FF14] font-bold">AD APPROVAL QUEUE (ALEX AGENT)</h2>
      {pendingAds.map(ad => (
        <div key={ad.id} className="flex items-center gap-4 mt-4">
          <img src={ad.imageUrl} width={100} className="border border-white" />
          <div className="flex-1">
            <p className="text-white text-xs">{ad.caption}</p>
            <p className="text-[#39FF14] text-xs">Target: {ad.targetPlatform}</p>
          </div>
          <button onClick={() => handleApprove(ad.id)} className="bg-[#39FF14] p-2 font-bold text-black text-xs">
            LAUNCH AD
          </button>
        </div>
      ))}
    </div>
  );
}
