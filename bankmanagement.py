# Base Class
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name                  # Public
        self.__account_number = account_number   # Private (Encapsulation)
        self.__balance = balance          # Private

    # Getter method
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")

    # Display details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")


# Derived Class (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, balance=0, interest_rate=5):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    # Method Overriding
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest} added.")


# Main Program
def main():
    acc1 = SavingsAccount("Zeeshan", 12345, 1000)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Add Interest")
        print("5. Display Details")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount: "))
            acc1.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter amount: "))
            acc1.withdraw(amount)

        elif choice == 3:
            print("Balance:", acc1.get_balance())

        elif choice == 4:
            acc1.add_interest()

        elif choice == 5:
            acc1.display()

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()