# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
cnt=0
sumOfHeight=0
for height in student_heights:
    cnt+=1
    sumOfHeight+=height

print(round(sumOfHeight / cnt))
# print(round(sum(student_heights) / len(student_heights)))

