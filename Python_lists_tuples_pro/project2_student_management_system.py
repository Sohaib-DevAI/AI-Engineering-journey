#PROJECT STUDENT MANAGEMENT SYSTEM
print("_" * 50)
print("STUDENT MANAGEMENT SYSTEM")
print("_" * 50)

#Student personal information
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
roll_number = int(input("Enter student roll number: "))
class_name = input("Enter student class: ")

#Subject marks (out of 100)
print("\nEnter marks for the following subjects (out of 100):")
mathematics_marks = int(input("Mathematics: "))
science_marks = int(input("Science: "))
english_marks = int(input("English: "))
history_marks = int(input("History: "))

#Attendance Tracking
total_days = 100
days_attended = int(input(f"\nEnter number of days attended(out of {total_days}): "))
attendance_percentage = (days_attended / total_days) * 100

#Total marks and percentage calculation
total_marks = mathematics_marks + science_marks + english_marks + history_marks
average_percentage = total_marks / 4

#Grade calculation based on average percentage
if average_percentage >= 90:
    grade = 'A'
    remarks = "Excellent performance! Keep it up!"
elif average_percentage >= 80:
    grade = 'B'
    remarks = "Good job! You can do even better!"
elif average_percentage >= 70:
    grade = 'C'
    remarks = "Fair performance. Focus on improving your weak areas."
elif average_percentage >= 60:
    grade = 'D'
    remarks = "Needs improvement. Consider seeking help in difficult subjects."
else:
    grade = 'F'
    remarks = "Failed. Please work harder and seek additional support."
    
#Attendance Status
if attendance_percentage >= 75:
    attendance_status = "Satisfactory"
else:
    attendance_status = "Unsatisfactory"

#Report card generation
print("\n" + "_" * 50)
print(f"{'STUDENT OFFICIAL PROGRESS REPORT' :^50}")
print("_" * 50)
print(f"Name: {student_name:<20} Roll Number: {roll_number}")
print(f"Age: {student_age:<21} Class: {class_name}")
print("_" * 50)
print(f"{'Subject' :<25}| {'Marks Obtained' :<15}")
print(f"{'Mathematics' :<25}| {mathematics_marks:<15}")
print(f"{'Science' :<25}| {science_marks:<15}")
print(f"{'English' :<25}| {english_marks:<15}")
print(f"{'History' :<25}| {history_marks:<15}")
print("_" * 50)
print(f"Total Marks: {total_marks}/400 | Average Percentage: {average_percentage:.2f}%")
print(f"Final Grade: {grade}")
print(f"Attendance: {attendance_percentage:.2f}% | Status: {attendance_status}")
print(f"Remarks: {remarks}")
print("_" * 50)
print(f"{'AI ENGINEER: SOHAIB KHAN PROTAL' :^50}")
print("_" * 50)    