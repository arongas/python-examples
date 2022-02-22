def prime_checker(number):
    flag = False
    for divider in range(2, number):
        if number % divider == 0:
            print("It's not a prime number.")
            flag = True
            break;
    if not flag:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
