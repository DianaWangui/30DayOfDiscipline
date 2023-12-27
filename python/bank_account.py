class BankAccount:
  """Instantiate the holder name and balace to 0"""
  def __init__(self, holder_name, balance=0):
    self.holder_name = holder_name
    self.balance = balance

  #Deposit method stating amount to deposit
  def deposit(self, deposit):
    print(f"Hello {self.holder_name}. Your account balance is {self.balance}")
    self.deposit = deposit
    self.balance += self.deposit
    print(f"You have deposited {self.deposit}.")
    print(f"Your new balance is {self.balance}\n")

  # Withdrawal method stating amount to withdraw, cannot withdraw with less than balance
  def withdraw(self, withdraw):
    print(f"Hello {self.holder_name}")
    self.withdraw = withdraw
    if self.withdraw > self.balance:
      print(f"You do not have enough fund to withdraw {self.withdraw}.")
      print(f"Your balance is {self.balance}\n")
    else:
      self.balance -= self.withdraw
      print(f"You have withdrawn {self.withdraw}.")
      print(f"Your new balance is {self.balance}\n")

  def __str__(self):
    return f"Bank Account of {self.holder_name} with initial balance {self.balance}"

# testing by calling the methods
b = BankAccount("Diana", 200)
b.withdraw(500)
b.deposit(1000)
#printed by calling __str__ inside the class BankAccount
print(b)