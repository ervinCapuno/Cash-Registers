from item import Item

class InvoiceItem:

    def __init__(self, item, qty):
        self.item = item
        self.qty = qty
        self.idItem = item.ids
        self.subTotal = (item.price * qty)

    def __repr__(self):
        return "<class 'IvoiceItem'>"

    def __str__(self):
        return f"ID: {self.idItem}\t\t Item: {self.item.name}\t  Qty: {self.qty}\t Sub Total: {self.getSubTotal():.2f}"
        

    def getSubTotal(self):
        return self.subTotal

    