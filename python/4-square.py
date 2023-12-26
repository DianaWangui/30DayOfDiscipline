"""
a square class that defines a square
And a Public instance method: def area(self):
that returns the current square area
Methods Getter and Setter properties for size.
property def size(self): to retrieve it
property setter def size(self, value): to set it:
"""


class Square:
    """
    instantiation of the attributes of the methods
    Raising errors if coditons are not met
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
