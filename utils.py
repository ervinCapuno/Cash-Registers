class ErrorHandling:

    @staticmethod
    def choiceError():
        while True:
            try:
                itemId = int(input("Enter the ID of the Item: "))
                return itemId
                break
            except:
                print("Enter a valid number!")  

    @staticmethod
    def QtyError():
        while True:
            try:
                qty = int(input("Quantity of your order: "))
                while True:
                    if qty > 0:
                        return qty
                    else:
                        print("Enter must be a higher than zero")
                    break
            except :
                print("Enter a valid number!")

    @staticmethod
    def inputError():
        while True:
            try:
                inp = input("Enter your choice: ")
                return inp
                break
            except:
                print("Invalid input!")

    @staticmethod
    def inputChoice():
        while True:
            choice = str(input("Do you want to continue[y/n]: "))
            if choice.upper() == "Y":
                return choice
                break
            elif choice.upper() == "N":
                return choice
                break
            else:
                print("Invalid Input!")


    @staticmethod
    def userNameValue(pos):
        non_valid_char = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        while True:
            inp = input(f"Enter your {pos} name: ")
            non_valid_char_counter = 0
            for char in non_valid_char:
                if char in inp:
                    non_valid_char_counter += 1
            if non_valid_char_counter > 0:
                print("Invalid Input! Name must contains alphabets!")
            else:
                break
        return inp