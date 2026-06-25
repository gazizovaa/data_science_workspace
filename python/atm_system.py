# balance, password

class ATM():
    def __init__(self, balance, password):
        self.balance = balance
        self.password = password
        self.attempts = 0
        self.max_attempts = 3

    # check the validation of the password 
    def validate(self):
        while self.attempts < self.max_attempts:
            get_user_password = input('Enter your password: ')
            if get_user_password == self.password:
                return 'Your password is correct!'
            else:
                self.attempts += 1 
                return f'Your password is incorrect! You have {self.max_attempts - self.attempts} attempts left.'

    def display_operation(self):
        print("\nATM operation:")
        print("1. Display balance")
        print("2. Withdraw money")
        print("3. Stop opeeration")

    def show_balance(self):
        print(f"Your balance is {self.balance} AZN.")

    def withdraw(self):
        try:
            amount = float(input("Note the money you want extract: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} AZN extracted! You have {self.balance} AZN")
            else:
                print("There is no enough money in your balance.")
        except ValueError:
            print("Mark the correct operation.")

    def start(self):
        if not self.validate_password():
            return  # stop the ATM operation 
        while True:
            self.display_menu()
            choice = input("Select operations - 1, 2, 3: ")
            if choice == "1":
                self.show_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                print("The operation is stopped!")
                break
            else:
                print("Mark the correct operation!")

my_atm = ATM(balance=2000, password='Az@1345')
my_atm.start()