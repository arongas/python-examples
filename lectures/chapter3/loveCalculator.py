# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name=name1+name2

t=name.lower().count("t")+name.lower().count("r")+name.lower().count("u")+name.lower().count("e")


l=name.lower().count("l")+name.lower().count("o")+name.lower().count("v")+name.lower().count("e")


score=int(str(t)+str(l))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
