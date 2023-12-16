import ctypes
import sys
import os

def is_admin():
    if os.name == 'nt':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0

def request_admin_permissions():
    if not is_admin():
        if os.name == 'nt':
            # Re-run the program with admin rights on Windows
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        elif os.name == 'posix':
            # Provide instructions for Posix
            print("Please run this script as root.")

