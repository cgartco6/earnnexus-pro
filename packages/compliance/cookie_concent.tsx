export const CookieConsent = () => (
  <div className="fixed bottom-0 bg-black text-[#39FF14] p-4 border-t border-[#39FF14]">
    <p>This system is POPIA (South Africa) and GDPR compliant. By launching, you agree to secure data processing.</p>
    <button onClick={() => window.close()}>Accept & Proceed</button>
  </div>
);
