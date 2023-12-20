"""This is a university model using hybrid inheritance
It contains 5 classes that inherits from each other
starting from the university class"""

class University:
  """Instantiating the university attributes"""
  def __init__(self, uni_name):
    self._uni_name = uni_name


"""A class with all courses inheriting University class."""
class Course(University):
  def __init__(self, uni_name, course_name):
    super().__init__(uni_name)
    self._course_name = course_name


"""A class that prints the univeruty branch""" 
class Branch(University):
  def __init__(self, uni_name, branch_name):
    super().__init__(uni_name)
    self._branch_name = branch_name


class Student(Branch, Course):
  def __init__(self,uni_name, course_name, student_name, reg_no,):
    super().__init__(uni_name, course_name)
    self._studentname = student_name
    self._reg = reg_no

  def student_details(self):
    print(f"Name: {self._studentname}, Reg_no: {self._reg}")

Std = Student("CS", "Mombasa", "Diana",123 )
print(Student.__mro__)
