class Customer:
    """Customer Details"""

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return "<class 'Customer'>"

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


