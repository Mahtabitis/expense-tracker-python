# Expense Tracker

A simple expense tracking application built to help users record, organize, and manage their daily expenses.

This project started as a command-line application in Python and is gradually being developed into a web application using Flask. The main goal is to create a simple and user-friendly way to keep track of personal expenses while improving my understanding of Python, web development, and user interface design.

## Features

### Current Features

* Add new expenses
* View saved expenses
* Edit existing expenses
* Delete expenses
* Organize expenses by category
* Store expense data using JSON
* Basic input validation

### Web Version (In Progress)

* Flask-based web interface
* User-friendly layout for managing expenses
* HTML/CSS based interface

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JSON

## Project Structure

```
expense-tracker/
│
├── main.py              # Command-line version
├── app.py               # Flask application
├── expenses.json        # Expense data storage
│
├── templates/
│   └── index.html       # Web page templates
│
└── static/
    └── style.css        # Styling files
```

## Future Improvements

Some features I plan to add:

* Connect the application to a database
* Add monthly expense tracking
* Improve filtering and searching options
* Add data visualization for spending patterns
* Improve the overall user experience

## Motivation

I built this project as a way to practice Python programming and gradually explore web application development. While developing it, I am focusing not only on functionality but also on creating a cleaner and more intuitive experience for users.

## How to Run

### Run the Command-Line Version

```
python main.py
```

### Run the Flask Version

Install Flask:

```
pip install flask
```

Run the application:

```
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

## Author

Mahtab Ramezani
