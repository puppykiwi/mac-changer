import subprocess
import string
import random
import re

def get_mac_address():
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

get_mac_address()