# This method overloading is not allowed in python
# I used this just for learning purposes

class Override:
  #avoid overlaoding by using default arguments
  def add(self, a, b, c=0):
    return a + b + c


class Demo:
  # avoid overloading by using *arg to take any args passed
  def sum(self, *args):
    total = 0
    for i in args:
      total = total + i
    return total
  

a = Override()
print(a.add(2, 3))
print(a.add(23,4,2))

s = Demo()
print(s.sum(1,2,3))
print(s.sum(2,3,4,5,2,3,5,4))
