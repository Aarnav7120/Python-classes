"""Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print
 out the total amount paid at a restaurant. Given a bill amount and the percentage 
 of the bill amount you decide to pay us a tip (tip_perc ), this function
calculates the total amount you should pay."""

"""def total_calc(bill_amount,tip_perc):

    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")

total_calc(5000,10)"""

"""Cube of the cube
Outline:
Define a function to find a cube and define another function which le
 execute the cube function if the number is divisible by 3"""

"""def cube(number):
    return number*number*number

def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
    
print(by_three(9))
print(by_three(5))"""

"""Factorial
Outline:
Write a program to find the factorial using recursive function"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negativ numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
6