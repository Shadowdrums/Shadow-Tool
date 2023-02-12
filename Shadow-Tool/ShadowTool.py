#!python3
# -*- coding: utf-8 -*-
########################################
# ShadowTool.py
#	ShadowTool Command Shell
#	Access Terminal for executing other packages from Shadow Tool Set
########################################
#
SoftName="ShadowTool"
ENCODED_CONFIG='null=='#/ENCODEDCONF
#
########################################
#		TO DO / IDEAS: 
# have a picture
# have a help terminal 
# be able to activate several programs
# password(key) activated
########################################
# Contributors:
#	Shadowdrums
#	DJ Stomp
#	toroidist
########################################
#
#
########################################
# IMPORTS
# 	they should always go at the top
########################################
#

# first we will set a standard wait time, to make loading modules look fun
lt=0.08
print("###########################")
print("# ShadowTool Initializing #")
print("###########################")

# time for wait
from time import sleep as wait
print("# -imported time"); wait(lt)

# pickle  for save/load of config files
import pickle
print("# -imported pickle"); wait(lt)

# base64 for encoding/decoding of the config
from base64 import b64encode, b64decode
print("# -imported base64"); wait(lt)

# os for system calls
import os
print("# -imported os"); wait(lt)

# sys for core functions like args and clean exit
import sys
print("# -imported sys"); wait(lt)

import random as R
print("# -imported random as R"); wait(lt)
# /imports


#sys.path.insert(0, 'utils/')
#from vox import *
#print("# -imported vox"); wait(lt)


#####################################################################
# ASCII ART / TEXT / CONFIG / TABLES
#####################################################################


# GHOST ART
GhostArt	=	{
	"SHADOW"		:	[
		"  .-')     ('-. .-.    ('-.      _ .-') _                  (`\ .-') /`",
		" ( OO ).  ( OO )  /   ( OO ).-. ( (  OO) )                  `.( OO ),'",
		"(_)---\_) ,--. ,--.   / . --. /  \     .'_   .-'),-----. ,--./  .--.  ",
		"/    _ |  |  | |  |   | \-.  \   ,`'--..._) ( OO'  .-.  '|      |  |  ",
		"\  :` `.  |   .|  | .-'-'  |  |  |  |  \  ' /   |  | |  ||  |   |  |, ",
		" '..`''.) |       |  \| |_.'  |  |  |   ' | \_) |  |\|  ||  |.'.|  |_)",
		".-._)   \ |  .-.  |   |  .-.  |  |  |   / :   \ |  | |  ||         |  ",
		"\       / |  | |  |   |  | |  |  |  '--'  /    `'  '-'  '|   ,'.   |  ",
		" `-----'  `--' `--'   `--' `--'  `-------'       `-----' '--'   '--'  ",
				],
	"TOOL"		:	[
		" .-') _                                        ",
		"(  OO) )                                       ",
		"/     '._   .-'),-----.  .-'),-----.  ,--.     ",
		"|'--...__) ( OO'  .-.  '( OO'  .-.  ' |  |.-') ",
		"'--.  .--' /   |  | |  |/   |  | |  | |  | OO )",
		"   |  |    \_) |  |\|  |\_) |  |\|  | |  |`-' |",
		"   |  |      \ |  | |  |  \ |  | |  |(|  '---.'",
		"   |  |       `'  '-'  '   `'  '-'  ' |      | ",
		"   `--'         `-----'      `-----'  `------' ",
				],
	"FULL"		:	[
		" .-')     ('-. .-.    ('-.      _ .-') _                  (`\ .-') /`   .-') _                                         ",
		"( OO ).  ( OO )  /   ( OO ).-. ( (  OO) )                  `.( OO ),'  (  OO) )                                        ",
		"(_)---\_) ,--. ,--.   / . --. /  \     .'_   .-'),-----. ,--./  .--.    /     '._   .-'),-----.  .-'),-----.  ,--.     ",
		"/    _ |  |  | |  |   | \-.  \   ,`'--..._) ( OO'  .-.  '|      |  |    |'--...__) ( OO'  .-.  '( OO'  .-.  ' |  |.-') ",
		"\  :` `.  |   .|  | .-'-'  |  |  |  |  \  ' /   |  | |  ||  |   |  |,   '--.  .--' /   |  | |  |/   |  | |  | |  | OO )",
		"'..`''.) |       |  \| |_.'  |  |  |   ' | \_) |  |\|  ||  |.'.|  |_)      |  |    \_) |  |\|  |\_) |  |\|  | |  |`-' |",
		".-._)   \ |  .-.  |   |  .-.  |  |  |   / :   \ |  | |  ||         |       |  |      \ |  | |  |  \ |  | |  |(|  '---.'",
		"\       / |  | |  |   |  | |  |  |  '--'  /    `'  '-'  '|   ,'.   |       |  |       `'  '-'  '   `'  '-'  ' |      | ",
		" `-----'  `--' `--'   `--' `--'  `-------'       `-----' '--'   '--'       `--'         `-----'      `-----'  `------' ",
			]
	}
