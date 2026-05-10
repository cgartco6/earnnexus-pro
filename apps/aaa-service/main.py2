from fastapi import FastAPI, Depends
from agents.outreach import LeadGenAgent
from packages.auth import get_current_user

app = FastAPI(title="EarnNexus Core")

@app.post("/run-track/aaa")
async def start_agency_workflow(niche: str, user=Depends(get_current_user)):
    """Triggers the B2B Lead Gen Agent to find high-ticket clients."""
    agent = LeadGenAgent(niche=niche)
    results = await agent.execute_outreach()
    return {"status": "success", "data": results}

@app.get("/stats/revenue")
async def get_global_revenue(user=Depends(get_current_user)):
    """Aggregates income from all three modules."""
    # Logic to pull from Stripe + Manual entries
    return {"total_rands": 15400.00} 
