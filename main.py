class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance


def main():
    my_atm = ATM('1234', 1000)  # Creating a new ATM with PIN '1234' and balance 1000.

    print("Welcome to our ATM! Please note that the correct PIN is '1234'. Any other PIN will be invalid.")
    pin = input("Enter your PIN: ")
    if my_atm.check_pin(pin):
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input()

            if choice == '1':
                print("Your balance is $", my_atm.get_balance())
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                print("Your new balance is $", my_atm.deposit(amount))
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                print("Your new balance is $", my_atm.withdraw(amount))
            elif choice == '4':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            print("\nWould you like to perform another transaction?")
            print("1. Yes")
            print("2. No")
            transaction_choice = input()

            if transaction_choice == '2':
                print("Thank you for using our ATM. Goodbye!")
                break
    else:
        print("Invalid PIN. Please try again.")


if __name__ == "__main__":
    main()

