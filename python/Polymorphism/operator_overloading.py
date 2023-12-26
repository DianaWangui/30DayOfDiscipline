class Complex:
  def __init__(self, r, i):
    self.real = r
    self.imaginary = i

  #using add operator to eliminate overiding
  def __add__(self, other):
    # This is a string
    return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary) + "i"
  # this commented line is for integer, you can uncomment to test and comment the above
   # return f"{self.real + other.real} + {self.imaginary + other.imaginary}i" 

# Creating  a New class to use greator than operator, One can use all other operators with this to learn
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Using gt operator to eliminate overriding 
  def __gt__(self, other):
    if self.age > other.age:
      return True
    else:
      return False

p1 = Person("Diana", 26)
p2 = Person("Daniel", 30)

if p1 > p2:
  print(f"{p1.name} will pay the bill.")

else:
  print(f"{p2.name} will pay the bill.")


c = Complex(2, 3)
d = Complex(3, 4)

print(c + d)