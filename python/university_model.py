"""This is a university model using hybrid inheritance
It contains 5 classes that inherits from each other
starting from the university class"""

class University:
  """Instantiating the university attributes"""
  def __init__(self, uni_name):
    self._uni_name = uni_name

  def get_uni_name(self):
    return self._uni_name


"""A class with all courses inheriting University class."""
class Course(University):
  def __init__(self, uni_name, course_name):
    University.__init__(self, uni_name)
    self._course_name = course_name

  def get_course_name(self):
    return self._course_name


"""A class that prints the university branch name
inheriting from University name""" 
class Branch(University):
  def __init__(self, uni_name, branch_name):
    University.__init__(self, uni_name)
    self._branch_name = branch_name

  def get_branch_name(self):
    return self._branch_name
  
class Student(Course, Branch):
  def __init__(self,uni_name, course_name, branch_name,student_name, reg_no):

    Course.__init__(self, uni_name, course_name)
    Branch.__init__(self, uni_name, branch_name)
    self._studentname = student_name
    self._reg = reg_no
    
  def student_details(self):
    print(f"University: {self._uni_name}\nCourse: {self._course_name}\nBranch: {self._branch_name}\nName: {self._studentname}\nReg_no: {self._reg}")

Std = Student("MKU", "CS", "Mombasa", "Diana", 123)
Std.student_details()