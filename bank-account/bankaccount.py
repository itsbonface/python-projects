import random, json

filename = "accounts.json"
accounts = dict()
with open(filename) as read_json:
    accounts = json.load(read_json)

class PersonalBankAccount(object):

    def __init__(self, name, idno, balance=0):
        self.name = name
        self.balance = balance
        self.idno = idno
        self.account = None

    @staticmethod
    def get_random_account():
        number = random.randint(1e9, 1e10-1)
        return number

    def create_account_number(self):
        self.account = str(self.get_random_account())
        for key, value in accounts.items():
            if value == self.idno:
                self.account = key
                return self.account
        if self.account not in accounts:
            accounts.update({self.account : self.idno})
            with open(filename, "w") as write_json:
                json.dump(accounts, 
                    write_json, 
                    indent=4, 
                    separators=(',',' : ')
                )
            return self.account

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insafficient Balance')
        else:
            self.balance -= amount
    
    def account_balance(self):
        return self.balance

    def account_description(self):
        return f"Account Information:\n\
        Acc. Name:      {self.name}\n\
        ID Number:      {self.idno}\n\
        Acc. number:    {self.account}\n\
        Acc. Balance:   {self.balance} KSh\n"
    
    #More methods goes here