# /GhostArt




# WINDOWS COMMAND PROMPT COLOURS TABLE
WINNT_CONSOLE_COLORS={
	# for lookups
	"0"	:	"Black",
	"1"	:	"Blue",
	"2"	:	"Green",
	"3"	:	"Aqua",
	"4"	:	"Red",
	"5"	:	"Purple",
	"6"	:	"Yellow",
	"7"	:	"White",
	"8"	:	"Gray",
	"9"	:	"LightBlue",
	"A"	:	"LightGreen",
	"B"	:	"LightAqua",
	"C"	:	"LightRed",
	"D"	:	"LightPurple",
	"E"	:	"LightYellow",
	"F"	:	"BrightWhite",
	# for setting color prefs
	"Black"			:	"0",
	"Blue"			:	"1",
	"Green"			:	"2",
	"Aqua"			:	"3",
	"Red"			:	"4",
	"Purple"		:	"5",
	"Yellow"		:	"6",
	"White"			:	"7",
	"Gray"			:	"8",
	"LightBlue"		:	"9",
	"LightGreen"	:	"A",
	"LightAqua"		:	"B",
	"LightRed"		:	"C",
	"LightPurple"	:	"D",
	"LightYellow"	:	"E",
	"BrightWhite"	:	"F",
	}
# /WinNT_Colours

# Example dictionary structure showing the template used for CONFIG
TEMPLATE	=	{
	
	# the name of a script which has values kept for it here
	"Script"	:	{
		
		# name of the script, with proper capitalization in case that matters
		# used for calling/executing, copying, and embedding a config within, the script
		"scriptname"	:	"Client.py",		#
		
		# path to that script's configuration file
		# make sure the config paths used here match the paths read by the scripts
		# a possible upgrade to this would be for the configs to be named by
		# sys.argv[0] in each script, to get the actual name. for example:
		# sys.argv[0].split("/")[-1].split("\\")[-1].split(".")[0] will get the filename
		# without any of the path, whether on unix or windows etc, and without .py
		"configpath"	:	"./client.shadow",	# 
		
		# create a placeholder here, to be filled in by the LoadConfig on launch
		"current"		:	{},
		
		# defaults to revert to, if no config file is present
		"defaults"		:	{
			
			# specific settings which will be loaded if no config file is present
			"settings_1"	:	'example', 			# comments for each 
			"settings_2"	:	65535,				# 
							},
					},
			}
# /TEMPLATE


# Defaults and paths for configurations
#	additional config sets can be added by following the same format
CONFIG	=	{
	"client"	:	{
		"scriptname"	:	"Client.pyw",		#
		"configpath"	:	"./Client.shadow",	# 
		"current"		:	{},
		"defaults"		:	{
			"SERVER_HOST"	:	'FF.FF.FF.FF', 		#host ip
			"SERVER_PORT"	:	1189,				# 
			"BUFFER_SIZE"	:	1024 * 128,			# 128KB max size of messages, feel free to increase
			"SEPARATOR"		:	"<sep>",			# separator string for sending 2 messages in one go
			"mode"			:	"auto",				# 
							},
					},
	"server"	:	{
		"scriptname"	:	"Server.py",		#
		"configpath"	:	"./Server.shadow",	# 
		"current"		:	{},
		"defaults"		:	{
			"SERVER_HOST"	:	'FF.FF.FF.FF', 		# host ip
			"SERVER_PORT"	:	1189,				# 
			"BUFFER_SIZE"	:	1024 * 128,			# 128KB max size of messages, feel free to increase
			"SEPARATOR"		:	"<sep>",			# separator string for sending 2 messages in one go
			"mode"			:	"auto",				# 
							},
		
					},
	"synflood"	:	{
		"scriptname"	:	"SYNflood.py",		#
		"configpath"	:	"./SYNflood.shadow",
		"current"		:	{},
		"defaults"		:	{
			"TARGET_IP"		:	"FF.FF.FF.FF",	# target IP address (should be a testing router/firewall)
			"TARGET_PORT"	:	80,					# the target port u want to flood
							},
					},
	"xks"	:	{
		"scriptname"	:	"xks.py",		#
		"configpath"	:	"./xks.shadow",
		"current"		:	{},
		"defaults"		:	{
			"SERVER_HOST"	:	"127.0.0.1",		# the server to receive our data - could be .onion too
			"SERVER_PORT"	:	10080,				# destination port for sent xkeyscore data
							},
					},
			}
