# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/height**2)

if bmi<18.5:
    type = "are underweight"
elif bmi<25:
    type = "have a normal weight"
elif bmi<30:
    type = "are slightly overweight"
elif bmi<35:
    type = "are obese"
else:
    type = "are clinically obese"

print(f"Your BMI is {bmi}, you {type}.")