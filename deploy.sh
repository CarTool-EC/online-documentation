# deploy.ps1 — Publica la documentacion en GitHub Pages sin usar GitHub Actions.
#
# Que hace:
#   1. Comprueba que estas en "main" y que no tienes cambios sin commitear
#      (si los tienes, PARA y te avisa -- el commit lo escribes tu a mano).
#   2. Construye el HTML con Sphinx.
#   3. Publica ese HTML en la rama "gh-pages" con ghp-import.
#
# Uso:
#   .\deploy.ps1
#
# Requiere tener instalado: sphinx (via requirements.txt) y ghp-import
#   pip install -r requirements.txt ghp-import
#
# La primera vez puede que necesites permitir ejecutar scripts en PowerShell:
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# Si cualquier comando falla, detener el script en vez de seguir a medias
$ErrorActionPreference = "Stop"

function Fallar($texto) {
    Write-Host $texto -ForegroundColor Red
    exit 1
}

Write-Host "==> 1. Comprobando rama actual..." -ForegroundColor Cyan
$ramaActual = git branch --show-current

if ($ramaActual -ne "main") {
    Fallar "Estas en la rama '$ramaActual', no en 'main'. Cambia a main antes de ejecutar esto (git checkout main)."
}

Write-Host "==> 2. Comprobando que no hay cambios sin commitear..." -ForegroundColor Cyan
$cambiosPendientes = git status --porcelain

if ($cambiosPendientes) {
    Write-Host "Tienes cambios sin commitear en main:" -ForegroundColor Yellow
    git status --short
    Fallar "Commitea y sube tus cambios tu mismo antes de publicar (git add / git commit / git push), y vuelve a ejecutar este script."
}

Write-Host "Todo commiteado. Trayendo la ultima version de main desde GitHub..." -ForegroundColor Green
git pull origin main

Write-Host "==> 3. Construyendo el HTML con Sphinx..." -ForegroundColor Cyan
$carpetaTemp = Join-Path $env:TEMP ("salida-doc-" + [guid]::NewGuid().ToString().Substring(0,8))

sphinx-build -b html docs $carpetaTemp
if ($LASTEXITCODE -ne 0) {
    Fallar "El build de Sphinx fallo. Revisa los errores de arriba, no se publico nada."
}

Write-Host "==> 4. Publicando en gh-pages..." -ForegroundColor Cyan
ghp-import -n -p -f $carpetaTemp
if ($LASTEXITCODE -ne 0) {
    Fallar "Fallo al publicar en gh-pages. Revisa los errores de arriba."
}

Write-Host "==> 5. Limpiando carpeta temporal..." -ForegroundColor Cyan
Remove-Item -Recurse -Force $carpetaTemp

Write-Host ""
Write-Host "Listo. En 1-2 minutos veras los cambios en:" -ForegroundColor Green
Write-Host "https://cartool-ec.github.io/online-documentation/" -ForegroundColor Green