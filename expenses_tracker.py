# ----------------------------------------------------
# expense_tracker.py
# 
# A simple command-line expense tracker that allows a
# user to:
# 1) Add expenses (amount, category, description)
# 2) View all expenses
# 3) View total amount spent
# 4) View total spent by each category
# 5) Exit the program
# 
# Author: Your Name
# Date: 01/10/2025
# ----------------------------------------------------

# Global list to store all expenses
expenses = []

def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n====== EXPENSE TRACKER MENU ======")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. View total spent by category")
    print("5. Exit")

def add_expense():
    """
    Prompt user to input an expense amount (float),
    a category (string), and an optional description.
    Store the expense in the global 'expenses' list.
    Handle invalid inputs such as non-numeric entries
    or negative amounts.
    """
    while True:
        amount_input = input("Enter the expense amount: ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    
    category = input("Enter the category for this expense: ")
    description = input("Enter a short description (optional): ")
    
    # Create a dictionary to store expense details
    expense_record = {
        "amount": amount,
        "category": category,
        "description": description
    }
    # Append the dictionary to the global list
    expenses.append(expense_record)
    
    print("Expense added successfully!")

def view_all_expenses():
    """
    Print out all expenses stored in the global 'expenses' list.
    Each expense includes amount, category, and description.
    """
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    
    print("\nAll Recorded Expenses:")
    for i, expense in enumerate(expenses, start=1):
        amount = expense["amount"]
        category = expense["category"]
        description = expense["description"]
        print(f"{i}. Amount: ${amount:.2f}, Category: {category}, Description: {description}")

def view_total_spent():
    """
    Sum the amount of all expenses in the global 'expenses' list
    and display the result to the user.
    """
    if len(expenses) == 0:
        print("No expenses to calculate.")
        return
    
    total = 0
    for expense in expenses:
        total += expense["amount"]
    
    print(f"Total spent so far: ${total:.2f}")

def view_total_spent_by_category():
    """
    Calculate how much is spent per category by iterating
    through all expenses. Display each category and the
    total spent for that category.
    """
    if len(expenses) == 0:
        print("No expenses to summarize.")
        return
    
    category_totals = {}
    
    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += amt
    
    print("\nTotal Spent By Category:")
    for cat, total_amt in category_totals.items():
        print(f"  {cat}: ${total_amt:.2f}")

def main():
    """
    Main function that runs a loop displaying the menu and
    executing the user's choice until they decide to exit.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_total_spent()
        elif choice == "4":
            view_total_spent_by_category()
        elif choice == "5":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid option from the menu.")

# This condition ensures the 'main' function only runs if this script
# is executed directly (rather than imported as a module).
if __name__ == "__main__":
    main()

