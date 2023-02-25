# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
average=round(sum(student_heights)//len(student_heights))


total=0
students=0
for height in student_heights:
  total+=height
  students+=1

average=round(total/students)

print(average)