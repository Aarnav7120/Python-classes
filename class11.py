"""number = 1
while number < 10:
    print(number)
    number +=1"""

"""Sum of Natural Numbers
Outline:
Write a program to find the sum of natural numbers."""

"""number= int(input("enter the final value: "))
sum = 0
i = 1 
while i <=number:
    sum = sum+i 
    i = i+1
print(sum)"""

"""Infinity
Outline:
Write a program to check the infinite loop?"""

"""i = 0
while i<=0:
    print("my name is Aarnav")"""   

"""Armstrong number
Outline:
Write a program to check if the number entered by the user is an Armstrong number or not?"""

num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

 