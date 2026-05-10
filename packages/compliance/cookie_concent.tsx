export const LegalBanner = () => {
  return (
    <div className="fixed bottom-0 w-full bg-slate-900 text-white p-4 text-xs">
      <p>
        By using EarnNexus, you agree to our <strong>POPIA</strong> and <strong>GDPR</strong> compliant 
        data processing policies. We use AI to optimize your experience.
      </p>
      <button className="bg-[#39FF14] text-black px-4 py-1 mt-2 font-bold">ACCEPT</button>
    </div>
  );
};
