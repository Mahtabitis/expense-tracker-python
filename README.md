# Expense Tracker

A simple expense tracking application built to help users record, organize, and manage their daily expenses.

This project started as a command-line application in Python and is gradually being developed into a web application using Flask. The main goal is to create a simple and user-friendly way to keep track of personal expenses while improving my understanding of Python, web development, backend development, and API design.

## Features

### Current Features

* Add new expenses
* View saved expenses
* Edit existing expenses
* Delete expenses
* Organize expenses by category
* Store expense data using JSON
* Basic input validation
* View expenses by month
* Calculate monthly expenses total

### REST API Endpoints

The project includes basic API endpoints for managing expenses:

| Method | Endpoint                | Description                |
| ------ | ----------------------- | -------------------------- |
| GET    | `/api/expenses`         | Retrieve all expenses      |
| POST   | `/api/expenses`         | Create a new expense       |
| PATCH  | `/api/expenses/<index>` | Update an existing expense |
| DELETE | `/api/expenses/<index>` | Delete an expense          |

The API endpoints were implemented using Flask and tested with Postman.

> **Note:** The current API uses list indexes to identify expenses. JSON is used for data storage instead of a database.

### Web Version

* Flask-based web interface
* User-friendly layout for managing expenses
* HTML/CSS-based interface
* Monthly expense navigation

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JSON
* Postman
* Git & GitHub

## Project Structure

```text
expense-tracker/
│
├── main.py              # Command-line version
├── app.py               # Flask application and API endpoints
├── expenses.json        # Expense data storage
│
├── templates/
│   └── index.html       # Web page template
│
└── static/
    └── style.css        # Styling files
```

## Future Improvements

Some features I plan to add:

* Replace JSON storage with a database
* Add unique IDs for expenses
* Improve API validation and error handling
* Add authentication and authorization
* Improve filtering and searching options
* Add data visualization for spending patterns
* Improve the overall user experience
* Add automated tests for API endpoints

## Motivation

I built this project as a way to practice Python programming and gradually explore web application development and backend development.

While developing it, I am focusing not only on functionality but also on creating a cleaner and more intuitive user experience.

## How to Run

### Run the Command-Line Version

```bash
python main.py
```

### Run the Flask Version

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

### Test the API

You can use Postman to test the API endpoints.

The base API URL is:

```text
http://127.0.0.1:5000/api/expenses
```

## Author

Mahtab Ramezani