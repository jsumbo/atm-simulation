# ATM Simulation in Python

This repository contains a simple console-based application simulating an Automated Teller Machine (ATM). The program is written in Python and is designed to illustrate basic concepts such as class-based object-oriented programming and user interaction.

## Features

The program simulates the following ATM operations:
1. PIN Verification: It asks for a PIN and validates it. The correct PIN is '1234'.
2. Balance Checking: It allows the user to check the current balance.
3. Deposit: It allows the user to deposit an amount, which is added to the current balance.
4. Withdrawal: It allows the user to withdraw an amount. If the requested amount is greater than the current balance, the withdrawal is denied.
5. Transaction Continuation: After each operation, it asks the user if they wish to perform another transaction.

## How to Run the Program

To run the ATM simulation program, follow these steps:

1. Clone the repository to your local machine using `git clone`.
2. Navigate into the cloned repository using the command line.
3. Run the program using Python by typing `python atm_simulation.py` and hitting enter. Please note that your command to run the script may vary depending on your Python installation (e.g., you may need to use `python3` instead of `python`).

Remember, this is a console-based application. You will interact with it using the command line of your system. 

## Disclaimer

This is a simple program designed for educational purposes and does not contain all the features of a real ATM. For instance, it does not include features like PIN change, transfer of funds, or multiple account handling. Use it as a starting point to build more complex applications.
