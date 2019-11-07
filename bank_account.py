

# Bank accounts have a name and a balance
class BankAccount:
    name: str
    balance: int

    def __init__(self, name_of_acct: str, init_balance: int):
        self.name=name_of_acct
        self.balance=init_balance

    def deposit(self, amount: int):
        self.balance+=amount

    def withdraw(self, amount:int):
        if amount>self.balance:
            old_balance=self.balance
            self.balance=0
            return old_balance
        else:
            self.balance-=amount
            return amount

dr_barts_points=BankAccount("UD Points", 100)
ellies_checking=BankAccount("M&T Checking Account",1000000)

dr_barts_points.deposit(200)
print(dr_barts_points.balance)
some_money=dr_barts_points.withdraw(1000)
print("you got", some_money, "dollars")
some_money=dr_barts_points.withdraw(10)
print("you got", some_money, "dollars")
