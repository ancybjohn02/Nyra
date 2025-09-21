import pyfiglet
from rich.console import Console
from rich.text import Text
import sys

def clear_screen():
    """Clears the terminal screen."""
    print("\033c", end="")

def run_nyra_terminal():
    console = Console()
    clear_screen()
    # ascii_art = pyfiglet.figlet_format("NYRA", font="rectangles")
    
    ascii_art = r"""
__   ___   _______  ___  
| \ | \ \ / / ___ \/ _ \ 
|  \| |\ V /| |_/ / /_\ \
| . ` | \ / |    /|  _  |
| |\  | | | | |\ \| | | |
\_| \_/ \_/ \_| \_\_| |_/
                         
                         
     """
    start_color = (0, 102, 255)  # Blue
    mid_color = (153, 51, 255)   # Purple
    end_color = (255, 102, 178)  # Pink

    lines = ascii_art.splitlines()
    gradient_text = Text()

    total_length = sum(len(line) for line in lines)
    current_pos = 0

    for line in lines:
        for char in line:
            pos = current_pos / total_length
            current_pos += 1

            if pos < 0.5:
                r = int(start_color[0] + (mid_color[0] - start_color[0]) * (pos / 0.5))
                g = int(start_color[1] + (mid_color[1] - start_color[1]) * (pos / 0.5))
                b = int(start_color[2] + (mid_color[2] - start_color[2]) * (pos / 0.5))
            else:
                r = int(mid_color[0] + (end_color[0] - mid_color[0]) * ((pos - 0.5) / 0.5))
                g = int(mid_color[1] + (end_color[1] - mid_color[1]) * ((pos - 0.5) / 0.5))
                b = int(mid_color[2] + (end_color[2] - mid_color[2]) * ((pos - 0.5) / 0.5))

            # Color everything, including spaces
            gradient_text.append(char if char != "" else " ", style=f"rgb({r},{g},{b})")
        gradient_text.append("\n")

    # Print solid gradient-painted banner
    console.print(gradient_text, justify="center")

    console.print("[bold bright_blue]Type 'help' for a list of commands.[/bold bright_blue]\n")
