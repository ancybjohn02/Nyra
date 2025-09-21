import sys

# This dictionary maps a common command name to its platform-specific equivalent.
PLATFORM_COMMANDS = {
    # Core File and Directory Operations
    "ls": {
        "win32": ["cmd", "/c", "dir"],
        "linux": ["ls"],
        "darwin": ["ls"],
    },
    "rm": {
        "win32": ["cmd", "/c", "del"],
        "linux": ["rm"],
        "darwin": ["rm"],
    },
    "rmdir": {
        "win32": ["cmd", "/c", "rmdir", "/s", "/q"], # -s & -q are for quiet recursive removal
        "linux": ["rm", "-r"],
        "darwin": ["rm", "-r"],
    },
    "cat": {
        "win32": ["cmd", "/c", "type"],
        "linux": ["cat"],
        "darwin": ["cat"],
    },
    "touch": {
        # 'touch' is not native to Windows, so we handle it in Python code
        # We can map it to a placeholder list here
        "win32": ["python-handler"], 
        "linux": ["touch"],
        "darwin": ["touch"],
    },

    # Networking Commands
    "ifconfig": {
        "win32": ["ipconfig"],
        "linux": ["ifconfig"],
        "darwin": ["ifconfig"],
    },
    "ping": {
        "win32": ["ping", "-n", "4"], # -n specifies count on Windows
        "linux": ["ping", "-c", "4"], # -c specifies count on Linux/macOS
        "darwin": ["ping", "-c", "4"],
    },
    "curl": {
        "win32": ["curl"],
        "linux": ["curl"],
        "darwin": ["curl"],
    },

    # Archiving Commands
    "zip": {
        "win32": ["zip"],
        "linux": ["zip"],
        "darwin": ["zip"],
    },
    "unzip": {
        "win32": ["unzip"],
        "linux": ["unzip"],
        "darwin": ["unzip"],
    },
}

def get_platform_command(command_name):
    """
    Looks up the correct native command based on the OS.
    Returns the command list if found, otherwise returns None.
    """
    # Get the current OS name (e.g., 'win32', 'linux', 'darwin')
    platform = sys.platform
    
    # Check if the command exists for the current platform
    if command_name in PLATFORM_COMMANDS:
        return PLATFORM_COMMANDS[command_name].get(platform)
        
    return None