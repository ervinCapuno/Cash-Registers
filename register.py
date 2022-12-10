from cashRegister import CashRegister
from customer import Customer
from item import Item
import os
from tabulate import tabulate
from utils import ErrorHandling as EH


#global variables
#getting the name of the customer
firstName = EH.userNameValue("First")
lastName = EH.userNameValue("Last")

customer = Customer(firstName, lastName)
cRegister = CashRegister(customer)

#items
milk = Item(100, "Milk", 59)
pencil = Item(101, "Pencil", 8)
biscuits = Item(102, "biscuit", 15)
energyDrink = Item(103, "Coke", 20)
shoes = Item(104, "Shoes", 200)
slippers = Item(105, "Slippers", 75)



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

    showItems()
    os.system('cls')
    showItems()
    selectItem = 'Y'
    while selectItem.upper() == 'Y':
        order = EH.choiceError()
        if order == 100:
            qty = EH.QtyError()
            cRegister.addItems(milk, qty)
        elif order == 101:
            qty = EH.QtyError()
            cRegister.addItems(pencil, qty)
        elif order == 102:
            qty = EH.QtyError()
            cRegister.addItems(biscuits, qty)
        elif order == 103:
            qty = EH.QtyError()
            cRegister.addItems(energyDrink, qty)
        elif order == 104:
            qty = EH.QtyError()
            cRegister.addItems(shoes, qty)
        elif order == 105:
            qty = EH.QtyError()
            cRegister.addItems(slippers, qty)
        else:
            print("ID Not Found! You entered a wrong id!")
        selectItem = EH.inputChoice()


#removing an item
def removes():
    os.system('cls')
    remRun = 'Y'
    while remRun.upper() == 'Y':
        if cRegister.getItemlength() > 0:
            cRegister.notOfficialInvoice()
            #cRegister.displayInvoice()
            remItem = EH.choiceError()
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
            
            remRun = EH.inputChoice()
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
            cRegister.notOfficialInvoice()
            updItem = EH.choiceError()
            updQty = EH.QtyError()
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
            updateRun = EH.inputChoice()
            os.system('cls')
        else:
            print("Looks like there are no items to update!")
            break

def mainMenu():
    while True:
        print("\t\t\tCHOOSE\n\n")
        print("[A]Add     [U] UPDATE       [R] REMOVE       [P]Print\n\n")
        choice = EH.inputError()
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

    while True:
        #calling the select function to select the item that the customer want to buy
        select()
        os.system('cls')
        mainMenu()
        os.system('cls')
        #printing the reciept
        if cRegister.getItemlength() > 0:
            cRegister.displayInvoice()
            break
        else:
            print("You didn't buy any item!")
                

if __name__ == '__main__':
    main()