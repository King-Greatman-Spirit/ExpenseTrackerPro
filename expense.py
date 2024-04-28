class Expense:  # Define a class named Expense

    def __init__(self, name, category, amount) -> None:  # Define the initialization method (__init__) with three parameters: name, category, and amount
        self.name = name  # Initialize the 'name' attribute of the Expense object
        self.category = category  # Initialize the 'category' attribute of the Expense object
        self.amount = amount  # Initialize the 'amount' attribute of the Expense object

    def __repr__(self):  # Define the representation method (__repr__) to provide a string representation of the Expense object
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"  # Return a string representation of the Expense object
