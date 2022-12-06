from datetime import datetime
import json
from customer import Customer
from invoiceItem import InvoiceItem
from item import Item

class CashRegister:
    """Cash Register for each customer"""

    def __init__(self, customer):
        self.customer = customer
        self.items: dict[str, InvoiceItem] = {}
        self.purchaseDate = datetime.now()
        self.invoiceTotal = 0

    def __repr__(self):
        return "<class 'CashRegister'>"

    def __str__(self):
        return f"Customer: {self.customer} \t\t\tTotal Items: {len(self.items)}"
    
    def getItemlength(self):
        return len(self.items)

    def decInvoiceTotal(self, item):
        """Increment the total invoice value each time an item is added"""
        self.invoiceTotal -= item.getSubTotal()

    def incInvoiceTotal(self, item):
        """Decrement the total invoice value each time an item is removed"""
        self.invoiceTotal += item.getSubTotal()
        
    def addItems(self, item, qty):
        """Add's an item to cash register"""
        if item.name not in self.items:
            newItem = InvoiceItem(item, qty)
            self.items[item.name] = newItem
            self.incInvoiceTotal(newItem)
        else:
            print(f"{item.name} already in cart")
        
    def updateItem(self, item, qty):
        if item.name in self.items:
            oldItem = self.items[item.name]
            self.decInvoiceTotal(oldItem)
            
            newItem = InvoiceItem(item, qty)
            self.items[item.name] = newItem
            self.incInvoiceTotal(newItem)

        else:
            print(f"{item.name} not in cart")

    def removeItem(self, item):
        """Remove items from cash register"""
        if item.name in self.items:
            oldItem = self.items[item.name]
            self.decInvoiceTotal(oldItem)

            del self.items[item.name]
        else:
            print(f"{item.name} not in cart")

    def getInvoiceTotal(self):
        return self.invoiceTotal

    def displayInvoice(self):
        print()
        print("+" * 70)
        print("\t\t\t  Reciept")
        print("+" * 70)
        print(self)
        print(f"Date: {self.purchaseDate.strftime('%B %d, %Y')}")
        print("-" * 70)
        for item in self.items.values():
            print(item)
        print("-" * 70)
        print(f"Total Price:  {self.getInvoiceTotal():.2f}")
        print("+" * 70)


    def getItemAsDict(self):
        items_dict = {}

        for item_name, invoice_item in self.items.items():
            items_dict[item_name] = invoice_item.dict()
        return items_dict
    
    def dict(self):
        """Returns dictionary representation of Cash Register"""
        CashRegister = {
            "Customer": self.customer.dict(),
            "items" : self.getItemAsDict(),
            "Purchase Date": self.purchaseDate.strftime("%B %d, %Y"),
            "Invoice Total" : self.getInvoiceTotal()
        }
        return CashRegister

    def toJSON(self):
        return json.dumps(self.dict(), indent = 4, sort_keys= True)

