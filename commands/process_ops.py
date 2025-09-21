import psutil

def handle_ps():
    """Lists running processes."""
    print(f"{'PID':<8} {'Name':<20} {'Status':<10} {'CPU %':<8}")
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
        try:
            pinfo = proc.info
            print(f"{pinfo['pid']:<8} {pinfo['name']:<20} {pinfo['status']:<10} {pinfo['cpu_percent']:<8.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def handle_kill(args):
    """Terminates a process by PID."""
    if not args:
        print("Usage: kill <pid>")
        return
    
    try:
        pid = int(args[0])
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} terminated.")
    except (ValueError, psutil.NoSuchProcess):
        print(f"Error: Invalid PID or process not found.")
    except Exception as e:
        print(f"Error: Could not terminate process - {e}")