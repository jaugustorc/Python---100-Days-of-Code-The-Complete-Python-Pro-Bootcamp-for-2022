student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for studant in student_scores:
    score=student_scores[studant]

    if score>90:
        student_grades[studant]="Outstanding"
    elif score>80:
        student_grades[studant]= "Exceeds Expectations"
    elif score>70:
        student_grades[studant]="Acceptable"
    else:
        student_grades[studant]="Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)