"""Class inheritance for calulation.
class Sum: to find sum.
class Sub: to find the difference.
class Mul: for multiplication. """
class Sum:
  def __init__(self, num1, num2):
    self.__num1 = num1
    self.__num2 = num2

  @property
  def num1(self):
    return self.__num1
  
  @num1.setter
  def num1(self, value):

    if type(value) != int:
       raise TypeError("value must be an integer")
    if value <= 0:
      raise ValueError("value must be > 0")
    self.__num1 = value

  @property
  def num2(self):
    return self.__num2
  
  @num2.setter
  def num1(self, value):

    if type(value) != int:
       raise TypeError("value must be an integer")
    if value <= 0:
      raise ValueError("value must be > 0")
    self.__num2 = value

  def sum(self):
    return self.__num1 + self.__num2

class Sub(Sum):
  def __init__(self, num1, num2):
    self.__num1 = num1
    self.__num2 = num2
    super().__init__(num1, num2)
  def subtract(self):
    return self.__num1 - self.__num2
  
class Mul(Sum):
  def __init__(self, num1, num2):
    self.__num1 = num1
    self.__num2 = num2
    super().__init__(num1, num2)
      
  def multiply(self):
    return self.__num1 * self.__num2
  
if __name__ == "__main__":
  s = Sum(5,3)
  print(f"Sum is {s.sum()}") 
  sub = Sub(7,2)
  print(f"Sub is {sub.subtract()}")
  mul = Mul(4,4)
  print(f"mul is {mul.multiply()}")



    