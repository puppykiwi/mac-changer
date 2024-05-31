import subprocess
import re
import platform

def get_mac_address(interface):
  """
  Retrieves the MAC address of a network interface, handling different operating systems.

  Args:
      interface (str): The name of the network interface (e.g., "eth0", "wlan0").

  Returns:
      str: The MAC address of the interface, or None if not found.
  """

  if platform.system() == "Linux":
    # Use ifconfig for Linux
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True, check=True)
    output = result.stdout
    match = re.search(r"ether\s+([0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2})", output)
    if match:
      return match.group(1).upper()  # Extract and uppercase the MAC address
    else:
      print(f"Failed to find MAC address for {interface} using ifconfig")
      return None

  elif platform.system() == "Windows":
    # Use PowerShell for Windows (requires administrator privileges)
    result = subprocess.run(["powershell", "-Command", f"Get-NetAdapter -Name {interface} | Select-Object -ExpandProperty MacAddress"], capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    return output.upper()  # Uppercase the MAC address

  else:
    print(f"Unsupported operating system: {platform.system()}")
    return None
  
if __name__ == "__main__":
  get_mac_address(ethernet)