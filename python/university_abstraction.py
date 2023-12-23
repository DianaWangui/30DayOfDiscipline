"""A class with all courses inheriting University class."""
from main_abs import University

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
    self._student_name = student_name
    self._reg_no = reg_no
    
  def student_details(self):
    print(f"University: {self.get_uni_name()}\nCourse: {self.get_course_name()}\nBranch: {self.get_branch_name()}\nName: {self._student_name}\nReg_no: {self._reg_no}")


Std = Student("MKU", "CS", "Mombasa", "Diana", 123)
Std.student_details()