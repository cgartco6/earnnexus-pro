# EarnNexus Genesis Master Launcher
# Run this as Administrator

Write-Host "🚀 INITIALIZING EARNNEXUS IMMORTAL STACK..." -ForegroundColor Cyan

# 1. Environment Check
if (!(Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Error: Docker is not installed. Please install Docker Desktop for Windows." -ForegroundColor Red
    exit
}

# 2. Variable Injection
if (Test-Path ".env.production") {
    Write-Host "✅ Environment Loaded." -ForegroundColor Green
} else {
    Write-Host "⚠️ Warning: .env.production missing. Using .env.example defaults." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env.production"
}

# 3. Security Lockdown
$env:MARKETING_MODE = "INBOUND_ONLY"
$env:COMPLIANCE_LEVEL = "POPIA_NCC_2026"

# 4. Deployment
Write-Host "📦 Building Containers..." -ForegroundColor Blue
docker-compose up --build -d

Write-Host "✨ Genesis Launch Complete. Access Portal at http://localhost:3000" -ForegroundColor Green
Write-Host "❤️ Heartbeat Monitor is active in the background." -ForegroundColor White
