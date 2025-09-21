import os
import subprocess
import sys

def handle_ls(args):
    """
    Lists the contents of a directory.
    Uses 'dir' on Windows and 'ls' on other systems.
    """
    if sys.platform == "win32":
        command = ["cmd", "/c", "dir"] + args
    else:  # Linux or macOS
        command = ["ls"] + args
        
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(f"Error: Command '{command[0]}' not found on this system.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")

def handle_mkdir(args):
    """
    Creates a new directory.
    """
    if not args:
        print("Usage: mkdir <directory>")
        return
        
    try:
        os.mkdir(args[0])
    except FileExistsError:
        print(f"mkdir: directory '{args[0]}' already exists")
    except Exception as e:
        print(f"mkdir: An error occurred: {e}")

def handle_rm(args):
    """
    Removes a file or directory.
    Uses 'del' on Windows for files and 'rm -r' on others for directories.
    """
    if not args:
        print("Usage: rm <file/directory>")
        return
        
    item_to_remove = args[0]
    
    if os.path.isfile(item_to_remove):
        try:
            os.remove(item_to_remove)
        except PermissionError:
            print(f"rm: permission denied: {item_to_remove}")
        except Exception as e:
            print(f"rm: An error occurred: {e}")
    elif os.path.isdir(item_to_remove):
        if sys.platform == "win32":
            # Using 'rmdir /s /q' for quiet recursive removal on Windows
            command = ["rmdir", "/s", "/q", item_to_remove]
        else:
            # Using 'rm -r' for recursive removal on Linux/macOS
            command = ["rm", "-r", item_to_remove]
        try:
            subprocess.run(command, check=True)
        except Exception as e:
            print(f"rm: An error occurred: {e}")
    else:
        print(f"rm: No such file or directory: {item_to_remove}")

def handle_pwd():
    """
    Prints the current working directory.
    """
    print(os.getcwd())

def handle_cd(args):
    """
    Changes the current working directory.
    """
    if not args:
        # 'cd' with no arguments in many terminals takes you to the home directory
        home_dir = os.path.expanduser("~")
        os.chdir(home_dir)
        return
        
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        print(f"cd: No such file or directory: {args[0]}")
    except Exception as e:
        print(f"cd: An error occurred: {e}")

def handle_cat(args):
    """Displays the content of a file."""
    if not args:
        print("Usage: cat <file>")
        return
        
    file_path = args[0]
    
    try:
        with open(file_path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"cat: No such file or directory: {file_path}")
    except Exception as e:
        print(f"cat: An error occurred: {e}")

def handle_touch(args):
    if not args:
        print("Usage: touch <file>")
        return
    try:
        with open(args[0], 'a'):
            os.utime(args[0], None)
        print(f"Created file: {args[0]}")
    except Exception as e:
        print(f"touch: An error occurred: {e}")

def handle_echo(args):
    try:
        # Join arguments and print them
        output = " ".join(args)
        print(output)
    except Exception as e:
        print(f"echo: An error occurred: {e}")