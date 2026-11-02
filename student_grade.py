print("------Welcome In The student Grade Checker-------")

while True:
 student_name = input("Please Enter Your Name : ")

 print("-----Enter Marks (Out Of 100)-----")
 English = float(input("Enter English Marks : "))
 Math = float(input("Enter Math Marks : "))
 urdu = float(input("Enter Urdu Marks : "))
 Science = float(input("Enter Science Marks : "))
 total_marks = 400
 obtained_marks = English + urdu + Math + Science

 percentage = (obtained_marks / total_marks) * 100

 if percentage >= 40:
    status = "PASS"
 else:
    status = "FAIL"


 if percentage >= 80:
    grade = "A+"
 elif percentage >= 70:
    grade = "A"
 elif percentage >= 60:
    grade = "B"
 elif percentage >= 50:
    grade = "C"
 elif percentage >= 40:
    grade = "D"
 else:
    grade = "F"


 print("\n" + "="*30)
 print(f"   STUDENT REPORT CARD")
 print("="*30)
 print(f"Name           : {student_name}")
 print(f"Total Marks    : {obtained_marks} / {total_marks}")
 print(f"Percentage     : {percentage}")
 print(f"Status         : {status}")
 print(f"Grade          : {grade}")