from flask import Flask, render_template , request , redirect , url_for
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    total = 0
    for expense in expenses:
        total += expense["amount"]

    return render_template("index.html", expenses=expenses, total=total)

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

    return redirect(url_for("home"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if 0 <= index < len(expenses):
        expenses.pop(index)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
