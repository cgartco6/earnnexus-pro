# bootstrap.ps1
Write-Host "🚀 Initializing EarnNexus Bootstrap for Windows 10 Pro..." -ForegroundColor Cyan

# 1. Check for Administrative Privileges
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "CRITICAL: Please run this script as Administrator."
    exit
}

# 2. Check for Docker Desktop
if (!(Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Docker not found. Install Docker Desktop with Hyper-V enabled." -ForegroundColor Red
    exit
}

# 3. Setup Python Virtual Environment
if (!(Test-Path ".\venv")) {
    Write-Host "📦 Creating Python Virtual Environment..." -ForegroundColor Yellow
    python -m venv venv
}

# 4. Install Dependencies
Write-Host "🛠️ Installing Hardened Dependencies..." -ForegroundColor Yellow
.\venv\Scripts\pip install -r .\apps\kernel\requirements.txt

Write-Host "✅ Bootstrap Complete. System is ready for Genesis." -ForegroundColor Green
