class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        self.x = int(input("put: "))
        self.balance += self.x
        return self.balance

    def withdraw(self):
        self.y = int(input("withdraw: "))
        if(self.balance > self.y):
            self.balance -= self.y
            return self.balance
        else:
            print("low balance")

person1 = Account("Aigerim", 100000)
print(person1.deposit())
print(person1.withdraw())

person2 = Account("Sanzhar", 70000)
print(person2.deposit())
print(person2.withdraw())