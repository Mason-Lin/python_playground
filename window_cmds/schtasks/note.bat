exit

schtasks.exe /create /sc once /st 23:26 /tn log /tr "c:\windows\system32\notepad.exe"
schtasks.exe /query /tn log
schtasks.exe /delete /tn log /f
