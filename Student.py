class StudentClass:
    def __init__(self, name, major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def is_on_honor_roll(self):
        if self.gpa>=3.0:
            return True
        else:
            return False

    def student_info(self):
        info = print("Student name: %s\n major: %s\n gpa: %s\n"%(self.name, self.major, self.gpa))
        return info

