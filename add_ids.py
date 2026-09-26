import json
with open("expenses.json", "r") as file:
    expenses = json.load(file)

for index, expense in enumerate(expenses, start=1):
    expense["id"] = index

with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)