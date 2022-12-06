from cashRegister import CashRegister
from customer import Customer
from item import Item
import os
from tabulate import tabulate


#global variables
#getting the name of the customer
firstName = str(input("What is your first name: "))
lastName = str(input("What is your last name: "))
customer = Customer(firstName, lastName)
cRegister = CashRegister(customer)

#items
milk = Item(100, "Milk", 59)
pencil = Item(101, "Pencil", 8)
biscuits = Item(102, "biscuit", 15)
energyDrink = Item(103, "Coke", 20)
shoes = Item(104, "Shoes", 200)
slippers = Item(105, "Slippers", 75)

def choiceError():
    while True:
        try:
            itemId = int(input("Enter the ID of the Item: "))
            return itemId
            break
        except:
            print("Enter a valid number!")        

def QtyError():
    while True:
        try:
            qty = int(input("Quantity of your order: "))
            return qty
            break
        except:
            print("Enter a valid number!")

def inputError():
    while True:
        try:
            inp = input("Enter your choice: ")
            return inp
            break
        except:
            print("Invalid input!")


def inputChoice():
    while True:
        try:
            choice = input("Do you want to continue[y/n]: ")
            if choice.upper() == "Y":
                return choice
                break
            elif choice.upper() == "N":
                return choice
                break
            else:
                print("Cannot Recognized!")
        except:
            print("Invalid input!")

#show the items in the store
def showItems():
    print("\t\t\tMENU\n\n")
    table_headers = ["  ITEM ID   ", "  ITEM NAME   ", "    ITEM PRICE  "]
    menu = [
        [milk.getId(), milk.getName(), milk.getprice()],
        [pencil.getId(), pencil.getName(), pencil.getprice()],
        [biscuits.getId(), biscuits.getName(), biscuits.getprice()],
        [energyDrink.getId(), energyDrink.getName(), energyDrink.getprice()],
        [shoes.getId(), shoes.getName(), shoes.getprice()],
        [slippers.getId(), slippers.getName(), slippers.getprice()]
    ]

    print(tabulate(menu, headers = table_headers, tablefmt = "fancy_grid"))

#selecting the items
def select():
    os.system('cls')

    showItems()
    os.system('cls')
    showItems()
    selectItem = 'Y'
    while selectItem.upper() == 'Y':
        order = choiceError()
        if order == 100:
            qty = QtyError()
            cRegister.addItems(milk, qty)
        elif order == 101:
            qty = QtyError()
            cRegister.addItems(pencil, qty)
        elif order == 102:
            qty = QtyError()
            cRegister.addItems(biscuits, qty)
        elif order == 103:
            qty = QtyError()
            cRegister.addItems(energyDrink, qty)
        elif order == 104:
            qty = QtyError()
            cRegister.addItems(shoes, qty)
        elif order == 105:
            qty = QtyError()
            cRegister.addItems(slippers, qty)
        else:
            print("ID Not Found! You entered a wrong id!")
        selectItem = inputChoice()

def JSONinfo():
    print(cRegister.toJSON())


#removing an item
def removes():
    os.system('cls')
    remRun = 'Y'
    while remRun.upper() == 'Y':
        if cRegister.getItemlength() > 0:
            JSONinfo()
            #cRegister.displayInvoice()
            remItem = choiceError()
            if remItem == 100:
                cRegister.removeItem(milk)
            elif remItem == 101:
                cRegister.removeItem(pencil)
            elif remItem == 102:
                cRegister.removeItem(biscuits)
            elif remItem == 103:
                cRegister.removeItem(energyDrink)
            elif remItem == 104:
                cRegister.removeItem(shoes)
            elif remItem == 105:
                cRegister.removeItem(slippers)
            else:
                print("Invalid input!")
                os.system('cls')
            
            remRun = inputChoice()
            os.system('cls')

        else:
            print("Looks like there are no items to remove!")
            break
#update
def updates():
    os.system('cls')
    updateRun = 'Y'
    while updateRun.upper() == 'Y':
        if cRegister.getItemlength() > 0:
            #printing the reciept
            #cRegister.displayInvoice()
            JSONinfo()
            updItem = choiceError()
            updQty = QtyError()
            if updItem == 100:
                cRegister.updateItem(milk, updQty)
            elif updItem == 101:
                cRegister.updateItem(pencil, updQty)
            elif updItem == 102:
                cRegister.updateItem(biscuits, updQty)
            elif updItem == 103:
                cRegister.updateItem(energyDrink, updQty)
            elif updItem == 104:
                cRegister.updateItem(shoes, updQty)
            elif updItem == 105:
                cRegister.updateItem(slippers, updQty)
            else:
                print("Invalid input!")
                os.system('cls')
            updateRun = inputChoice()
            os.system('cls')
        else:
            print("Looks like there are no items to update!")
            break

def mainMenu():
    while True:
        print("\t\t\tCHOOSE\n\n")
        print("[A]Add     [U] UPDATE       [R] REMOVE       [P]Print\n\n")
        choice = inputError()
        if choice.upper() == "A":
            select()
        elif choice.upper() == "U":
            updates()
        elif choice.upper() == "R":
            removes()
        elif choice.upper() == "P":
            break
        else:
            print("Canno't Recognized!")
            os.system('cls')


#driver code
def main():
    os.system('cls')
    
    #calling the select function to select the item that the customer want to buy
    select()
    os.system('cls')
    mainMenu()
    os.system('cls')
    #printing the reciept
    cRegister.displayInvoice()

if __name__ == '__main__':
    main()