class University:
    def __init__(self, uni_name):
        self._uni_name = uni_name


class Course:
    def __init__(self, uni, c_name):
        self._uni = uni
        self._c_name = c_name


class Branch:
    def __init__(self, uni, branch_name):
        self._uni = uni
        self._branch_name = branch_name


class Student:
    def __init__(self, uni_name, c_name, branch_name, s_name, reg_no):
        self._uni = University(uni_name)
        self._course = Course(self._uni, c_name)
        self._branch = Branch(self._uni, branch_name)
        self._sname = s_name
        self._reg = reg_no

    def student_details(self):
        print(f"Name: {self._sname}, Reg_no: {self._reg}, Branch: {self._branch._branch_name}, Course: {self._course._c_name}")


# Instantiate Student
student = Student("MKU", "CS", "Mombasa", "Diana", 123)

# Access student details
student.student_details()
