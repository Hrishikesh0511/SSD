import csv
from tabulate import tabulate
Players = []


def read_from_csv():
    filepath = input("Enter file path: ")
    try:
        with open(filepath, 'r') as file:
            # reads into dictionary
            csvreader = csv.DictReader(file)
            for player in csvreader:
                Players.append(player)
            print("Data has been read from csv sucessfully")
    except OSError as oserr:
        print("OSError: ", oserr)
        read_from_csv()
    except ValueError:
        print("No data available")
        read_from_csv()


def display_entries():
    print(tabulate(Players, headers="keys",
          tablefmt="fancy_grid", showindex="always"))


def add_entry():
    strikerate = "dummy"
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    nationality = input("Enter nationality: ")
    role = input("Enter role among [batsmen,wk-batsmen,bowler,all-rounder]: ")
    runs = input("Enter runs: ")
    balls = input("Enter balls: ")
    wickets = input("Enter wickets: ")
    try:
        strikerate = input("Enter strike rate: ")
    except ValueError:
        pass
    if (role.lower() not in ["batsmen", "wk-batsmen", "bowler", "all-rounder"]):
        print("Enter a valid role and try updating again")
        return
    if (strikerate):
        pass
    else:
        try:
            if (role.lower() == "batsmen" or role.lower() == "wk-batsmen"):
                strikerate = int(runs)/int(balls)
            elif (role.lower() == "bowler"):
                strikerate = int(wickets)/int(balls)
            elif (role.lower() == "all-rounder"):
                strikerate = max(int(runs)/int(balls), int(wickets)/int(balls))
        except ZeroDivisionError:
            print("Balls cannot be zero try adding again")
            return 
    player = {
        "First-name": first_name,
        "Last-name": last_name,
        "Age": age,
        "Nationality": nationality,
        "Role": role,
        "Runs": runs,
        "Balls": balls,
        "Wickets": wickets,
        "StrikeRate": strikerate
    }
    Players.append(player)
    print("Added entry succesfully")


def remove_entry():
    name = list(input(
        "Enter player name in this format to remove:<first_name><space><last_name>: ").split())
    flag = True
    for player in Players:
        if (player["First-name"] == name[0] and player["Last-name"] == name[1]):
            Players.remove(player)
            flag = False
    print("Player data removed successfully")
    if (flag):
        print("There is no such player to remove")


def update_entry():
    name = list(input(
        "Enter player name in this format to remove:<first_name><space><last_name>: ").split())
    flag = False
    for player in Players:
        if (player["First-name"] == name[0] and player["Last-name"] == name[1]):
            flag = True
            new_age = input("Enter updated age: ")
            new_nationality = input("Enter updated nationality: ")
            new_role = input(
                "Enter updated role among [batsmen,wk-batsmen,bowler,all-rounder]")
            new_runs = input("Enter updated runs: ")
            new_balls = input("Enter updated balls: ")
            new_wickets = input("Enter updated wickets: ")
            try:
                strikerate = input("Enter strike rate: ")
            except ValueError:
                pass
            if (new_role.lower() not in ["batsmen", "wk-batsmen", "bowler", "all-rounder"]):
                print("Enter a valid role and try updating again ")
                return
            if strikerate:
                pass
            else:
                try:
                    if (new_role.lower() == "batsmen" or new_role.lower() == "wk-batsmen"):
                        strikerate = int(new_runs)/int(new_balls)
                    elif (new_role.lower() == "bowler"):
                        strikerate = int(new_wickets)/int(new_balls)
                    elif (new_role.lower() == "all-rounder"):
                        strikerate = max(int(new_runs)/int(new_balls),
                                        int(new_wickets)/int(new_balls))
                except ZeroDivisionError:
                    print("Balls cannot be zero Try updating again.")
                    return 
            player.update({
                "Age": new_age,
                "Nationality": new_nationality,
                "Role": new_role,
                "Runs": new_runs,
                "Balls": new_balls,
                "Wickets": new_wickets,
                "StrikeRate": strikerate
            })
            print("Player data updated sucessfully!!")
    if (flag == False):
        print("No such player to update")


def search_entry():
    search_attr = input("Enter attribute you want to search on:")
    if (search_attr in Players[0].keys()):
        search_query = input("Enter "+search_attr+" to search: ")
        display_list = [i for i in Players if i[search_attr] == search_query]
        if (display_list):
            print(tabulate(display_list, headers="keys", tablefmt="fancy_grid"))
        else:
            print("No data to display")
    else:
        print("No such attribute: " + search_attr)


def save_in_csv():
    filename = "GachibowliGorillas.csv"
    if (len(Players) > 0):
        data = []
        for i in Players:
            data.append(i.values())
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the header
            csvwriter.writerow(Players[0].keys())
            # writing the data rows
            csvwriter.writerows(data)
        print("Data saved successfully in "+filename)
    else:
        print("No data to save")


def menu():
    while (1):
        print("1: Read/Load entries from a csv file")
        print("2: Display directory on terminal")
        print("3: Add a new entry")
        print("4: Remove an entry")
        print("5: Update an entry")
        print("6: Search for entries")
        print("7: Save in csv")
        print("8: Exit")
        print("Select your choice: ")
        choice = int(input())
        if (choice == 1):
            read_from_csv()
        elif (choice == 2):
            display_entries()
        elif (choice == 3):
            add_entry()
        elif (choice == 4):
            remove_entry()
        elif (choice == 5):
            update_entry()
        elif (choice == 6):
            search_entry()
        elif (choice == 7):
            save_in_csv()
        elif (choice == 8):
            break
        else:
            print("Unknown choice")


menu()
