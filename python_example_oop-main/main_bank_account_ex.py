from bank_account_class import BankAccount 

# Here ist the example

jonys_balance = 0

def deposit(amount):
    global jonys_balance
    if amount > 0:
        jonys_balance += amount

def withdraw(amount):
    global jonys_balance
    if amount > 0 and jonys_balance >= amount:
        jonys_balance -= amount


# With class
jonys_bank = BankAccount()
jonys_bank.deposit(100)
print(jonys_bank.balance)

deposit(100)
print(jonys_balance)


# Adding new person is difficult!

peters_bank = BankAccount()

