"""AND-OR operator
Outline:
Write a program to check whether the given values have boolean values or not."""

"""a=10
b=15
c=0

if a or b or c:
    print("all the numbers are boolean values") 
else:
    print("at least 1 number has a boolean value")"""

"""NOT Equal Operator
Outline:
Write a program to check the application of not equal operator"""

"""a=10
b=10
print(a!=b)"""

"""BMI Checker
Outline:
Write a program to calculate the BMI of a person?"""

height=int(input("enter your height in cm "))

weight=int(input("enter your weight in kg "))

BMI = weight/(height /  100)**2

print("your bmi is ",  BMI)

if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severely overweight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severly obese")