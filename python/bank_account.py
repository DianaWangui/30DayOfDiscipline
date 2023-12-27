class Bank:
  """Instantiate the holder name and balace to 0"""
  def __init__(self, holder_name, balance=0):
    self.holder_name = holder_name
    self.balance = balance

  #Deposit method stating amount to deposit
  def deposit(self, deposit):
    print(f"Hello {self.holder_name}. Your account balance is {self.balance}")
    self.deposit = deposit
    self.balance += self.deposit
    print(f"You have deposited {self.deposit}. Your new balance is {self.balance}\n")

  # Withdrawal method stating amount to withdraw, cannot withdraw with less than balance
  def withdraw(self, withdraw):
    print(f"Hello {self.holder_name}")
    self.withdraw = withdraw
    if self.withdraw > self.balance:
      print(f"You do not have enough fund to withdraw {self.withdraw}. Your balance is {self.balance}\n")
    else:
      self.balance -= self.withdraw
      print(f"You have withdrawn {self.withdraw}. Your new balance is {self.balance}\n")

# testing by calling the methods
b = Bank("Diana", 200)
b.withdraw(500)
b.deposit(1000)
b.balance