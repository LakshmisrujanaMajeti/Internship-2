
import os
import json
import pandas as pd

# File to save expenses
DATA_FILE = "expenses.json"

# Load existing expenses
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file)

# Add an Expense
def add_expense(expenses):
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")

# View Expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    df = pd.DataFrame(expenses)
    print("\nRecorded Expenses:")
    print(df)

# Summarize by Category
def summarize_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    df = pd.DataFrame(expenses)
    summary = df.groupby("category")["amount"].sum()
    print("\nExpense Summary by Category:")
    print(summary)

# Main function
def main():
    print("Welcome to the Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\nChoose an option:")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summarize_by_category(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
