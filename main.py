expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))

def show_expenses():
    total = 0
    for name, amount in expenses:
        print(f"{name}: ₹{amount}")
        total += amount
    print("Total Expense: ₹", total)

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
