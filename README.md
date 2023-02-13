# Shadow-Tool
A Penetration Testing tool for windows to windows application, and home made



Welcome to Shadow-Tool:

Authors:

.Shadowdrums

.Toroidist

Contributers:

.DJ Stomp

ADVISEMENT:

Shadow-Tool was made for educational purposes and as a proof of concept. This program is 
ment to be a Penatration-Testing tool. Author(s) will not be held liable for any miss use
of this program. ONLY USE shadow-tool on your own device(s) or have DOCUMENTED PRE APPROVAL
from the owner of the device(s).

Shadow-Tool:

Shadow-Tool.py is the used for the Shadow-Tool Terminal

Shadow-Tool is a all in one terminal capable of running several programs from within the terminal.
You can also edit and save your edits for 3 of the programs all from the terminal.

Shadow-Tool can also be used from a usb for a portable deployable tool.
This program has a set key in ShadowTool.py that can be changed manualy in the script. Current Key 
is set to (7331). The password will only except numbers.

Rescources Required for Shadow-Tool:

1. To be able to run Shadow-Tool you will need python3.

2. after Installing Python3 you must update pip via: 
   PS> python.exe -m pip install --upgrade pip

3. Scapy will also be required for one of the deplyable programs to get scapy you must use pip:
   PS> pip install scapy 

How To Use:

How To Edit:

When logged into the Shadow-Tool terminal you must use "/E" to edit server, client, and synflood.
once you are in the edit menu and type server or client and hit "enter". Then you choose which 
aspect of the program you would like to edit, for example: to change IP in server you type
"SERVER_IP" then hit "enter", now you change the IP to host devices IP, hit "enter" and type yes then hit
"enter" again, after the change has been made type "/save" and hit "enter". Now you can use "/back"
twice to get back to main menu and then run server.

These same steps can be used for Synflood.

To use client and server:

Server must run on your host device, the ip and port for both server and client must match
and the IP that must be used is the IP for the Host device.


How To Use SYNflood:

Synflood is a DDoS script but wont be effective unless multiple devices use it and have the same
target. to use it, you must edit the IP for synflood to the IP of the device you are going to target.
after edit has been made and saved you can run Synflood.

Informer:

Informer will make a print out of device information into the shadow-tool folder.

Move-Client:

Move-Client will move the Client.pyw to target device start up folder and will run client in 
a hidden window when the computer is started up and logged into.

Enable-RDP:

This option will enable remote desktop on target device.

Laptop Keep Alive:

This will make the target laptop do nothing when the lid is closed. This will keep the laptop on and running while lid is closed so connections can still be made.

Notes:

Updates will be made to this in the future for more functionality.

Enjoy Shadow-Tool


