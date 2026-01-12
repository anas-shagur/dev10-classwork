import csv
import statistics

FILE_PATH = "players.csv"

def menu():
    select = 0
    while True:
        select = int(input("""Main Menu
=========
0. Exit
1. List players
2. Calculate Central Tendencies
3. Add a player
Select [0-3]: """))
        match select:
            case 0:
                print("Exiting application...")
                break
            case 1:
                list_players()
            case 2:
                calculate_central_tendencies()
            case 3:
                add_player(FILE_PATH)
            case _:
                print("Invalid selection. Try again.")        

def list_players():
    records = parse_file(FILE_PATH)
    print("\nPlayers")
    print("========")
    print(f"{'ID':<3} {'Name':<20} {'Club':<20} {'Nation':<15} {'Ht(cm)':<7} {'G/Game'}")

    for row in records:
        print(f"{row[0]:<3} {row[1]:<20} {row[2]:<20} {row[3]:<15} {row[4]:<7} {row[5]:.2f}")
    
    print()

def parse_file(file_path):
    players = []

    with open(file_path, encoding="utf-8", newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            player = (
                int(row[0]),        
                row[1],             
                row[2],             
                row[3],             
                int(row[4]),        
                float(row[5])       
            )
            players.append(player)

    return players

def calculate_central_tendencies():
    records = parse_file(FILE_PATH)

    goals = [player[5] for player in records]

    mean_goals = statistics.mean(goals)
    median_goals = statistics.median(goals)

    try:
        mode_goals = statistics.mode(goals)
    except statistics.StatisticsError:
        mode_goals = "No unique mode"

    print("\nCentral Tendencies")
    print("==================")
    print(f"Sample Size: {len(goals)}")
    print(f"Mean goals per game: {mean_goals:.3f}")
    print(f"Median goals per game: {median_goals:.3f}")
    print(f"Mode goals per game: {mode_goals}\n")

def read_required_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error, enter a valid value.")

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error, value must be a positive integer.")
        except ValueError:
            print("Error, invalid integer.")

def read_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0 and value < 1:
                return value
            print("Error, value must be a positive number that is less than 1.")
        except ValueError:
            print("Error, invalid number.")

def add_player(file_path):
    records = parse_file(file_path)

    if records:
        next_id = max(player[0] for player in records) + 1
    else:
        next_id = 1

    print("\nAdd a Player")
    print("============")

    name = read_required_string("Player Name: ")
    club = read_required_string("Club: ")
    nationality = read_required_string("Nationality: ")
    height_cm = read_int("Height (cm): ")
    avg_goals = read_positive_float("Average Goals Per Game: ")

    new_player = [
        next_id,
        name,
        club,
        nationality,
        height_cm,
        avg_goals
    ]

    with open(file_path, "a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_player)

    print("\nPlayer added successfully.")

menu()
