@echo off

REM Stocker le chemin complet du fichier source
set "sourcePath=%~dp0joystick-in-windows.py"

REM Vérifier si le fichier source existe avant de demander les droits d'administrateur
if not exist "%sourcePath%" (
    echo Le fichier source n'existe pas.
    pause
    exit /b
)

REM Vérifier si l'utilisateur a les droits d'administrateur
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    REM Si l'utilisateur n'a pas les droits d'administrateur, redémarrer le script avec les droits d'administrateur
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

REM Spécifiez le chemin complet du dossier de démarrage
set "destinationPath=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"


REM Copie le fichier vers le dossier de démarrage
copy /Y "%sourcePath%" "%destinationPath%"

echo Copié avec succès !