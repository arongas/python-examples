# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4==0:
    if year%100==0:
        if year%400==0:
            isleap=True
        else:
            isleap=False
    else:
        isleap=True
else:
    isleap=False

if isleap:
    print("Leap year.")
else:
    print("Not leap year.")



