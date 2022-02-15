# sumOfNumbers:int=0
# for i in range(1,101):
#     if i%2==0:
#         sumOfNumbers+=i
# print(sumOfNumbers)

sumOfNumbers: int = 0
for i in range(2, 101, 2):
    sumOfNumbers += i
print(sumOfNumbers)
