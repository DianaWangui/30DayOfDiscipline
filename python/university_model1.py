class University:
  def __init__(self, uni_name):
    self._uni_name = uni_name

  def get_uni_name(self):
    return self._uni_name


class Branch(University):
  def __init__(self, uni_name, branch_name):
    super().__init__(uni_name)
    self._branch = branch_name

  def get_branch_name(self):
    return self._branch
  

class Faculty(Branch):
  def __init__(self, branch_name, faculty_name):
    Branch.__init__(branch_name)
    self._faculty_name = faculty_name

  def get_faculty_name(self):
    return self._faculty_name
  

class Course(Faculty):
  def __init__(self, uni_name, faculty_name, branch_name, course_name):
    Faculty.__init__(uni_name, faculty_name, branch_name)
    self._course_name = course_name

  def get_course_name(self):
    return self._course_name
  

class Student(Course):
  def __init__(self, uni_name, faculty_name, branch_name, course_name, student_id, student_name):
    Course.__init__(uni_name, faculty_name, branch_name, course_name)
    self._student_id = student_id
    self._student_name = student_name

  def display_student_info(self):
    return self.display_student_name() + " " + str(self.display_student_id())
  
# Testing  
student = Student("MKU", "IT", "Mombasa", "CS", "123", "Diana")
print(student.display_student_info)