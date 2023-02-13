# Shadow-Tool

A Penetration Testing tool for windows to windows application, and home made



## Welcome to Shadow-Tool


Shadow-Tool is an all-in-one terminal capable of running, editing, and redeploying several programs from within the Shadow-Tool terminal itself. Shadow-Tool can also be installed on removable storage such as a USB drive to create a portable and deployable tool.



#### Authors

- Shadowdrums

- Toroidist

#### Contributors

- DJ Stomp


## Advisory

Shadow-Tool was made for educational purposes and as a proof of concept. This program is 
ment to be a Penatration-Testing tool. Author(s) will not be held liable for any misuse
of this program. ONLY USE shadow-tool on your own device(s) or have DOCUMENTED PRE Approval from the owner of the device(s)



## Requirements

1. To be able to run Shadow-Tool you will need python3.

2. After Installing Python3, update pip via: 
   ```sh
   python -m pip install --upgrade pip
   ```

3. Scapy will also be required for one of the deplyable programs. You can get scapy with pip:
   ```sh
   pip install scapy
   ```

## Usage


### Quickstart

The program has a pre-defined key in ShadowTool.py that can be changed manualy in the script. The password will only except numbers, and is set to (7331) by default. 


### Editing

When logged into the Shadow-Tool terminal you must use "/E" to edit server, client, and synflood.
once you are in the edit menu and type server or client and hit "enter". Then you choose which 
aspect of the program you would like to edit, for example: to change IP in server you type
"SERVER_IP" then hit "enter", now you change the IP to host devices IP, hit "enter" and type yes then hit
"enter" again, after the change has been made type "/save" and hit "enter". Now you can use "/back"
twice to get back to main menu and then run server.

These same steps can be used for Synflood.

### Client and server

Server must run on your host device, the ip and port for both server and client must match
and the IP that must be used is the IP for the Host device.


#### SYNflood

Synflood is a DDoS script but wont be effective unless multiple devices use it and have the same
target. to use it, you must edit the IP for synflood to the IP of the device you are going to target.
after edit has been made and saved you can run Synflood.

#### Informer

Informer will make a print out of device information into the shadow-tool folder.

#### Move-Client

Move-Client will move the Client.pyw to target device start up folder and will run client in 
a hidden window when the computer is started up and logged into.

#### Enable-RDP

This option will enable remote desktop on target device.

#### Laptop Keep Alive

This will make the target laptop do nothing when the lid is closed. This will keep the laptop on and running while lid is closed so connections can still be made.

Notes:

Updates will be made to this in the future for more functionality.

Enjoy Shadow-Tool
