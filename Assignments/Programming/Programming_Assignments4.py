# 1. Write a Python Program to Find the Factorial of a Number?

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# 2. Write a Python Program to Display the multiplication Table?

def multiplication_table(number):
    print("Multiplication table for", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


# 3. Write a Python Program to Print the Fibonacci sequence?

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence


# 4. Write a Python Program to Check Armstrong Number?

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit)**num_digits for digit in num_str)
    if sum_of_digits == num:
        return True
    else:
        return False

# 5. Write a Python Program to Find Armstrong Number in an Interval?

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit)**num_digits for digit in num_str)
    if sum_of_digits == num:
        return True
    else:
        return False

# Function to find Armstrong numbers within a given interval

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


# 6. Write a Python Program to Find the Sum of Natural Numbers?

def sum_of_natural_numbers(limit):
    sum = 0
    for num in range(1, limit + 1):
        sum += num
    return sum

