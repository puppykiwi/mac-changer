import subprocess
import argparse
import random
import string
import re

def get_current_macAddress():
  result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {"Ethernet"} | Select-Object -ExpandProperty MacAddress"], capture_output=True, text=True, check=True)
  return result.stdout.strip()

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
        
        
        if i != 5:
            mac_address += ":" 
    
    return mac_address

print(get_current_macAddress())
print(get_random_macAddress())