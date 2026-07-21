print("=== Expense Tracker ===")

expenses = []

while True:
    print("Menu:")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Choose an option: ")
# used the double quotation for numbers because output of input() is held in a string
    if choice == "1":

        while True:

            name = input("Expense name: ")
            amount = float(input("Amount: "))

            expense = {
                "name": name,
                "amount": amount
            }

            expenses.append(expense)

            print("Expense added successfully!")

            another = input("Would you like to add another expense?").strip().lower()

            if another != "yes" and another != "y":
                break

    elif choice == "2":

        if not expenses:
            print("You have not added any expenses yet.")
        else:
             print("Your expenses:")

             for expense in expenses:
                  print(f"{expense['name']}: ${expense['amount']}")
           
    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total: ${total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")