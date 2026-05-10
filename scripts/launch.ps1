# scripts/launch.ps1 (Fragment)
Write-Host "🚀 INITIALIZING EARNNEXUS GENESIS LAUNCH..." -ForegroundColor Cyan

# SAFETY LOCK: Disable all Direct-to-User communication modules
$env:ALLOW_DIRECT_DM = "FALSE"
$env:ALLOW_COLD_CALLS = "FALSE"
$env:MARKETING_MODE = "INBOUND_ONLY"

# Start Leo (The Architect)
python apps/content-engine/generator.py --batch 50
Write-Host "✅ 50 Unique Posters Created. Awaiting Approval in Portal..." -ForegroundColor Green
