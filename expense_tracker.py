# Import necessary modules
from expense import Expense  # Import the Expense class from the expense module
import calendar  # Import the calendar module for date-related functionalities
import datetime  # Import the datetime module for working with dates and times


# Define the main function
def main():
    print(f"Running Expense Tracker!")  # Print a message indicating that the Expense Tracker is running

    # Get user input for expense.
    expense = get_user_expense()  # Call the get_user_expense function to get expense details from the user

    # Define the file path for storing expenses
    expense_file_path = "file\expenses.csv"  # Define the file path where expenses will be saved

    budget = 7000  # Set the budget amount

    # Write the user's expense to a file
    save_user_expense(expense, expense_file_path)  # Call the save_user_expense function to save the user's expense

    # Read the file and summarize expenses
    summarize_expense(expense_file_path, budget)  # Call the summarize_expense function to summarize expenses


# Function to get user expense details
def get_user_expense():
    print(f"Getting User Expense")  # Print a message indicating that user expense details are being obtained

    # Get expense details from the user
    expense_name = input("Enter expense name: ")  # Get the name of the expense from the user
    expense_amount = float(input("Enter expense amount: "))  # Get the amount of the expense from the user

    # Define expense categories
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    # Loop to prompt user to select a category
    while True:
        print("Select a category: ")  # Print a message prompting the user to select a category
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")  # Print category options for the user to select

        # Get user input for selecting a category
        value_range = f"[1 - {len(expense_categories)}]"  # Define the valid range of category numbers
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1  # Get user input for category selection

        # Check if the selected category index is valid
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]  # Get the selected category
            new_expense = Expense(  # Create a new Expense object with user input
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense  # Return the new expense object
        else:
            print("Invalid category. Please try again!")  # Print an error message for invalid category


# Function to save user expense to a file
def save_user_expense(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")  # Print a message indicating that user expense is being saved

    # Open the expense file in append mode and write the expense details to it
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")  # Write expense details to the file


# Function to summarize user expenses
def summarize_expense(expense_file_path, budget):
    print(f"Summarizing User Expense")  # Print a message indicating that user expenses are being summarized

    expenses: list[Expense] = []  # Initialize an empty list to store Expense objects

    # Open the expense file in read mode and read expense details
    with open(expense_file_path, "r") as f:
        lines = f.readlines()  # Read all lines from the file
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")  # Split each line to extract expense details
            line_expense = Expense(  # Create an Expense object with the extracted details
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)  # Append the Expense object to the list of expenses

    # Calculate total expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # Print expenses by category
    print("Expenses By Category:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    # Calculate total spent
    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: ${total_spent:.2f}")

    # Get the current date
    now = datetime.datetime.now()

    # Calculate remaining budget
    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate remaining number of days in the current month
    remaining_days = days_in_month - now.day

    # Calculate daily budget
    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget Per Day: ${daily_budget:.2f}"))  # Print the daily budget in green


# Function to make text in terminal turn green
def green(text):
    return f"\033[92m{text}\033[0m"  # Return the text in green color


# Entry point of the program
if __name__ == '__main__':
    main()  # Call the main function when the script is executed
