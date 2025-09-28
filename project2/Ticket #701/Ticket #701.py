class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    def gpa(self, scale=4.0):
        raw = sum(self.grades)/len(self.grades)
        return round((raw/100)*scale, 2)