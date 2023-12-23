class Square:
  def __init__(self, size=0, position=(0,0)):
    self.__size = size
    self.__position = position

  @property
  def size(self):
    return self.__size
  
  @size.setter
  def size(self, value):
    if not isinstance(value, int):
      raise TypeError("Size must be an integer.")
    if value < 0:
      raise ValueError("Size cannot be negative.")
    else:
      self.__size = value


  @property
  def position(self):
    return self.__position
  
  @position.setter
  def position(self, value):
    if  (not isinstance(value, tuple) or
         len(value) != 2 or
         not all(isinstance(num, int) for num in value) or
         not all(num >= 0 for num in value)) :
      raise TypeError("Position must be a tuple of two integers.")
    self.__position = value

    
  def area(self):
    return (self.__size ** 2)
  
  def my_print(self):
    if self.__size == 0:
      print()

    else:
        for i in range(self.__position[1]):
          print()

        for i in range(self.__size):
          print(" " * self.__position[0], end='')
          print("#" * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")