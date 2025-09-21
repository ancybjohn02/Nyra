import subprocess
import sys

def handle_ping(args):
    """Pings a host to check network connectivity."""
    if not args:
        print("Usage: ping <host>")
        return
        
    host = args[0]
    
    # Use platform-specific options for a more reliable ping
    if sys.platform == "win32":
        command = ["ping", "-n", "4", host] # -n for Windows
    else:
        command = ["ping", "-c", "4", host] # -c for Linux/macOS
        
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Error: Could not reach host {host}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_curl(args):
    """Makes a web request using curl."""
    if not args:
        print("Usage: curl <URL>")
        return
        
    try:
        subprocess.run(["curl"] + args, check=True)
    except FileNotFoundError:
        print("Error: 'curl' not found. Is it installed on your system?")
    except subprocess.CalledProcessError as e:
        print(f"Error: Request failed with exit code {e.returncode}")

def handle_ip_address(args):
    """
    Handles both ifconfig and ipconfig based on the OS.
    """
    if sys.platform == "win32":
        command = ["ipconfig"] + args
    elif sys.platform == "linux":
        command = ["ifconfig"] + args
    else:
        # Fallback for other systems like macOS
        command = ["ifconfig"] + args
    
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("Network command not found on this system.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
