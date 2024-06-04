import matplotlib.pyplot as plt
import numpy as np
import csv


def read_from_csv(Participants):
    filepath = input()
    try:
        with open(filepath, 'r') as file:
            # reads into dictionary
            csvreader = csv.DictReader(file)
            for participant in csvreader:
                Participants.append(participant)
            print("Data has been read from csv sucessfully")
    except OSError as oserr:
        print("OSError: ", oserr)
        read_from_csv(Participants)
    except ValueError:
        print("No data available")
        read_from_csv(Participants)


print("Enter the path of file for expenses: ")
Participants = []
read_from_csv(Participants)
owes_list = []
owes_amt = []
getsBack_list = []
getsBack_amt = []
owed_amt = 0
gets_back_amt = 0
for participant in Participants:
    if (participant["Owes or GetsBack"] == "Owes"):
        owes_list.append(participant["Participant_name"])
        owes_amt.append(float(participant["Amount"]))
        owed_amt += float(participant["Amount"])
    else:
        getsBack_list.append(participant["Participant_name"])
        getsBack_amt.append(float(participant["Amount"]))
        gets_back_amt += float(participant["Amount"])
# Owes
plt.figure("Owes",figsize=(10,10))
max_value_owes = max(owes_amt)
max_owes = [i for i, x in enumerate(owes_amt) if x == max_value_owes]
# this gives all the indices whose value is equal to max value
owes_explode = [0.1 if i in max_owes else 0 for i in range(len(owes_amt))]
# this makes all the indices in max owes to explode
plt.pie(owes_amt, labels=owes_list, autopct='%1.1f%%', explode=owes_explode)
plt.legend(owes_list, loc="best", title="Amount="+str(int(owed_amt))+"\nOwes")
# GetsBack
plt.figure("GetsBack",figsize=(10,10))
max_value_getsBack = max(getsBack_amt)
max_getsBack = [i for i, x in enumerate(
    getsBack_amt) if x == max_value_getsBack]
getsBack_explode = [
    0.1 if i in max_getsBack else 0 for i in range(len(getsBack_amt))]
plt.pie(getsBack_amt, labels=getsBack_list,
        autopct='%1.1f%%', explode=getsBack_explode)
plt.legend(getsBack_list, loc="best", title="Amount=" +
           str(int(gets_back_amt))+"\nGetsBack")
# Plottings
plt.show()


print("Enter the file path for Cricket Players: ")
Players = []
read_from_csv(Players)
names = []
roles = []
runs = []
balls = []
wickets = []
for player in Players:
    names.append(player["First-name"])
    roles.append(player["Role"])
    if(player["Role"] in ["batsmen","wk-batsmen","all-rounder"]):
        runs.append(player["Runs"])
    else:
        runs.append('0')
    balls.append(player["Balls"])
    if player["Role"] in ["bowler","all-rounder"]:
        wickets.append(player["Wickets"])
    else:
        wickets.append("0")
battingStrikeRates = []
bowlingStrikeRates = []
x = range(len(names))
for i in range(len(Players)):
    battingStrikeRates.append(float(runs[i])/float(balls[i]))
    bowlingStrikeRates.append(float(wickets[i])/float(balls[i]))
x = np.arange(len(names))
bar_width = 0.3

plt.figure("StrikeRates Comparision")
plt.bar(x - bar_width/2, battingStrikeRates,
        width=bar_width, label='Batting StrikeRate')
plt.bar(x + bar_width/2, bowlingStrikeRates,
        width=bar_width, label='Bowling StrikeRate')
plt.xlabel('Players')
plt.ylabel('Strike Rate')
plt.title('Batting and Bowling Strike Rates')
plt.xticks(x, names)
plt.legend()

plt.tight_layout()
plt.show()
