class A:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b
  
class B:
  def add(self, a, b):
    return a + b
  pass

a = B()
# Method overriding
print(a.add(3, 4))
