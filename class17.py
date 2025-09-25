"""for i in range(11):
    if i == 5:
        continue

    print(i)"""

"""Break
Outline:
Write a program to check alphabet “A” is present in the given string or not.
 And terminate the loop after finding the alphabet “A.”"""

"""a = input ("Enter a word: ")
for i in a:
    if (i == 'A'):
        print("A is found")
        break #break statement
    else:
        print("A not found")"""

"""Pass
Outline:
Write a program to satisfy the following conditions of the given range: 
If the number is divisible by 20, it provides an output "twist."
If the number is divisible by 15, it will pass (no output)
If the number is divisible by 5, it will give an output “fizz.”
If the number is divisible by 3, it will give an output "buzz." 
Otherwise, it will give the output of that number."""

"""for num in range(10):
    if num % 20 == 0:
        print("twist")
    elif num % 15 == 0:
        continue  
    elif num % 5 == 0:
        print("fizz")
    elif num % 3 == 0:
        print("buzz")
    else:
        print(num)"""

"""Continue
Outline:
Write a program to display 1 to 10 numbers in reverse order and skip the number 5."""


var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue

    print('\nCurrent variable value :', var)
print ("\nGood bye!")








    