@echo off
>>"%~dp0session-log.txt" echo.
>>"%~dp0session-log.txt" echo [%date% %time%] %CD%^> %*
%* 1>"%TEMP%\k8s-out.txt" 2>&1
type "%TEMP%\k8s-out.txt"
type "%TEMP%\k8s-out.txt" >>"%~dp0session-log.txt"
