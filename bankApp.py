'''
Description: Project 6 Bank App problem
Written By: Avery Einhorn
Date: 12/4/2018
'''
names=["Alec","Ezra","Michael","Dakota"] #global list of users
balances=[300,200,1000,400] #global list of balances indexed to global list of users
namesCounter=0 #global username index that changes each time a user is selected and is used to process all requests

def deposit(amount,counter):
    if amount<=0:
        deposit(float(input("Invalid deposit amount. Please enter a positive number: ")),counter)
    newBalance=[]
    balanceCounterOne=counter
    global balances
    for i in balances:
        if balanceCounterOne==0:
            i+=amount
            balanceCounterOne-=1
        else:
            balanceCounterOne-=1
        newBalance+=[i]
    balances=newBalance
    return
def displayBalance(name):
    balanceCounterOne=name
    for i in balances:
        if balanceCounterOne==0:
            print("Your balance is now "+str(float(i)))
            break
        else:
            balanceCounterOne-=1
def withdraw(amount,counter):
    if amount<=0:
        withdraw(float(input("Invalid deposit amount. Please enter a positive number: ")),counter)
    newBalance=[]
    balanceCounterOne=counter
    global balances
    for i in balances:
        if balanceCounterOne==0:
            if i<amount: #validates for sufficient funds
                print("You do not have enough balance to withdraw that amount. Sorry.")
                return
            i-=amount
            balanceCounterOne-=1
        else:
            balanceCounterOne-=1
        newBalance+=[i]
    balances=newBalance
    return

def bank(inputName): #the main functional "app"
    namesCounter=0
    for i in names:
        if inputName==i:
            break
        else:
            namesCounter+=1
    if namesCounter>(len(names)-1):
        bank(str(input("Sorry you are not a customer. Please enter a valid customer name: ")))
        return
    print("Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit")
    userChoice=str(input())
    if userChoice=="d" or userChoice=="w" or userChoice=="b" or userChoice=="c" or userChoice=="e":
        if userChoice=="d":
           deposit(float(input("How much would you like to deposit? ")), namesCounter)
           displayBalance(namesCounter)
           return bank(inputName)
        elif userChoice=="w":
            withdraw(float(input("How much would you like to withdraw? ")), namesCounter)
            displayBalance(namesCounter)
            return bank(inputName)
        elif userChoice=="b":
            displayBalance(namesCounter)
            return bank(inputName)
        elif userChoice=="c":
            print("Alright, go ahead and change your name.")
            bank(str(input("What is your name? ")))
            return
        elif userChoice=="e":
            return
    else:
        print("Invalid menu option, please try again:")
        print("Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit")
        userChoice=str.lower(input())
    namesCounter=0

bank(str(input("What is your name? "))) #the original function call