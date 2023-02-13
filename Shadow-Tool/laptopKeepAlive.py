
import os

os.system("@ECHO OFF)
os.system("cd %TEMP%")
os.system("powershell -command Powercfg SETACVALUEINDEX 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 000")
os.system("powerhsell -command Powercfg SETDCVALUEINDEX 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 000")
os.system(powerhsell -command exit")