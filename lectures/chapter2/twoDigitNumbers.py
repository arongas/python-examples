# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
d0d =int(two_digit_number) % 10
d1d = int((int(two_digit_number)- d0d)/10)
dsum=d0d+d1d
print(dsum)

# Alternative
d0d = int(two_digit_number[0])
d1d = int(two_digit_number[1])
dsum=d0d+d1d
print(dsum)