# /CONFIG





#####################################################################
# BASIC FUNCTION DEFINITIONS
#####################################################################



# CLEAR SCREEN
def cls():
	os.system('cls')
	return
# /cls


# LINE BREAK
def br(lines=1,CHAR="#"):
	# basic print blank line (print break), with # for aesthetics
	# you can specify how many lines you want blanked out
	i=0
	while(i<lines):
		# and could get rid of the leading # its just for looks
		print(CHAR," ")
		i+=1
# /br


#
def CenteredText(text_input="",printing=True,terminal_width=os.get_terminal_size().columns,border_char=" "):
	if(len(text_input)>terminal_width-4):
		spaces=0
	else:
		spaces=(terminal_width-4)-len(text_input)
	text_output=border_char+" "
	if(spaces/2 != int(spaces/2)):
		text_output+=" "
	i=1
	while(i<=spaces/2):
		text_output+=" "
		i+=1
	text_output+=text_input
	i=1
	while(i<=spaces/2):
		text_output+=" "
		i+=1
	text_output+=" "+border_char
	if(printing):
		if(terminal_width==80):
			print(text_output,end="")
		else:
			print(text_output)
	return text_output
# /CenteredText


# PRINT SAMELINE
def print_sameline(text):
	print(text, end="")
# /PrintSameline


# PRANK
def prank(user_string='deleting windows system files...'):
	itr=0
	bucket=[]
	nof=7000
	#
	while(itr<R.randint(nof,nof*2)):
		bucket.append(str(R.randint(100000,999999)))
		itr+=1
	i=0
	itr=0
	for item in bucket:
		i=bucket.index(item)
		#print(i)
		percentage=int(i/len(bucket)*100)
		perdecum=int(i/len(bucket)*10)
		i+=1
		statusbar='['
		x=0
		while(x<=perdecum):
			statusbar+=u"\u2588"
			x+=1
		while(len(statusbar)<11):
			statusbar+=' '
		statusbar+=']'
		printline_a="# "+user_string+"    "
		printline_b='#                                                                '+statusbar+'  '+"\r"
		printline_c=' '+str(percentage)+"% complete"
		printline=printline_a + printline_c+"\r"
		print_sameline(printline_b)
		print_sameline(printline)
		'''
		br(3)
		print("i: "+str(i)+"     /     "+"x: "+str(x))
		print("percentage: "+str(percentage))
		print("perdecum: "+str(perdecum))
		sleep(0.02)
		'''
		st=3/R.randint(1,3000)
	#	print('st: '+str(st))
		wait(st)
		#
	#
# /prank



# SET TITLE
def set_title():
	# this is a simplified set_title over the one in vox, only supports windows
	os.system('TITLE '+SoftName)
	return
# /SetTitle









########################################
# CONFIGURATION FUNCTIONS
########################################


# LOAD CONFIGURATIONS
def LoadConfig(Script="all",CONFIG=CONFIG):
	#
	# this creates a list of the subdicts inside CONFIG,
	# the purpose is so that adding additional config sets later is easier
	CONFIG['configs']=[]
	#
	# Config would be the name of each subdict, like ['client', 'server', 'synflood']
	for Config in CONFIG:
		CONFIG['configs'].append(Config)
	# remove "configs" from CONFIG['configs'] because it is silly for it to count itself
	CONFIG['configs'].remove('configs')
	#
	# using .lower() here and keeping the names lowercase in the dict allows
	# the user to type Client or client or SYNFlood or SERVER and all are acceptable
	if(Script.lower() in CONFIG['configs'] or Script.lower()=="all"):
		# check if the user requested to load "all" configs, by typing "all"
		if(Script.lower()=="all"):
			# here we start using "script" in lowercase, to represent each script
			# not specifically a user selected script, and without overwriting "Script"
			for script in CONFIG['configs']:
				try:
					# Load the config file for each script here, if they exist
					with open(CONFIG[script]['configpath'], 'rb') as file:
						CONFIG[script]['current'] = pickle.load(file)
						print(f"Configuration for {script} loaded!")
				except:
					# give option to load defaults, if no config exists
					print(f"{CONFIG[script]['configpath']} does not exist.")
					loadmode="silent"
					if(loadmode=="silent"):
						CONFIG[script]['current'] = CONFIG[script]['defaults']
					else:
						print(f"\nwould you like to load defaults for {script}?")
						print('typing anything other than "yes" will not load defaults')
						dcheck=input(" (yes/*) >> ")
						if(dcheck.lower()=="yes"):
							CONFIG[script]['current'] = CONFIG[script]['defaults']
		else:
			# since we already checked whether it was in the list or all,
			# and already handled the "all" scenario, with this we handle
			# any other
			try:
				with open(CONFIG[Script]['configpath'], 'rb') as file:
					CONFIG[Script]['current'] = pickle.load(file)
					print(f"Configuration for {Script} loaded!")
			except:
				print(f"{CONFIG[Script]['configpath']} does not exist.")
	else:
		print("that is not a valid configuration name")
		print(f"please try 'all' or any of these: {CONFIG['configs']}")
	return CONFIG
