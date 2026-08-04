from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)