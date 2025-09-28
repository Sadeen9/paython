class Student:
    """Represents a student with ID and grades"""
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    def gpa(self):
        return round(sum(self.grades)/len(self.grades),2)