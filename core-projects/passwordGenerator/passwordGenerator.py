#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)
for index in range(0, nr_letters):
    password += letters[random.randint(0, letters_length)]

for index in range(0,nr_symbols):
    password += symbols[random.randint(0, symbols_length)]

for index in range(0, nr_numbers):
    password += numbers[random.randint(0, numbers_length)]

print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
remaining_numbers = nr_numbers
remaining_letters = nr_letters
remaining_symbols = nr_symbols
password = ''
letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)
for index in range(0, nr_numbers + nr_letters + nr_symbols):
    bag = []
    if remaining_letters > 0:
        bag.append(0)
    if remaining_numbers > 0:
        bag.append(1)
    if remaining_symbols > 0:
        bag.append(2)

    pickWhatToAdd = bag[random.randint(0,len(bag)-1)]
    if pickWhatToAdd == 0:
        password += letters[random.randint(0, letters_length)]
        remaining_letters -= 1
    elif pickWhatToAdd == 1:
        password += numbers[random.randint(0, numbers_length)]
        remaining_numbers -= 1
    else:
        password += symbols[random.randint(0, symbols_length)]
        remaining_symbols -= 1

print(password)
