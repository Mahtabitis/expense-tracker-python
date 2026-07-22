from datetime import datetime
import json

def load_expenses():
     
     try: 
  
      with open("expenses.json", "r") as file:
           return json.load(file)
           
     except FileNotFoundError:
      expenses = load_expenses()

     with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def save_expenses():

    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def get_amount():

    while True:

        try:
            amount = float(input("Amount: "))
            return amount

        except ValueError:
            print("Please enter a valid number.")

def add_expense() :
 
        while True:

            name = input("Expense name: ")
            category = input("Category: ")
            amount = get_amount()

            date = datetime.today().strftime("%Y-%m-%d")

            expense = {
                "name": name,
                "category": category,
                "amount": amount,
                "date": date
            }

            expenses.append(expense)

            save_expenses()

            print("Expense added successfully!")

            another = input("Would you like to add another expense?").strip().lower()

            if another != "yes" and another != "y":
                break

def view_expenses():

    if not expenses:
            print("You have not added any expenses yet.")
    else:
             print("Your expenses:")

             for expense in expenses:
                  print(f"{expense['date']} | {expense['name']} | {expense.get('category' , 'unknown')} | ${expense['amount']}")

def calculate_total():
     
     total = 0

     for expense in expenses:
        total += expense["amount"]

     print(f"Total: ${total}")



expenses = load_expenses()

while True: 

    print("=== Expense Tracker ===")
    print("Menu:")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        add_expense()

    elif choice == "2":
        
        view_expenses()

        
    elif choice == "3":

        calculate_total()
       

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")