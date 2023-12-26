class Complex:
  def __init__(self, r, i):
    self.real = r
    self.imaginary = i

  def __add__(self, other):
    # This is a string
    return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary) + "i"
  # this commented line is for integer, you can uncomment to test and comment the above
   # return f"{self.real + other.real} + {self.imaginary + other.imaginary}i" 
  
c = Complex(2, 3)
d = Complex(3, 4)

print(c + d)