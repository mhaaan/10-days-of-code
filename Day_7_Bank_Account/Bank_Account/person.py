from random import randint

class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):
    def __init__(self, first_name, last_name, account_num, balance) -> None:
        super().__init__(first_name, last_name)
        self.account_number = account_num
        self.balance = balance

    def __str__(self):
        return f"First Name: {self.first_name} Last Name: {self.last_name} Account Number: {self.account_number} Balance: {self.balance}"

    def deposit(self, deposit):
        self.balance = self.balance +  deposit

    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw


def create_client():
    fname = input("Please enter your first name?")
    lname = input("Please enter your last name?")
    account_number = randint(10000000, 99999999)
    client = Customer(fname, lname, account_number, 0)
    return client

def main():
    client = create_client()
    service = 0
    print(client)
    while service != "E":
        print("Deposit: D     Withdraw: W     Balance: B     End: E")
        service = input()
        if service == 'D':
            dep_amount = int(input("Deposit amount: "))
            client.deposit(dep_amount)
        elif service == 'W':
            with_amount = int(input("Withdraw amount"))
            client.withdraw(with_amount)
        print(client)
            
    
    print("Goodbye")


main()
