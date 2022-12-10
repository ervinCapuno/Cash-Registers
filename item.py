class Item:
    """Simple Item for cash register"""

    def __init__(self, ids, name, price):
        self.ids = ids
        self.name = name
        self.price = price

    def __repr__(self):
        return "<class 'Item'>"

    def __str__(self):
        return f"{self.ids} {self.name} {self.price}"

    def getId(self):
        return self.ids

    def getName(self):
        return self.name
        
    def getprice(self):
        return self.price

