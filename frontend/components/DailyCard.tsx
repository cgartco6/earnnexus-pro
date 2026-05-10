// frontend/components/DailyCard.tsx
import React from 'react';

export const DailyCard = ({ day, title, status, reward }) => {
  return (
    <div className="p-4 border rounded-xl shadow-sm bg-white">
      <h3 className="text-lg font-bold">Day {day}: {title}</h3>
      <p className="text-sm text-gray-500">Goal: Earn your first $5 using AI Copywriting.</p>
      <div className="mt-4 flex justify-between items-center">
        <span className={`badge ${status === 'complete' ? 'bg-green-100' : 'bg-blue-100'}`}>
          {status}
        </span>
        <button className="btn-primary">Start Task</button>
      </div>
    </div>
  );
};
