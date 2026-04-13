# GRADE CHECK FOR PROJECT 3
def grade_check():
    print("Welcome to the Grade Check for Project 3!")


student_Mark = int(input("Enter your mark for one subject:"))
if student_Mark >= 90:
    print("Outstanding grade A+")
elif student_Mark >= 80:
    print("Excellent grade A")
elif student_Mark >= 70:
    print("Good grade B")
elif student_Mark >= 60:
    print("Satisfactory grade C")
else:
    print("Keep trying! Failed grade D")

grade_check() 