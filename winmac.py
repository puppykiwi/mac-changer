import subprocess
import argparse
import random
import string
import re

def get_current_macAddress(interface_name):
  result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface_name} | Select-Object -ExpandProperty MacAddress"], capture_output=True, text=True, check=True)
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
    print(f"Random mac: {mac_address}")
    
    return mac_address

# def generate_random_mac_address():
#   """
#   Generates a random MAC address with the locally administered bit set.
# 
#   Returns:
    #   str: The generated random MAC address.
#   """
# 
#   mac_bytes = [random.randint(0, 255) for _ in range(6)]
#   mac_bytes[0] |= 2  # Set the second bit from left in the first byte
#   return ':'.join(['%02x' % b for b in mac_bytes])


def change_macAddress(interface_name, new_mac):

  # Get current MAC address (for informational purposes)
  current_mac = get_current_macAddress(interface_name)
  print(f"Current MAC address of {interface_name}: {current_mac}")
  print(f"New MAC address of {interface_name}: {new_mac}")

  # # Check network adapter status
  # result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface_name} | Select-Object Status"], capture_output=True, text=True, check=True)
  # adapter_status = result.stdout.strip()

  # if adapter_status == "Disabled":
  #   print(f"Network adapter {interface_name} is already disabled.")
  # else:
  #   # Disable the network adapter (requires administrator privileges)
  #   result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface_name} | Disable-NetAdapter"], capture_output=True, text=True, check=True)
  #   if result.returncode != 0:
  #     raise RuntimeError(f"Failed to disable network adapter: {result.stderr}")

  result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface_name} | Disable-NetAdapter"], capture_output=True, text=True, check=True)
  if result.returncode != 0:
      raise RuntimeError(f"Failed to disable network adapter: {result.stderr}")
  
  print("Adapter Off") #debug

  # Set the new MAC address
  result = subprocess.run(["powershell", "-Command", f"Set-NetAdapter -Name {interface_name} -MacAddress {new_mac}"], capture_output=True, text=True, check=True)
  # if result.returncode != 0:
    # raise RuntimeError(f"Failed to set new MAC address: {result.stderr}")
  print("Adapter Changed") #debug

  # Enable the network adapter
  result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface_name} | Enable-NetAdapter"], capture_output=True, text=True, check=True)
  if result.returncode != 0:
    raise RuntimeError(f"Failed to enable network adapter: {result.stderr}")
  print("Adapter On") #debug

  print(f"New MAC address of {interface_name}: {new_mac}")


if __name__ == "__main__":
#   print(get_current_mac_address())
    parser = argparse.ArgumentParser(description="Johnray's MAC address changer for linux")
    parser.add_argument("-i", "--interface", dest="interface", help="The network interface name", default="Ethernet")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
    args = parser.parse_args()
    
    if args.interface=="":
      interface = "Ethernet"
    else:
      interface = args.interface
      
    new_macAddress = ""
    if args.random:
        new_macAddress = get_random_macAddress()
    elif args.mac:
        new_macAddress = args.mac

    old_macAddress = get_current_macAddress(interface)
    print("[*] Old MAC address:", old_macAddress)
    print("[+] New MAC address:", new_macAddress)

    change_macAddress(interface, new_macAddress)

    new_macAddress = get_current_macAddress(interface)
    print("[+] New MAC address:", new_macAddress)