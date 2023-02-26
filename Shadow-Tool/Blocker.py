import subprocess

def block_ip(ip_address):
    # Check if the inbound rule already exists, update it with the new IP if it does, otherwise create a new rule
    command_check_in = f"netsh advfirewall firewall show rule name=\"susIPin\""
    rule_exists_in = subprocess.call(command_check_in, shell=True)
    if rule_exists_in == 0:
        command_in = f"netsh advfirewall firewall set rule name=\"susIPin\" new remoteip={ip_address}/32"
    else:
        command_in = f"netsh advfirewall firewall add rule name=\"susIPin\" dir=in interface=any action=block remoteip={ip_address}/32"
    subprocess.call(command_in, shell=True)

    # Check if the outbound rule already exists, update it with the new IP if it does, otherwise create a new rule
    command_check_out = f"netsh advfirewall firewall show rule name=\"susIPout\""
    rule_exists_out = subprocess.call(command_check_out, shell=True)
    if rule_exists_out == 0:
        command_out = f"netsh advfirewall firewall set rule name=\"susIPout\" new remoteip={ip_address}/32"
    else:
        command_out = f"netsh advfirewall firewall add rule name=\"susIPout\" dir=out interface=any action=block remoteip={ip_address}/32"
    subprocess.call(command_out, shell=True)

    # Block the IP address on all ports for both inbound and outbound rules
    command_inbound = "netsh advfirewall firewall add rule name='Block {}' dir=in action=block protocol=any remoteip={} profile=any".format(ip_address, ip_address)
    subprocess.call(command_inbound, shell=True)
    command_outbound = "netsh advfirewall firewall add rule name='Block {}' dir=out action=block protocol=any remoteip={} profile=any".format(ip_address, ip_address)
    subprocess.call(command_outbound, shell=True)


if __name__ == '__main__':
    # Ask the user for the IP address to block
    ip_address = input("Enter the IP address to block: ")

    # Block the IP address
    block_ip(ip_address)
