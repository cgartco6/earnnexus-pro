// apps/portal/src/components/ApprovalBoard.tsx
import React, { useState } from 'react';

interface Poster {
  id: string;
  url: string;
  caption: string;
  platform: string;
}

export default function ApprovalBoard({ initialPosters }: { initialPosters: Poster[] }) {
  const [posters, setPosters] = useState(initialPosters);

  const handleAction = (id: string, action: 'APPROVE' | 'REJECT') => {
    // Send to /api/content/status-update
    setPosters(prev => prev.filter(p => p.id !== id));
    console.log(`${action} applied to ${id}`);
  };

  return (
    <div className="min-h-screen bg-black p-8 font-mono text-white">
      <header className="border-b border-[#39FF14] pb-4 mb-8">
        <h1 className="text-3xl text-[#39FF14] font-bold">GENESIS APPROVAL BOARD</h1>
        <p className="text-gray-400">Review Inbound Assets for Compliance & Visual Impact</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {posters.map(poster => (
          <div key={poster.id} className="border border-zinc-800 bg-zinc-900 overflow-hidden rounded-lg">
            <img src={poster.url} alt="AI Generated Poster" className="w-full h-auto" />
            <div className="p-4">
              <p className="text-xs text-[#39FF14] mb-2 uppercase">{poster.platform}</p>
              <p className="text-sm italic text-gray-300 mb-4">"{poster.caption}"</p>
              <div className="flex gap-2">
                <button 
                  onClick={() => handleAction(poster.id, 'APPROVE')}
                  className="flex-1 bg-[#39FF14] text-black font-bold py-2 hover:bg-white transition-colors"
                >
                  APPROVE
                </button>
                <button 
                  onClick={() => handleAction(poster.id, 'REJECT')}
                  className="flex-1 border border-red-600 text-red-600 font-bold py-2 hover:bg-red-600 hover:text-white transition-colors"
                >
                  REJECT
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
