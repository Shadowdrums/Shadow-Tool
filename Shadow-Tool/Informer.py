#!python3
# -*- coding: utf-8 -*-
########################################
# Informer.py
#	reconnaissance tool
#
########################################
#
SoftName="ShadowTools-Informer"
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
os.system("powershell.exe echo 'Informer Is Starting'")
os.system("powershell -command mkdir .\\INFORMER")
os.system("powershell -command echo 'Computer And User Name:' > .\\INFORMER\\Informer.txt")
os.system("powershell -command whoami >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'IP-Address:' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command ipconfig /all >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'ARP:' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command arp -a >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'OS Name:' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command (get-wmiobject win32_operatingsystem).name >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'CS OS Name:' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command (get-wmiobject win32_operatingsystem).csname >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'OS Architecture:' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command (get-wmiobject win32_operatingsystem).osarchitecture >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'Thank You For Using Informer' >> .\\INFORMER\\Informer.txt")
os.system("powershell -command echo 'Informer Has Finished, Thank You And Good Bye'")
os.system("powershell -command sleep 3")
os.system("powershell -command exit")

