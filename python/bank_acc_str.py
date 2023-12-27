class BankAccount:
  def __init__(self, holder_name, balance=0):
    self.holder_name = holder_name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"You have deposited {amount} to your account.")

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"You have withdrawn {amount} from your account.")
    else:
      print(f"Insufficient funds your balance is {self.balance}")

  def __str__(self):
    return f"Bank Account of {self.holder_name} with initial balance {self.balance}\n"

# testing our methods 
obj = BankAccount("Diana", 200)
print(obj)
obj.deposit(500)
obj.withdraw(1000)
print(obj)