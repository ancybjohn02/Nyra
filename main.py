import os
import shlex
import subprocess
import sys
import readline
import atexit

# Import all functions from our command modules
from commands.file_ops import handle_ls, handle_mkdir, handle_rm, handle_pwd, handle_cd, handle_cat, handle_touch, handle_echo
from commands.sys_monitor import handle_monitor, handle_hostname, handle_uptime
from commands.process_ops import handle_ps, handle_kill
from commands.network_ops import handle_ping, handle_curl, handle_ip_address
from commands.archive_ops import handle_zip, handle_unzip
from commands.command_map import get_platform_command
from utils.nyra import run_nyra_terminal

# Global variables for command history
HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".Nyra_history")

# List of all built-in commands for autocompletion and help
ALL_BUILT_IN_COMMANDS = [
    'ls', 'cd', 'pwd', 'mkdir', 'rm', 'cat', 'touch', 'echo',
    'monitor', 'hostname', 'uptime', 'ps', 'kill',
    'ping', 'curl', 'ifconfig', 'ipconfig', 'zip', 'unzip',
    'help', 'history', 'exit'
]

def handle_external_command(command_input, args):
    """
    Executes commands that are not explicitly mapped (built-in) but might have
    a platform-specific name.
    """
    native_command = get_platform_command(command_input)
    
    if native_command:
        # If a mapping exists in command_map.py, use it.
        try:
            full_command = native_command + args
            subprocess.run(full_command, check=True)
        except subprocess.CalledProcessError as e:
            print(e.stderr, end='')
        except FileNotFoundError:
            print(f"Error: Command '{native_command[0]}' not found on this system. Please install it.")
        return

    # Fallback to a generic subprocess call if no mapping exists for this command.
    try:
        subprocess.run([command_input] + args, check=True)
    except FileNotFoundError:
        print(f"Nyra: {command_input}: command not found")
    except subprocess.CalledProcessError as e:
        print(e.stderr, end='')

def display_help():
    """Displays a list of all available commands and their descriptions."""
    print("Available Commands:")
    command_descriptions = {
        'ls': 'Lists files and directories.',
        'cd': 'Changes the current directory.',
        'pwd': 'Prints the current working directory.',
        'mkdir': 'Creates a new directory.',
        'rm': 'Removes a file or directory.',
        'cat': 'Displays the content of a file.',
        'touch': 'Creates a new empty file.',
        'echo': 'Prints text to the terminal.',
        'monitor': 'Displays system resource usage.',
        'hostname': 'Displays the system hostname.',
        'uptime': 'Shows how long the system has been running.',
        'ps': 'Displays running processes.',
        'kill': 'Terminates a process by its ID.',
        'ping': 'Pings a host to check network connectivity.',
        'curl': 'Makes a web request.',
        'zip': 'Compresses files into a .zip archive.',
        'unzip': 'Extracts files from a .zip archive.',
        'help': 'Displays this help message.',
        'history': 'Shows the command history.',
        'exit': 'Exits the terminal.'
    }
    for cmd in sorted(ALL_BUILT_IN_COMMANDS):
        print(f"  {cmd:<10} - {command_descriptions.get(cmd, '')}")

def display_history():
    """Displays the command history."""
    history_length = readline.get_current_history_length()
    for i in range(1, history_length + 1):
        print(f"  {i:<4} {readline.get_history_item(i)}")

def completer(text, state):
    """
    This function suggests commands and file/directory names for readline.
    """
    # Try to complete a command name
    options = [c for c in ALL_BUILT_IN_COMMANDS if c.startswith(text)]
    if options:
        return options[state]
    
    # Then, try to complete a file or directory name
    try:
        items = os.listdir('.')
        matches = [i for i in items if i.startswith(text)]
        if matches:
            return matches[state]
    except FileNotFoundError:
        pass
    
    return None

def save_history():
    """Saves the command history to a file."""
    readline.write_history_file(HISTORY_FILE)

def main():
    """
    Main loop for the Python-based command terminal.
    """
    # Setup readline for history and autocompletion - RUN ONCE
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
    
    readline.set_completer(completer)
    readline.set_history_length(100) # Optional: limit history size
    
    # Load command history from file
    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)
    
    atexit.register(save_history)
    
    print("=" * 40)
    print("\nWelcome to your custom terminal!")
    print("\nGetting Started:")
    print("  - Type 'help' to see available commands.")
    print("  - Use arrow keys to navigate command history.")
    print("  - Press 'Tab' for autocompletion.")
    print("  - Press 'Ctrl+R' to search history.")
    print("\n" + "-" * 40 + "\n")
    
    while True:
        try:
            current_directory = os.getcwd()
            prompt = f"[{os.getlogin()}@Nyra {os.path.basename(current_directory)}]$ "
        except Exception:
            prompt = "[Nyra]$ "
        
        try:
            command_input = input(prompt)
            
            if not command_input.strip():
                continue
            
            command_parts = shlex.split(command_input)
            command = command_parts[0]
            args = command_parts[1:]
            
            command_map = {
                'ls': lambda: handle_ls(args),
                'cd': lambda: handle_cd(args),
                'pwd': lambda: handle_pwd(),
                'mkdir': lambda: handle_mkdir(args),
                'rm': lambda: handle_rm(args),
                'cat': lambda: handle_cat(args),
                'touch': lambda: handle_touch(args),
                'echo': lambda: handle_echo(args),
                'monitor': lambda: handle_monitor(),
                'hostname': lambda: handle_hostname(),
                'uptime': lambda: handle_uptime(),
                'ps': lambda: handle_ps(),
                'kill': lambda: handle_kill(args),
                'ping': lambda: handle_ping(args),
                'curl': lambda: handle_curl(args),
                'ifconfig': lambda: handle_ip_address(args),
                'ipconfig': lambda: handle_ip_address(args), 
                'zip': lambda: handle_zip(args),
                'unzip': lambda: handle_unzip(args),
                'history': lambda: display_history(),
                'help': lambda: display_help(),
                'exit': lambda: print("Exiting terminal.") or sys.exit(0),
            }

            if command in command_map:
                command_map[command]()
            else:
                handle_external_command(command_input, args)

        except (ValueError, IndexError):
            print("Error: Invalid command or arguments.")
        except KeyboardInterrupt:
            print("\nExiting terminal.")
            break
        except EOFError:
            print("\nExiting terminal.")
            break

if __name__ == "__main__":
    run_nyra_terminal()
    main()
