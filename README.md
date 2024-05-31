# mac-changer

This Python script allows you to change the Media Access Control (MAC) address of a network interface on Windows, Linux and Mac OS machines.

**Features**

* Change the MAC address to a random value or a user-specified address.
* Provides basic checks and user interaction for a smoother experience.

**Installation**

1. **Prerequisites:**
   - Python 3 ([python](https://www.python.org/downloads/))
   - Administrator privileges are required to change the MAC address. (Use sudo in linmac and powershell admin  for winmac)

2. **Clone the repository:**

   ```bash
   git clone https://github.com/puppykiwi/mac-changer.git
   ```

3. **Install dependencies (optional, if not already installed):**

   ```bash
   cd mac-changer
   pip install -r requirements.txt  
   ```

**Usage**

1. Open a command prompt or terminal and navigate to the directory where you cloned the repository.

2. Run the script with the following options:

   - `-r`: Generate a random MAC address (default behavior if no option is specified).
   - `-m <mac_address>`: Specify the new MAC address you want to set (e.g., `-m 00:11:22:33:44:55`).

   ```bash
   python winmac.py  # Generates a random MAC address
   python winmac.py -r  # Generates a random MAC address (same as above)
   python winmac.py -m 00:11:22:33:44:55  # Sets the MAC address to 00:11:22:33:44:55
   ```

**Notes**

- Use ([winmac] (https://github.com/puppykiwi/mac-changer/winmac.py)) in windows machines and ([linmac] (https://github.com/puppykiwi/mac-changer/linmac.py)) for all other UNIX machines

- Changing the MAC address might temporarily disrupt your network connection.

- You can specify the interface to change but it defaults to your ethernet interface

**Disclaimer**

This script is provided for educational purposes only. Use it at your own risk. The authors are not responsible for any misuse or unexpected consequences of using this script.
