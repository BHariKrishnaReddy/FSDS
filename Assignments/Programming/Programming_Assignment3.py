# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def checknum(n):
    if n >0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"
    
# 2. Write a Python Program to Check if a Number is Odd or Even?

def evod(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
    
# 3. Write a Python Program to Check Leap Year?

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 4. Write a Python Program to Check Prime Number?

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

def print_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    print(prime_numbers)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print_prime_numbers(1, 10000)
