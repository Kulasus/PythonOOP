from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def withdraw(self, ammount):
        return 0

    @abstractmethod
    def insert(self, ammount):
        return 0

    @abstractmethod
    def display(self):
        return 0

class SavingAccount(Account):
    def __init__(self, userName, initalDeposit):
        self.userName = userName
        self.balance = initalDeposit
        self.accountNumber = randint(10000,99999)
        print("Your account number is {}. Please keep it secret.".format(self.accountNumber))
    
    def withdraw(self, ammount):
        if ammount < 0 :
            print("Invalid ammount to withdraw! Ammount must be a positive number or zero!")
        elif self.balance - ammount < 0:
            print("Invalid ammount to withdraw! Not enought money!")
        else: 
            self.balance -= ammount

    def insert(self, ammount):
        if ammount >=0:
            self.balance += ammount
        else:
            print("Invalid ammount to inser! Ammount must be a positive number or zero!")

    def display(self):
        print("Your balance is {}.".format(self.balance))

class Bank:
    def __init__(self):
        self.savingAccounts = []

    def addSavingAccount(self, savingAccount):
        self.savingAccounts.append(savingAccount)


class Terminal:
    def __init__(self, bank):
        self.bank = bank

    def showMenu(self):
        print()
        print("Enter 1 for creating new saving account")
        print("Enter 2 for accessing existing saving account")
        print("Enter 3 for exit")
        print()

    def showOptionOne(self):
        print("Enter your name:")
        userName = input()
        print("Enter your initial deposit (0-n)")
        userInitialDeposit = float(input())
        savingAccount = SavingAccount(userName, userInitialDeposit)
        self.bank.addSavingAccount(savingAccount)
        print("Your saving account was sucesfully created.")


    def showOptionTwo(self):
        print("Enter your name username: ")
        userName = input()
        savingAccount = self.findAccountByUsername(userName)
        if savingAccount is not None:
            print("Enter your account secret number: ")
            accountNumber = int(input())
            if savingAccount.accountNumber != accountNumber:
                print("Invalid account number.")
            else:
                self.showAccountAccessMenuInitialMessage(savingAccount)
                self.accountAccessMenu(savingAccount)
        else:
            print("Account with this username does not exist.")
            
    def showOptionTwoAccountAccess(self):
        print("Enter 1 to withdraw cash")
        print("Enter 2 to insert cash")
        print("Enter 3 to dispaly your balance")
        print("Enter 4 to log out")

    def accountAccessMenu(self, savingAccount):
        self.showOptionTwoAccountAccess()
        userInput = int(input())
        self.accountAccessMenuResolution(savingAccount, userInput)

    def showAccountAccessMenuInitialMessage(self, savingAccount):
        print()
        print("Welcom {} to your saving account {}.".format(savingAccount.userName, savingAccount.accountNumber))

    def accountAccessMenuResolution(self, savingAccount, userInput):
        if userInput == 1:
            print("Enter ammount to withdraw:")
            ammount = int(input())
            savingAccount.withdraw(ammount)
            self.accountAccessMenu(savingAccount)
        elif userInput == 2:
            print("Enter ammount to insert:")
            ammount = int(input())
            savingAccount.insert(ammount)
            self.accountAccessMenu(savingAccount)
        elif userInput == 3:
            savingAccount.display()
            self.accountAccessMenu(savingAccount)
        elif userInput == 4:
            pass

    def menuResolution(self):
        userInput = int(input())
        if userInput == 1:
            self.showOptionOne()
        if userInput == 2:
            self.showOptionTwo()
        if userInput == 3:
            quit()

    def findAccountByUsername(self, userName):
        for savingAccount in self.bank.savingAccounts:
            if savingAccount.userName == userName:
                return savingAccount

    def run(self):
        while True:
            self.showMenu()
            self.menuResolution()


myBank = Bank()
myTerminal = Terminal(myBank)
myTerminal.run()
