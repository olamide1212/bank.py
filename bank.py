class Account():
    def __init__(self, num):
        self.accno=num
        self.balance=0
        
    def deposit(self):
        amount=float(input("enter deposit amount"))
        self.balance+amount
        print("you have deposit $.",amount)
        
    def withdraw(self):
        amount=float(input("enter withdrawal amount"))
        if self.balance<amount:
            amount=self.balance
        self.balance-=self.accno
        print("you have withdraw $.",amount)
        
    def check_balance(self):
        print("current balance is $.",self.balance)
        
acc1=Account(100)
print(acc1.accno)
acc1.deposit()
acc1.withdraw()
acc1.check_balance()