# /LoadConfig


# SAVE CONFIGURATIONS
def SaveConfig(Script,TEMP,CONFIG=CONFIG):
	#
	# this is pretty much a copy of LoadConfig, so duplicate comments are erased
	CONFIG['configs']=[]
	#
	for Config in CONFIG:
		CONFIG['configs'].append(Config)
	CONFIG['configs'].remove('configs')
	#
	# This allows SaveConfig to be used without requiring further input,
	#	specify what config subdict you want to save changes to when calling it
	if(Script in CONFIG['configs']): 
		try:
			# Save the config file for each script here
			with open(CONFIG[Script]['configpath'], 'wb') as file:
				pickle.dump(TEMP['current'], file)
				print(f"Configuration for {Script} saved!")
		except:
			# not sure why this would come up, except a path error
			print(f"something fucked up trying to save {CONFIG[Script]['configpath']}")
	else:
		print("that is not a valid configuration name")
		print(f"please try 'all' or any of these: {CONFIG['configs']}")
# /SaveConfig


# EDIT CONFIGURATIONS
def EditConfig(Script="",CONFIG=CONFIG):
	#
	#
	# Create our list of configs in a subdict called... 'configs'
	CONFIG['configs']=[]
	# this does for each key in the dict, append configs with the name of that key
	for Config in CONFIG:
		CONFIG['configs'].append(Config)
	# then remove the key  we created 4 lines up from the list, it doesnt need to count itself
	CONFIG['configs'].remove('configs')
	#
	# if there is a script specified to edit settings for, not let blank=""
	#	then we do not need to start with choosing, we could skip that
	#	so Choosing would be set to False, and which=Script is known
	if(Script.lower() in CONFIG['configs']):
		which=Script
		Choosing=False
	else:
		# If there was no script specified, or it  was not recognized, then Choosing=True
		Choosing=True
	# now that we know whether we will be choosing or not, we can basically start Editing
	Editing=True
	while(Editing):
		# While we are in 'editing' mode (not sure if there is a way to exit yet)
		if(Choosing):
			# if we are choosing, then while we are choosing, there is a choice
			#	this could be prettied up a little btw, its pretty bare right now
			while(Choosing):
				cls()
				br(5)
				CenteredText("Choices are:")
				br()
				#
				CenteredText(str(CONFIG['configs']))
				#for choice in CONFIG['configs']:
				#	CenteredText(choice)
				br(5)
				CenteredText("Which configuration set file would you like to edit?")
				which=input("                  >> ").lower()
				if(which in CONFIG['configs']):
					Choosing=False
				elif(which =="/back"):
					Editing=False
					break
				else:
					print("that is not a valid configuration name")
					print(f"please try one of these: {CONFIG['configs']}")
			# /while(choosing) once the while is broke, the if will be passed also
			# so we move on to the else: (!Choosing) as we have a valid subdict chosen
		else:
			# store that script's options in a TEMP dict, so we are not directly
			# modifying the options, in case we wish to cancel any edits
			TEMP=CONFIG[which]
			# if there are no current values, then we revert to defaults again
			if(len(TEMP['current'])==0):
				TEMP['current']=TEMP['defaults']
			#
			# open space is nice on the eyes
			print("\n")
			#
			# HELP for this operation
			print("# these are the settings currently stored for that script.")
			print("# choose an option to change by typing the name of it's key,")
			print("# '/add' or '/remove' to create or destroy keys,")
			print("# '/defaults' to restore defaults, '/embed' to store CONFIG in the script,")
			print("# '/save' to commit changes, or '/back' to return.")
			print("# example: \n# <STR> key : value\n\n")
			# currently supported functions::
			# /save /embed /add /remove /back /defaults
			#	the help here could be made better, more aesthetic - more menu like
			#
			# print all of the options, so we know what we have to work with
			#	first we print the name of the subdict/script and ={ so it shows like a full dict
			#	we use ,end="" in this print line just to keep with formatting of the rest of this
			#	section - which uses ,end="" on every print, but adds "\n" at the start
			print(which," = {",end="")
			#	like this header line (showing format of <type>key:value)
			print("\n<TYPE>   <key>  :  <value>",end="")
			#	for each key/option in the current scripts config:
			for option in TEMP['current']:
				# print the new line first
				print("\n",end="")
				#	THIS TYPE HANDLER NEEDS MORE TYPES AND AN ELSE:
				#	but currently it handles strings and ints
				# checks the type() of the value on each key
				if(type(TEMP['current'][option])==type(1)):
					print("<INT> ",end="")
				elif(type(TEMP['current'][option])==type("a")):
					print("<STR> ",end="")
				# then displays the value associated with the key
				print(option," : ",TEMP['current'][option],",",end="")
			# }closes up the dict/configset visually
			print("}\n")
			#	and asks for input about which one you intend to modify
			key=input(" key to modify or command >> ")
			#
			# NOW we start listening for commands or keys to edit
			#	using /command format avoids name conflicts,
			#	since keys starting with '/' are very unlikely.
			# IF /back then return to the choosing menu, which needs its own /back still iirc
			if(key=="/back"):
				Choosing=True
			# /add allows you to add a new key:value pair
			elif(key=="/add"):
				# get the proposed key and value from the user
				proposed_key=input("what should the key name be?\n >> ")
				proposed_value=input("what should the value be?\n >> ")
				#
				# there could be a check put here, 
				# but it asks for confirmation in a moment anyways
				#input("press enter to continue..")
				#
				#
				# if the value can be stored as an int, then it is
				#	but this could merge with the wait above into an intended type() check
				try:
					proposed_value=int(proposed_value)
				except:
					pass
				#
				# now that we have entry, we will ask for confirmation, before comitting changes
				confirmed=False
				# while confirmation is not yet given
				while(not confirmed):
					# we have a type() check, so we can display it in keeping format with before
					#	this type check uses an else: but the one above doesnt. they both need upgrades tbh
					if(type(proposed_value)==type(1)):
						print(f"create <INT> {proposed_key} : {proposed_value} ?")
					else:
						print(f"create <STR> {proposed_key} : \"{proposed_value}\" ?")
					#
					# now that we printed the proposed key:value, we ask if it is correct
					confirm=input("(yes or no >> ")
					if(confirm=="yes"):
						# if the user confirms, we commit changes to the TEMP dict
						TEMP['current'][proposed_key]=proposed_value
						confirmed=True
					elif(confirm=="no"):
						# if the user cancels, then we break loop
						#	I think this returns us to while(Editing)?
						break
					else:
						# unless you type "yes" or "no" it will keep asking
						print("please be clear.")
				# this could be a more informational delay, like saying "Key Saved"
				input("press enter to continue..")
			# /REMOVE removes a key, similar to /add but a little simpler
			elif(key=="/remove"):
				unwanted_key=input("what key would you like to remove?\n >> ")
				if(unwanted_key in TEMP['current']):
					confirmed=False
					while(not confirmed):
						print(f"remove  {unwanted_key} : {TEMP['current'][unwanted_key]} ?")
						confirm=input("(yes or no >> ")
						if(confirm=="yes"):
							TEMP['current'].pop(unwanted_key,None)
							confirmed=True
						elif(confirm=="no"):
							break
						else:
							print("please be clear.")
				else:
					print("That is not a valid key to remove")
				input("press enter to continue..")
			# /embed will encode and attempt to store the current config inside the script
			#	in base64 string using the EmbedConfig() function defined above
			elif(key=="/embed"):
				EmbedConfig("./"+CONFIG[which]['scriptname'],TEMP['current'])
				input("press enter to continue..")
			# This will read the embedded config function from a script, not done yet
			elif(key=="/read"):
				#ParseConfig("./"+CONFIG[which]['scriptname'],TEMP['current'])
				print("Not Yet Implemented")
				input("press enter to continue..")
			# /SAVE will save the current config as a .shadow file
			elif(key=="/save"):
				SaveConfig(which,TEMP,CONFIG)
				input("press enter to continue..")
			# /DEFAULTS will reload defaults for the current script
			#	this should have a confirmation, to prevent lost work
			elif(key=="/defaults"):
				TEMP['current']=CONFIG[which]['current']
				input("press enter to continue..")
			#
			# now that we got through the commands, we check to see if the user
			#	entered a valid key to edit the value for
			elif(key in TEMP['current']):
				# if we got this far, they did enter a valid key, so we show the value
				print(key," is currently set to: ",TEMP['current'][key])
				#	now we get user entry for what to change it to
				value=input("What would you like to change it to? \n >> ")
				confirmed=False
				# another confirmation dialogue
				while(not confirmed):
					# if both are strings, we dont even need to do a type check
					if(type(TEMP['current'][key])!=type(value)):
						# this could also include type handling for [lists, (tuples,etc)]
						# so far it was just made to handle ints for ports etc
						if(type(TEMP['current'][key])==type(1)):
							try:
								value=int(value)
							except:
								# if the key used to be INT, and is changing, it will WARN you
								print("\n\n          !!!!! WARNING !!!!!")
								print("The key had an INT type value, and your proposed value does not match that.")
					# type check and warning over, now we actually ask for confirmation or cancel
					print(f"change {key} \n from {TEMP['current'][key]} \n into {value} ?")
					confirm=input("(yes or no >> ")
					if(confirm=="yes"):
						TEMP['current'][key]=value
						confirmed=True
					elif(confirm=="no"):
						break
					else:
						print("please be clear.")
			# /command/key check
		# /else: (done choosing)
	# /while(Editing)
	return CONFIG
