from fastapi import FastAPI
from agents.outreach import OutreachAgent
from fpdf import FPDF # For PDF generation

app = FastAPI()

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/generate-proposal")
async def create_proposal(client_name: str):
    # Real PDF Creation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"AI Automation Proposal for {client_name}", ln=1, align='C')
    pdf.output(f"proposals/{client_name}_proposal.pdf")
    return {"message": "PDF Created", "path": f"/{client_name}_proposal.pdf"}
