import bankaccount
from bankaccount import *

if __name__ == "__main__":
    client = PersonalBankAccount('Orman', 58923961)
    client.deposit(90550)
    client.account_balance()
    client.create_account_number()
    
    print(client.account_description())
    print(accounts.values())