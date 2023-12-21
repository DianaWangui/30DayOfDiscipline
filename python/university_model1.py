class University:
  def __init__(self, uni_name):
    self._uni_name = uni_name

  def get_uni_name(self):
    return self._uni_name


class Branch(University):
  def __init__(self, uni_name, branch_name):
    University.__init__(self, uni_name)
    self._branch_name = branch_name

  def get_branch_name(self):
    return self._branch_name
  

class Faculty(Branch):
  def __init__(self, uni_name, branch_name, faculty_name):
    Branch.__init__(self, uni_name, branch_name)
    self._faculty_name = faculty_name

  def get_faculty_name(self):
    return self._faculty_name
  

class Course(Faculty):
  def __init__(self, uni_name, faculty_name, branch_name, course_name):
    Faculty.__init__(self, uni_name, branch_name, faculty_name)
    self._course_name = course_name

  def get_course_name(self):
    return self._course_name
  

class Student(Course):
  def __init__(self, uni_name, faculty_name, branch_name, course_name, student_id, student_name):
    Course.__init__(self, uni_name, faculty_name, branch_name, course_name)
    self._student_id = student_id
    self._student_name = student_name

  def display_student_id(self):
    print(f"University: {self._uni_name}\nFaculty: {self._faculty_name}\nBranch: {self._branch_name}\nCourse: {self._course_name}\nStudent Id: {self._student_id}\nStudent Name: {self._student_name}")
  
# Testing  
student = Student("Mount Kenya University", "Computer Informatics", "Mombasa", "Computer Science", 123456, "Diana Wangui")
student.display_student_id()