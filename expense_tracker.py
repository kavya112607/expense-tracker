import json
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Study/Other): ")
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        "amount": amount,
        "category": category,
        "date": date
    })

    print("✅ Expense added successfully!")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")
        return

    print("\n📊 Your Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} - {exp['date']}")

# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        idx = int(input("Enter expense number to delete: ")) - 1
        expenses.pop(idx)
        print("🗑️ Expense deleted!")
    except:
        print("Invalid input!")

# Show total
def show_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}")

# Main program
expenses = load_expenses()

while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Spending")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        delete_expense(expenses)
    elif choice == "4":
        show_total(expenses)
    elif choice == "5":
        save_expenses(expenses)
        print("Exiting... Data saved!")
        break

    save_expenses(expenses)