# /EditConfig


# PARSE CONFIG
def ParseConfig(MASTERCONFIG='./Master.shadow'):
	# this is what will power the /read option in EditConfig()
	# it was verified to work with a single config file that stored all of CONFIG
	# it combines the shadow files with b64, instead of using pickle
	#	using the b64/eval() method only could be viable single method option
	#	instead of including pickle import too for similar purpose
	#	we could also have a configS file with multiple lines;
	#		each one a separate base64 configset, like for different clients/presets
	configfile = open(MASTERCONFIG, 'r')
	# anyways here we read and b64decode the contents of the file,
	#	when this gets expanded to /read from scripts also, this will be more like /embed
	#	mixed with LoadConfig()
	CONFIG=b64decode(configfile.read())
	# it is good practice to close files after done, or use with: to open as it autocloses
	configfile.close()
	# now that we have the dict recovered as a string, but base64decode leaves it as bytes
	#	we still need to decode it, then eval() it to turn the string into a dict
	CONFIG=eval(CONFIG.decode())
	# then return that config from the function as a result
	return CONFIG
# /ParseConfig


# EMBED CONFIGURATION
def EmbedConfig(TARGET_FILE,CONFIG):
	# This will embed a configuration within a script, but it needs some error checking
	# set markers, for use by metamorphic code
	CHECK_CONF_START = 'ENCODED'+"_CONFIG='"
	CHECK_CONF_END = "'#/ENCOD"+"EDCONF"
	#
	#
	# CHECK TO SEE IF A CONFIG FILE IS STORED OR NOT
	#	sys.argv[] ar runtime arguments,
	# sys.argv[0] is the name of the script itself, so it opens and reads itself
	# and looks for CHECK_C with .find() if it does not find it, that is our condition here
	#if(open(TARGET_FILE).read().find(CHECK_CONF_END) == -1):
	#
	# open and read the target file - which may be this file,
	#	or one of the payload/utility scripts
	file_data  = open(TARGET_FILE, 'r')
	file_contents = file_data.read()
	file_data.close()
	#
	# prepare the config we passed this function as a base64 string,
	#	first we .encode() it as bytes (b"string") then as b64()
	NEW_CONFIG=b64encode(str(CONFIG).encode())
	#input(NEW_CONFIG)				# ALL OF THESE input() LINES COULD BE DELETED, it was for testing
	# could be worth keeping the input() lines, and just putting them behind a if(DEBUG):
	# 
	# first marker is where the CHECK_CONF_START ends in the file_contents
	# this needs to have a check added, so that if there is no CHECK_CONF_START we
	#	should find an appropriate line, and simply add the encoded_config line in full
	FIRST_MARKER	= file_contents.find(CHECK_CONF_START) + len(CHECK_CONF_START)
	#input(FIRST_MARKER)
	
	# The first half of the file is everything up to the end of the first marker
	FIRST_HALF	= file_contents[0:FIRST_MARKER]
	#input(FIRST_HALF)
	
	# the second marker is where the end of the ENCODED_CONFIG line is at
	SECOND_MARKER	= file_contents.find(CHECK_CONF_END)
	#input(SECOND_MARKER)
	
	# the second half is everything after the start of the second marker
	SECOND_HALF	= file_contents[SECOND_MARKER:]
	#input(SECOND_HALF)
	
	# that splitting into "halves" leaves the old config (or "null") in the middle
	#	we can put that into a variable now, and could add a check that displays this config
	#	so the user can compare both configs and decide which one to keep
	OLD_CONFIG=file_contents[FIRST_MARKER:SECOND_MARKER]
	#input(OLD_CONFIG)
	
	# this is where the new version of the file gets prepared, with new config embedded
	NEW_FILE= FIRST_HALF + NEW_CONFIG.decode() + SECOND_HALF
	#input(NEW_FILE)
	#
	#
	# and finally we write changes to the target file. this is where it will break the file
	#	if something went wrong, and we did not have error handling prevent it
	#	such as a file with no ENCODED_CONFIG line being overwritten from the first line
	#		(that is a real error that happened btw, and still needs fixed!)
	file_data = open(TARGET_FILE, 'w')
	file_data.write(NEW_FILE)
	file_data.close()
	return
