import psutil
import socket
import os
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_monitor():
    """
    Displays real-time CPU, memory, and a list of top processes.
    This mimics the functionality of `top` or `htop`.
    """
    try:
        while True:
            clear_screen()
            
            # Get system information
            cpu_percent = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()
            
            # Display system stats
            print(f"System Monitor (Press Ctrl+C to exit)\n")
            print(f"  CPU: {cpu_percent:>5.1f}%")
            print(f"  Memory: {mem.percent:>5.1f}% | {mem.used/1024/1024:.0f} MB / {mem.total/1024/1024:.0f} MB\n")
            
            # Get a list of top processes
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            # Sort processes by CPU usage
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            # Display the top processes
            print(f"{'PID':<8} {'CPU%':<8} {'MEM%':<8} {'NAME'}")
            print("-" * 40)
            for proc in processes[:10]: # Show top 10 processes
                mem_percent = proc['memory_info'].rss / mem.total * 100
                print(f"{proc['pid']:<8} {proc['cpu_percent']:<8.1f} {mem_percent:<8.1f} {proc['name']}")
            
            time.sleep(5) # Refresh every second
            
    except KeyboardInterrupt:
        print("\nExiting monitor.")

def handle_hostname():
    """Prints the system hostname."""
    print(socket.gethostname())

def handle_uptime():
    """Shows how long the system has been running."""
    uptime_seconds = time.time() - psutil.boot_time()
    print(f"Uptime: {int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m {int(uptime_seconds % 60)}s")
