# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#metodo 1
max_s=0
for student in student_scores:
    if max_s<student:
        max_s=student
#print(f"The highest score in the class is: {max_s}")

#metodo 2
print(f"The highest score in the class is: {max(student_scores)}")