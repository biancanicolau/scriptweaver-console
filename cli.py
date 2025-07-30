from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt
from rich import print
import os

from api_utils import get_current_ip, get_random_joke  # adăugăm și alte funcții pe parcurs

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = figlet_format("Scriptweaver", font="big")
    console.print(banner, style="bold cyan")

def menu():
    print("\n[bold magenta]Welcome, Scriptweaver![/bold magenta]")
    print("[green]1.[/green] Show current IP address")
    print("[green]2.[/green] Get a random joke")
    print("[green]3.[/green] Write mock data to DynamoDB")
    print("[green]4.[/green] Read data from DynamoDB")
    print("[green]5.[/green] Trigger Lambda (or simulate)")
    print("[green]0.[/green] Exit\n")

def main():
    while True:
        clear_screen()
        show_banner()
        menu()

        choice = Prompt.ask("\n[bold yellow]Choose an option[/bold yellow]", choices=["0", "1", "2", "3", "4", "5"])

        if choice == "0":
            print("\n[italic]Goodbye, Scriptweaver.[/italic]")
            break

        elif choice == "1":
            print(">>> [cyan]Fetching IP address...[/cyan]")
            ip = get_current_ip()
            print(f"\nYour current IP is: [bold green]{ip}[/bold green]")

        elif choice == "2":
            print(">>> [cyan]Getting a joke...[/cyan]")
            joke = get_random_joke()
            print(f"\n[italic yellow]{joke}[/italic yellow]")


        elif choice == "3":
            print(">>> [cyan]Writing to DynamoDB...[/cyan]")
            # TODO

        elif choice == "4":
            print(">>> [cyan]Reading from DynamoDB...[/cyan]")
            # TODO

        elif choice == "5":
            print(">>> [cyan]Triggering Lambda (simulated)...[/cyan]")
            # TODO

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
