# Nyra: The Cross-Platform Developer's Shell

**Nyra** is a custom command-line interface (CLI) built in Python, designed to be a seamless, unified shell for developers working across different operating systems.  
It provides a familiar and powerful set of commands, intelligently mapping them to native system utilities to ensure a consistent experience whether you're on **Windows**, **Linux**, or **macOS**.

Our mission is to eliminate the friction of switching between operating systems, allowing you to use your preferred commands without having to learn new syntax.

---

## Key Features

- **Intelligent Command Mapping**  
  Automatically translates common Linux/Unix commands to their Windows equivalents.  
  Example: use `ls` and `cat` even in a Windows environment.

- **Comprehensive Built-in Commands**  
  Includes essential commands for file operations, system monitoring, and network diagnostics (`cd`, `ls`, `pwd`, `ps`, `ping`, and more).

- **Real-Time System Monitoring**  
  The `monitor` command provides a real-time, interactive dashboard of CPU, memory, and disk I/O.

- **Interactive & User-Friendly**  
  Features command history, autocompletion, and rich, colored output.

- **Extensible Architecture**  
  Modular design makes it easy to add new custom commands or integrate external services.

---

## Getting Started

### Prerequisites
- Python **3.x**
- `pip` (Python package installer)

### Installation
```bash
# Clone the repository
git clone https://github.com/ancybjohn02/Nyra.git
cd Nyra

# Install dependencies
pip install -r requirements.txt
````

### Usage

Start the Nyra terminal by running:

```bash
python main.py
```

You’ll see a stylized welcome banner. From there, you can type your commands.

---

## Examples

List files and directories:

```bash
ls -l
```

Change directory:

```bash
cd my_project_folder
```

Check system resource usage:

```bash
monitor
```

Get help:

```bash
help
```

---

## Available Commands

| Command    | Description                                 |
| ---------- | ------------------------------------------- |
| `ls`       | Lists files and directories.                |
| `cd`       | Changes the current directory.              |
| `pwd`      | Prints the current working directory.       |
| `mkdir`    | Creates a new directory.                    |
| `rm`       | Removes a file or directory.                |
| `cat`      | Displays the content of a file.             |
| `touch`    | Creates a new empty file.                   |
| `echo`     | Prints text to the terminal.                |
| `monitor`  | Displays system resource usage.             |
| `hostname` | Displays the system hostname.               |
| `uptime`   | Shows how long the system has been running. |
| `ps`       | Displays running processes.                 |
| `kill`     | Terminates a process by its ID.             |
| `ping`     | Pings a host to check network connectivity. |
| `curl`     | Makes a web request.                        |
| `zip`      | Compresses files into a `.zip` archive.     |
| `unzip`    | Extracts files from a `.zip` archive.       |
| `history`  | Shows the command history.                  |
| `help`     | Displays a list of all commands.            |
| `exit`     | Exits the terminal.                         |

---

## Dependencies

* [`rich`](https://github.com/Textualize/rich) → Beautiful terminal output and formatting
* [`psutil`](https://github.com/giampaolo/psutil) → Cross-platform system monitoring
* [`pyfiglet`](https://github.com/pwaller/pyfiglet) → ASCII art for the welcome banner
