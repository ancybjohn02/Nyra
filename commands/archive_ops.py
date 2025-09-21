import subprocess
def handle_zip(args):
    if not args or len(args) < 2:
        print("Usage: zip <archive_name> <file1> <file2> ...")
        return

    try:
        # The 'zip' command is external, so we'll use subprocess
        subprocess.run(["zip"] + args, check=True)
    except FileNotFoundError:
        print("Error: 'zip' not found. Is it installed on your system?")
    except subprocess.CalledProcessError as e:
        print(f"Error zipping files: {e}")

def handle_unzip(args):
    if not args:
        print("Usage: unzip <archive_name>")
        return

    try:
        subprocess.run(["unzip"] + args, check=True)
    except FileNotFoundError:
        print("Error: 'unzip' not found. Is it installed on your system?")
    except subprocess.CalledProcessError as e:
        print(f"Error unzipping file: {e}")