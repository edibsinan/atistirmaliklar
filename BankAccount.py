class BankAccount:
    def __init__(self):
        self.__balance=0
    
    def deposit(self, amount):
        self.__balance=self.__balance+amount
        print(self.__balance)
    
    def withdraw(self, amount):
        self.__balance=self.__balance-amount
        print(self.__balance)

hesap=BankAccount()
print(hesap.deposit(200))
print(hesap.withdraw(100))