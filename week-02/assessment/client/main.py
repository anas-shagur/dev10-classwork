# Simple API dataset

import numpy as np
import scipy.stats as stats
from requests.exceptions import HTTPError
from rich.console import Console
from rich.table import Table

import console_io as cio
from players_api import PlayerAPI
from models import Player

api = PlayerAPI("http://127.0.0.1:5000")


def choose_menu():
    cio.print_header("Main Menu")
    print("0. Exit")
    print("1. List Players")
    print("2. Calculate Central Tendencies")
    print("3. Add a Player")

    return cio.read_int("Select [0-3]: ", 0, 3)


def list_players():
    cio.print_header("Players")
    
    table = Table(show_header=True, header_style="bold magenta", title="Players")
    table.add_column("ID", style="dim")
    table.add_column("Player Name")
    table.add_column("Club")
    table.add_column("Nationality")
    table.add_column("Height (cm)", justify="right")
    table.add_column("Avg Goals/Game", justify="right")

    for player in api.find_all():
        table.add_row(
            str(player.id),
            f"[cyan]{player.player_name}[/cyan]",
            player.club,
            player.nationality,
            str(player.height_cm),
            f"[yellow]{player.avg_goals_per_game:.2f}[/yellow]",
        )

    console = Console()
    console.print(table)


def calculate_central_tendencies():
    cio.print_header("Central Tendencies")

    players = api.find_all()
    
    if not players:
        print("No players in database.")
        return
    
    goals = [player.avg_goals_per_game for player in players]

    result = stats.describe(goals)

    print(f"Sample Size: {result.nobs}")
    print(f"Mean goals per game: {result.mean}")
    print(f"Median goals per game: {np.median(goals)}")
    print(f"Mode goals per game: {stats.mode(goals).mode}")
    print(f"Min goals per game: {result.minmax[0]}")
    print(f"Max goals per game: {result.minmax[1]}")
    print(f"Variance: {result.variance}")
    print(f"Skewness: {result.skewness}")
    print(f"Kurtosis: {result.kurtosis}")


def add_player():
    cio.print_header("Add a Player")

    player = Player(
        id=None,
        player_name=cio.read_required_string("Player Name: "),
        club=cio.read_required_string("Club: "),
        nationality=cio.read_required_string("Nationality: "),
        height_cm=cio.read_positive_int("Height (cm): "),
        avg_goals_per_game=cio.read_positive_float("Avg Goals per Game: "),
    )

    created = api.post(player)
    print(f"Player ID {created.id} created.")


def choose(choice):
    match choice:
        case 1:
            list_players()
        case 2:
            calculate_central_tendencies()
        case 3:
            add_player()
        case _:
            print("Invalid choice. Please try again.")


def main():
    choice = choose_menu()
    while choice != 0:
        try:
            choose(choice)
        except HTTPError as e:
            print(f"HTTP Error: {e}")

        choice = choose_menu()

    cio.print_header("Goodbye")


if __name__ == "__main__":
    main()