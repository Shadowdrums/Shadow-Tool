
import os

os.system("@ECHO OFF")
os.system("cd %TEMP%")
os.system("powershell -command echo 'Preparing To Enable RDP'")
os.system("powershell -command set-executionpolicy remotesigned")
os.system("powershell -command Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\' -Name 'fDenyTSConnections' -Value 0")
os.system("powershell -command Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\' -Name 'UserAuthentication' -Value 1")
os.system("powershell -command Enable-NetFirewallRule -DisplayGroup 'Remote Desktop'")
os.system("powershell -command echo 'RDP Is Ready'")
os.system("powershell -command exit")
