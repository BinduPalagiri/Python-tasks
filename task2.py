import os  # Add this line to import the os module
import json
from collections import defaultdict

# Function to load data from file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': []}

# Function to save data to file
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Function to save data to a text file
def save_data_to_text(data, filename):
    with open(filename, 'w') as file:
        file.write(f"Income: {data['income']}\n")
        file.write("Expenses:\n")
        for expense in data['expenses']:
            file.write(f"Category: {expense['category']}, Amount: {expense['amount']}\n")
    print("Data saved successfully.")

# Function to record income
def record_income(data):
    amount = float(input("Enter income amount: "))
    data['income'] += amount
    print("Income recorded successfully!")

# Function to record expense
def record_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print("Expense recorded successfully!")

# Function to calculate remaining budget
def calculate_budget(data):
    expenses_total = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - expenses_total
    return remaining_budget

# Function to analyze expenses
def analyze_expenses(data):
    expense_categories = defaultdict(float)
    for expense in data['expenses']:
        expense_categories[expense['category']] += expense['amount']
    for category, amount in expense_categories.items():
        print(f"{category}: {amount:.2f}")

# Main function
def main():
    filename = 'budget_data.txt'
    if os.path.exists(filename):
        data = load_data(filename)
    else:
        data = {'income': 0, 'expenses': []}

    while True:
        print("\n1. Record Income")
        print("2. Record Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            record_income(data)
        elif choice == '2':
            record_expense(data)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"Remaining Budget: {remaining_budget:.2f}")
        elif choice == '4':
            analyze_expenses(data)
        elif choice == '5':
            save_data_to_text(data, filename)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
