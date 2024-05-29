@echo off
REM Abrufen der lokalen IP-Adresse
for /f "tokens=13" %%i in ('ipconfig ^| findstr /r /c:"IPv4-Adresse" /c:"IPv4 Address"') do set "localIP=%%i"
echo IP-Adresse des Servers: %localIP%
echo Schreibe dir jetzt die IP adresse ab!
echo Drücke dann einen knopf, so dass der server starten kann!
pause
python server.py