# /EmbedConfig


########################################
# / END CONFIG FUNCTIONS
########################################














# GET KEY
def AuthorizeUser():
	os.system('color 0b')
	key = -1
	authorize_time=1	# how long to start the user wait between attempts to answer
	authorize_time_increase=1 # how much longer each wrong answer, 0.5 works if you have a limit around 10
	correct = [7331,7777]	# correct answer could be in the form of a list
	incorrect=0
	incorrect_limit=3
	while(key not in correct):
		cls()
		wait(0.1)
		cls()
		br(8)
		CenteredText("You must use Key to use ShadowTool")
		br()
		if(incorrect>=1):
			CenteredText("incorrect:"+str(incorrect))
		br()
		CenteredText("please enter key:")
		key = input("          >> ")
		try:
			if(int(key) not in correct):
				raise
			else:
				key = int(key)
		except:
			incorrect+=1
			if(incorrect>=incorrect_limit):
				os.system('color 0c')
				CenteredText("Access Dendied")
				br()
				CenteredText("You should not have tried that.")
				br()
				wait(authorize_time)
				br()
				return False
			else:
				CenteredText("Access Dendied Inavlid Key")
				br()
				wait(authorize_time)
				br()
				authorize_time+=authorize_time_increase
	return True
# /get_key



# INTRO
def Intro():
	# THIS could have the ascii art / splash screen etc, at the end, 
	#	instead of putting that stuff in MainMenu()'s start
	# though one reason why to put it in that menu instead of here
	#	would be because the user should be able to get back to that menu
	#	without needing to go through the key stuff again.. but we could just
	#	have a check for if the user needs to do the keycheck *or not* and enchance that
	#	instead of let the way it is currently control how we handle graphics
	# AUTHORIZE THE CLIENT
	if(AuthorizeUser()):
		os.system('color 0a')
		# AuthorizeUser() will return True if passed, so Intro() will return True also
		wait(1)
		br(3)
		CenteredText("Access Granted")
		br(1)
		wait(2)
		cls()
		br(2)
		wait(1)
		if(os.get_terminal_size().columns>120):
			for line in GhostArt['FULL']:
				CenteredText(line)
		else:
			for line in GhostArt['SHADOW']:
				CenteredText(line)
			for line in GhostArt['TOOL']:
				CenteredText(line)
		wait(0.5)
		br(3)
		wait(2)
		input(CenteredText("Press Enter to Continue...",False))
		cls()
		return True
	else:
		# or if the user failed at get_key() then we will pass on the False as well
		print("Access Denied")
		return False
