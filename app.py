from flask import Flask, render_template , request , redirect , url_for
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    month = request.args.get("month", type=int)

    if month is None:
        month = datetime.now().month

    year = datetime.now().year

    monthly_expenses = []

    for index, expense in enumerate(expenses):
        date = datetime.strptime(expense["date"], "%Y-%m-%d")

        if date.month == month and date.year == year:
            monthly_expenses.append({
            "index": index,
            "name": expense["name"],
            "category": expense["category"],
            "amount": expense["amount"],
            "date": expense["date"]
        })

    total = 0
    for expense in monthly_expenses:
        total += expense["amount"]

    month_name = datetime(year, month, 1).strftime("%B")

    previous_month = month - 1
    next_month = month + 1

    if previous_month == 0:
        previous_month = 12

    if next_month == 13:
        next_month = 1

    return render_template("index.html", 
        expenses=monthly_expenses,
        total=total,
        month_name=month_name,
        previous_month=previous_month,
        next_month=next_month 
    )

@app.route("/add", methods=["POST"])
def add_expense():

    name = request.form["name"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    date = request.form["date"]

    new_expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    expenses.append(new_expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return redirect(url_for("home"))

@app.route("/edit/<int:index>", methods=["POST"])
def edit_expense(index):

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    name = request.form["name"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    date = request.form["date"]

    expenses[index] = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return redirect(url_for("home", month=datetime.strptime(date, "%Y-%m-%d").month))

@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if 0 <= index < len(expenses):
        expenses.pop(index)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

    return redirect(url_for("home"))

@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    return expenses

@app.route("/api/expenses", methods=["POST"])
def create_expense():
    data = request.get_json()

    name = data["name"]
    category = data["category"]
    amount = float(data["amount"])
    date = data["date"]

    new_expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    expenses.append(new_expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return new_expense, 201

@app.route("/api/expenses/<int:index>", methods=["PATCH"])
def update_expense(index):
    data = request.get_json()

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if index < 0 or index >= len(expenses):
        return {"error": "Expense not found"}, 404

    expense = expenses[index]

    if "name" in data:
        expense["name"] = data["name"]

    if "category" in data:
        expense["category"] = data["category"]

    if "amount" in data:
        expense["amount"] = float(data["amount"])

    if "date" in data:
        expense["date"] = data["date"]

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return expense, 200

@app.route("/api/expenses/<int:index>", methods=["DELETE"])
def delete_expense_api(index):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if index < 0 or index >= len(expenses):
        return {"error": "Expense not found"}, 404

    deleted_expense = expenses.pop(index)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return {
        "message": "Expense deleted successfully",
        "expense": deleted_expense
    }, 200

if __name__ == "__main__":
    app.run(debug=True)
