import subprocess

# Update pip
subprocess.call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])

# Install scapy and psutil
subprocess.call(['python', '-m', 'pip', 'install', 'scapy'])
subprocess.call(['python', '-m', 'pip', 'install', 'psutil'])
