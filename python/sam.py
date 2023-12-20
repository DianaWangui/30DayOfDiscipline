class University:
    def __init__(self, uni_name, branch, faculty):
        self.uniname = uni_name
        self.branch = branch
        self.faculty = faculty

    @property
    def uni_name(self):
        return self.uniname

    @uni_name.setter
    def uni_name(self, name):
        self.uniname = name

    @property
    def branch_name(self):
        return self.branch

    @branch_name.setter
    def branch_name(self, branch):
        self.branch = branch

    def university_name(self):
        print(f"Your university name is {self.uniname}")

    def branch_name(self):
        print(f"Your branch is {self.branch}")

    def faculty_name(self):
        print(f"Your faculty is {self.faculty}")


class Courses(University):
    def __init__(self, c_name, uni_name, branch, faculty):
        self.__cname = c_name
        super().__init__(uni_name, branch, faculty)

    def course_name(self):
        print(f"Your course is {self.__cname}")


class Branch(University):
    def __init__(self, b_name, uni_name, branch, faculty):
        self.__bname = b_name
        super().__init__(uni_name, branch, faculty)

    def branch_name(self):
        print(f"Your branch name is {self.__bname}")


class Student(Branch, Courses):
    def __init__(self, s_name, reg_no, c_name, uni_name, branch, faculty):
        self.__sname = s_name
        self.__reg = reg_no
        Branch.__init__(self, branch, uni_name, branch, faculty, faculty)
        Courses.__init__(self, c_name, uni_name, branch, faculty, faculty)

    def student_name(self):
        print(f"Your name is {self.__sname}")

    def reg_number(self):
        print(f"Your registration no is {self.__reg}")


class Faculty(Branch):
    def __init__(self, f_name, b_name, uni_name, branch, faculty):
        self.__fname = f_name
        super().__init__(b_name, uni_name, branch, faculty)

    def faculty_name(self):
        print(f"Your faculty is {self.__fname}")


# Example usage
student = Student("Diana", 234, "Cs", "MKU", "Mombasa")
student.university_name()
student.branch_name()
student.faculty_name()
student.course_name()
student.student_name()
student.reg_number()
