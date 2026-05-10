export async function safeAIRequest(prompt: string) {
  try {
    // Attempt primary model execution
    const res = await fetch('/api/ai/primary', { method: 'POST', body: JSON.stringify({ prompt }) });
    return await res.json();
  } catch (e) {
    console.error("Primary AI Failed. Healing and Re-routing...");
    // Trigger evolution_log and swap to fallback
    return { error: "Self-healing in progress, please retry." };
  }
}
