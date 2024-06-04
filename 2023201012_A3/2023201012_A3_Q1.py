#need to handle edge cases
from tabulate import tabulate
import csv
#Each participant is stored in a dictionary named 
info={}
while(1):
    print("Menu:")
    print("1.Add participant(s)")
    print("2.Add Expenses")
    print("3.Show all participants")
    print("4.Show Expenses")
    print("5.Exit")
    print("Enter Your Choice: ",end="")
    choice=input()
    if(choice=="1"):
        #Add participants
        print("Enter Participant names seperated by commas")
        participants=list(input().split(","))
        for i in participants:
            if i not in info:   
                info[i]=0
            else:
                print("Participant named {0} Already Exists!!,So ignored".format(i))
        print("Participants Added Successfully :)")
    elif(choice=="2"):
        #Add Expenses
        flag=True
        print("Enter the name of person who paid the money: ",end="")
        bakara=input()
        if bakara not in info:
                print("There is no such participant named {0}".format(bakara))
                print("Try adding to the participants and enter again")
                print(".................cancelling the transaction .............")
                flag=False
                continue
        print("Amount paid by the person: ",end="")
        Amount=int(input())
        print("Mention all the  participants that are involved in this payment: ")
        participantsInvolved=list(input().split(","))
        spentAmt=Amount/len(participantsInvolved)
        for i in participantsInvolved:
            if i not in info:
                print("There is no such participant named {0}".format(i))
                print("Try adding to the participants and enter again")
                print(".................cancelling the transaction .............")
                flag=False
                break
            else:
                info[i]-=spentAmt
        if(flag==False):
            #reset all the transactions
            for i in participantsInvolved:
                if i not in info:
                    break
                else:
                    info[i]+=spentAmt
        if(flag):
            info[bakara]+=Amount
    elif(choice=="3"):
        #Show all participants
        for i in info:
            print(i)
    elif(choice=="4"):
        col_names=['Participant_name','Amount','Owes or GetsBack']
        keys=list(info.keys())
        values=list(info.values())
        data=[]
        for i in range(len(keys)):
            data.append([keys[i],abs(values[i]),"Owes" if(values[i]<0)else "GetsBack"])
        print(tabulate(data,headers=col_names,tablefmt="fancy_grid",showindex="always"))
    elif(choice=="5"):
        col_names=['Participant_name','Amount','Owes or GetsBack']
        keys=list(info.keys())
        values=list(info.values())
        data=[]
        for i in range(len(keys)):
            data.append([keys[i],abs(values[i]),"Owes" if(values[i]<0)else "GetsBack"])
        filename = "expenses.csv"
        with open(filename, 'w') as csvfile:  
            # creating a csv writer object  
            csvwriter = csv.writer(csvfile)  
            # writing the header
            csvwriter.writerow(col_names)  
            # writing the data rows  
            csvwriter.writerows(data) 
        break
    
