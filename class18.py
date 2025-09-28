"""Value Error
Outline:
Write a program to understand how the value error exception works?"""

"""try:
    number = int(input("Enter a number: "))
    print("The number is entered is", number)

except ValueError as ex:
    print("Exception:", ex)"""

"""try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 / num2 
    print("Result is", result)

except ZeroDivisionError:
    print("Division zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers sperated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")"""

"""Bye Bye
Outline:
Write a program using nested while loop.
If the value is divided by two, then it will run an infinite loop of the bye."""

valid = False
while not valid:
    try:
        n=int(input("Enter a number: "))

        while n%2==0:
            
            print("bye")
        valid = True
    except ValueError:
        print("Invalid")