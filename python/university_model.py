"""This is a university model using hybrid inheritance
It contains 5 classes that inherits from each other
starting from the university class"""

class University:
  """Instantiating the university attributes"""
  def __init__(self, uni_name):
    self._uni_name = uni_name

  @property
  def uni_name(self):
    """Uni name getter"""
    return self._uni_name
  
  @uni_name.setter
  def uni_name(self, name):
    """Uni name setter"""
    self._uni_name = name
  
  def university_name(self):
    """Method to prints university name."""
    print(f"Your university name is {self._uni_name}")

"""A class with all courses inheriting University class."""
class Course(University):
  def __init__(self, c_name, uni_name):
    self._c_name = c_name

    super().__init__(uni_name)

  def course_name(self):
    print(f"Your course is {self._c_name} and University {self.uni_name}")

"""A class that prints the univeruty branch""" 
class Branch(University):
  def __init__(self, b_name, uni_name):
    self._branch_name = b_name
    super().__init__(uni_name)

  def branch_name(self):
    print(f"Your branch name is {self._branch_name} and university is {self.uni_name}")


class Student(Branch, Course):
  def __init__(self, s_name, reg_no, b_name, uni_name):
    self._sname = s_name
    self._reg = reg_no
    super().__init__(b_name, uni_name)

  def student_details(self):
    print(f"Name: {self._sname}, Reg_no: {self._reg}")