# /intro


# PRINT HELP
def PrintHelp():
	# this would be nice to wrap  in a little dialogue box
	br()
	CenteredText("please choose from one of our options")
	br(2)
	CenteredText("/S /server : will start the Server")
	CenteredText("/C /client : will start and run Client,")
	CenteredText("/F /flood  : Will start the Synflood")
	CenteredText("/I /informer : Will start the Informer")
	CenteredText("/M /move-client : will move the Client")
	#CenteredText("/L /load   : Load configurations for scripts")
	print("")
	CenteredText("/E /edit   : Edit configurations for scripts")
# /PrintHelp




# MAIN MENU
def MainMenu(CONFIG=CONFIG):
	#
	# ROUTINES which get launched in exec_routine
	#	this is where you would add the names of additional scripts,
	#	create new CONFIG set{}s in ShadowConfig to go with each one
	routines = {
		"/S": "Server.py",
		"/server": "Server.py",
		"/C": "Client.pyw",
		"/client": "Client.pyw",
		"/F": "SYNflood.py",
		"/flood": "SYNflood.py",
		"/I": "Informer.py",
		"/informer": "Informer.py",
		"/M": "move-client.py",
		"/move-client": "move-client.py",
		}
	#
	# ROUTINES which get launched as ShadowConfig functions
	#	this could include the rest of the options like /embed /save etc
	#	but idk if it really needs that, since /e allows all of that
	#	there does need to be some more testing on all these features though
	#	to make sure there was not some unforseen bug or glitch
	config_routines = {
		"/L"	: "load",
		"/load"	: "load",
		"/E"	: "edit",
		"/edit"	: "edit",
		}
	#
	# EXEC ROUTINE
	def exec_routine(inpt):
		# executes an action routine defined in routines={} as a script name
		#	if the input matches a key in the routines{} dict
		if inpt in routines.keys():
			# system call to a specific location on disk, this could be relative path
			#	such as os.system(f'./{routines[inpt]}.py')
			# 	or specified like os.system(f'{exec_dir}/{routines[inpt]}.py')
			# pretty sure those style paths would work in python, even on windows, sometimes
			os.system(routines[inpt])
			print(f"{routines[inpt]} has finished")
	# /exec_routine
	#
	#
	# set blank variables for Menu and command
	#	command will be the input()
	command = ""
	#	Menu will store both the action and config routines from above
	#	and combine them into a third list called 'valid'
	Menu={'action':[],'config':[]}
	#
	# This is where the action and config routines all get added into Menu
	#	and combined into the universal 'valid' list which we check later
	for routine in routines:
		Menu['action'].append(routine)
	for routine in config_routines:
		Menu['config'].append(routine)
	Menu['valid']=Menu['config']+Menu['action']
	#
	# at this point setup is mostly complete, and we are really running
	Running=True
	while(Running):
		#
		# give the user a moment to read the initial printing of /help
		#input("press enter to continue")
		#
		# now it is time for user input, for them to Choose a command
		Choosing=True
		while(Choosing):
			cls()
			br()
			CenteredText("Welcome to ShadowTool")
			br(2)
			# Print the help text
			PrintHelp()
			# this could be wrapped with a nice display, but works as is
			br(2)
			CenteredText("Please enter command:")
			command = input("                              >> ")
			try:
				# now that a command is entered, we try to run it
				if command not in Menu['valid']:
					# if the command is not in the 'valid' Menu list,
					#	then we check it as a core/hardcoded command
					# such as HELP (reviewable any time)
					if(command=="/help" or command=="/h"):
						PrintHelp()
					# or EXIT
					elif(command=="/exit" or command=="/quit"):
						input("Thank you for using ShadowTool")
						sys.exit()
					# or EXIT
					elif(command=="/debug"):
						print("Menu['valid]: ",Menu['valid'])
						br(2)
					else:
						# if it reaches this else, cause an exception.
						# a command that lead here was not 'valid' nor hardcoded
						raise
				# Now if the command was on the 'Valid' list...
				else:
					# we would be done choosing a command, time to move out of this loop
					Choosing=False
				input(CenteredText("Press Enter to Continue...",False))
			except:
				# this is where we end up when an exception is 'raised'
				print(f"{command} is an Invalid Command")
				# remind the user what the available options are
				print(f"Valid options are {Menu['valid']}")
				input(CenteredText("Press Enter to Continue...",False))
		# now that we know the command is in 'valid' we dont need to check that again
		#	we just need to know which subset of valid it was in.
		#	lets check 'action' first, because it is alphabetical.
		# some elif()s could be added here, if more routine{} sets are added up above
		if(command in Menu['action']):
			# if the command *was* in action, then exec_routine() and launch the script
			exec_routine(command)
		else:
			# otherwise, until more categories are added, a valid option would be
			#	related to loading or editing configurations for the scripts
			if(config_routines[command]=="load"):
				# this time alphabetical did not come in, but again there is only one
				#	specific check, because there are only two options, and the input is
				#	already verified as being one or the other
				#	if you add extra options up top, just back them up down here
				CONFIG=LoadConfig()
			else:
				# EditConfig() is where you can create and save/embed configs
				CONFIG=EditConfig("all",CONFIG)
			#
		#
	#
	# do we need to return anything from this function? not necessarily
	return
# /MainMenu



# IF this script is launched as primary, then code executes,
#	keeping any execution of code in a block like this,
#	makes the script able to be read by another script as an import,
# 	so we can combine assets from multiple scripts
if __name__ == '__main__':
	# 
	# set the title to ShadowTool
	set_title()
	# Intro will return True if get_key() returned True
	#	so if Intro is True, then go to MainMenu, else go to Prank (once it is added)
	if(Intro()):
		CONFIG=LoadConfig()
		MainMenu(CONFIG)
	else:
		try:
			Denied=voicebox()
			Denied.ransomeware_notice()
			Denied.prank()
		except:
			prank()
	#
	#
  #
#
# 
# 
##################################################
#             S H A D O W    T O O L             #
##################################################
# End Of File: ShadowTool.py
