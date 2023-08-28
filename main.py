class GradeReport:
    def __init__(self,bangla_marks,english_marks,math_marks,science_marks):
        self.bangla_marks = bangla_marks
        self.english_marks = english_marks
        self.math_marks = math_marks
        self.science_marks = science_marks
    
    def getGrade(self):
        avg = (self.bangla_marks+self.english_marks+self.math_marks+self.science_marks)/4
        avg = round(avg)
        if avg>0 and avg <=40:
            return "F"
        elif avg>40 and avg <=60:
            return "D"
        elif avg>60 and avg <=70:
            return "C"
        elif avg>70 and avg <=80:
            return "B"
        elif avg>80 and avg <=90:
            return "A"
        elif avg>90 and avg <=100:
            return "A+"


gradeReport = GradeReport(
    int(input("Enter Marks of bangla:")),
    int(input("Enter Marks of english:")),
    int(input("Enter Marks of maths:")),
    int(input("Enter Marks of science:")),
)

print("Student grade {}".format(gradeReport.getGrade()))