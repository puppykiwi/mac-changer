import subprocess
import string
import random
import re

def get_random_macAddress():
    hexdigits = ''.join(set(string.hexdigits.upper()))
    special_choice = "02468ACE"

    mac_address = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac_address += random.choice(special_choice)
            else:
                mac_address += random.choice(hexdigits)
        
        # Add ":" after every 2 characters, though unnecessary for now
        '''
        if i != 5:
            mac_address += ":" 
    print(mac_address)
        '''
    return mac_address

def get_current_macAddress(interface):
    result = subprocess.Popen(f"ifconfig {interface}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.read().decode('utf-8')
    error = result.stderr.read().decode('utf-8')
    
    current_macAddress = re.search("ether (.+) ", output).group().split()[1].strip() # regex to strip the address from the output of ifconfig

    if error == "":
        return current_macAddress
    else:
        print(error)
        return None

def change_macAddress(interface, new_macAddress):
    #switch the device down, change the mac address, back up it comes
    subprocess.call(f"ifconfig {interface} down", shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_macAddress}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)

