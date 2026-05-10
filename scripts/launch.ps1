# Genesis Launch Script
Write-Host "🔥 Activating EarnNexus Immortal Stack" -ForegroundColor Cyan

# Check Docker
if (!(Get-Process "Docker Desktop" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Launch Docker Desktop First!" -ForegroundColor Red; exit
}

# Build and Run
docker-compose -f docker-compose.prod.yml up -d --build

# Start Self-Healing in background
Start-Job -ScriptBlock { python .\apps\kernel\repair_engine.py }

Write-Host "✅ Genesis Launch Complete. Modules are LIVE and SELF-HEALING." -ForegroundColor Green
