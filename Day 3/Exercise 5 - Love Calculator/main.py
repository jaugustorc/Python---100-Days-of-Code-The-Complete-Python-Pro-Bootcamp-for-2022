# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string=name1+name2
combined_string=combined_string.lower()

t=combined_string.count("t")
r=combined_string.count("r")
u=combined_string.count("u")
e=combined_string.count("e")
true=t+r+u+e

l=combined_string.count("l")
o=combined_string.count("o")
v=combined_string.count("v")
e=combined_string.count("e")

love=l+o+v+e
love_score=str(true)+str(love)
love_score=int(love_score)

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
