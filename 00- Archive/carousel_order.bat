@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════
echo   📱 Instagram Carousel Organizer
echo   📚 راست یا چپ؛ میانه کجاست؟
echo ═══════════════════════════════════════════════════
echo.

set "SRCDIR=D:\Code\Apps\chatMergerTool\output\Left-Right-The-Middle\slides\png"

if not exist "%SRCDIR%" (
    echo ❌ PNG directory not found: %SRCDIR%
    echo    Run the Python script first, then convert SVGs to PNG.
    pause
    exit /b
)

echo 📁 Source: %SRCDIR%
echo.
echo 📋 Carousel Order:
echo    1. Cover ^& Introduction
echo    2. Key Question
echo    3. Timeline
echo    4-5. Left ^& Right Spectrum
echo    6-7. Philosophers ^& Economics
echo    8-10. Famous Debates
echo    11-13. Intellectual Converts
echo    14-15. Overton Window ^& Horseshoe
echo    16-17. More Debates
echo    18-19. Facts ^& Book Structure  
echo    20. Final CTA
echo.

echo ✅ Files are already numbered in carousel order!
echo.
echo 💡 Upload to Instagram in numerical order (01-20)
echo.
pause
