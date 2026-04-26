class ATM:
    def __init__(self, user_name, pin, balance=0):
        self.user_name = user_name
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")


def main():
    # Create a sample account
    atm = ATM("User1", 2007, 5000)

    print("=== Welcome to ATM ===")
    entered_pin = int(input("Enter your PIN: "))

    if not atm.check_pin(entered_pin):
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

#SIDHANT CODE