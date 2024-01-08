@echo off

REM Vérifier si l'utilisateur a les droits d'administrateur
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    REM Si l'utilisateur n'a pas les droits d'administrateur, redémarrer le script avec les droits d'administrateur
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

REM Le script continue ici s'il est exécuté avec les droits d'administrateur

REM Spécifiez le chemin complet du dossier de démarrage
set "destinationPath=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"

REM Vérifier si le fichier existe dans le dossier de démarrage avant de le supprimer
if exist "%destinationPath%\joystick-in-windows.py" (
    del "%destinationPath%\joystick-in-windows.py"
    echo Fichier supprimé avec succès !
) else (
    echo Le fichier n'existe pas dans le dossier de démarrage.
)

pause
