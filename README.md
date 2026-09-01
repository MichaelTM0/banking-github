# Banking Simulator

A beginner-friendly Python command-line banking simulator that allows users to log in, manage checking and savings account balances, make deposits and withdrawals, transfer money between accounts, and view their transaction history.

## Features

* Username and password login authentication
* View checking account balance
* View savings account balance
* Deposit money into checking or savings
* Withdraw money from checking or savings
* Prevent withdrawals when there are insufficient funds
* Transfer money between checking and savings accounts
* Prevent deposits of zero or negative amounts
* Track deposits and withdrawals in transaction history
* View transaction history
* Interactive command-line banking menu

## Banking Menu

The application provides the following options:

1. View Balances
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Exit

## How It Works

When the program starts, the user is prompted to enter their username and password.

If the login credentials are correct, the user gains access to the banking menu.

From the menu, the user can:

* Check their current account balances
* Deposit money into either checking or savings
* Withdraw money from either account
* Transfer money between checking and savings
* Review their transaction history
* Exit the application

The program uses global variables for the checking and savings balances so that the `transfer()` function can update both account balances.

Transaction history is stored in a Python list, with each transaction recorded as a text entry.

## Data Structures Used

* **Variables** — Used to store account balances and login credentials.
* **List** — Used to store transaction history.
* **Functions** — Used to organize banking operations such as transfers.
* **Conditional statements** — Used to validate login credentials, account selections, and available funds.
* **Loops** — Used to keep the banking menu running until the user chooses to exit.

## Technologies Used

* Python 3
* Functions
* Lists
* Variables
* `if` / `elif` / `else` statements
* `while` loops
* `global` variables
* User input and validation
* Formatted strings (f-strings)

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with:

```bash
python banking_simulator.py
```

## Project Status

Version 1.0 — Complete

This project was created as a beginner Python project to practice functions, lists, loops, conditional statements, user input, account balance calculations, and basic authentication logic.

## Future Improvements

Potential improvements for future versions include:

* Store usernames and passwords securely instead of directly in the source code
* Add transaction history for account transfers
* Add protection against negative withdrawal amounts
* Add a maximum withdrawal limit
* Allow users to create multiple accounts
* Store account information in a file or database
* Add persistent data so account balances remain after closing the program
* Improve password security
