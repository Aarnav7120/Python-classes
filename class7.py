"""Outline:
Write a program to illustrate the use of 'is' identity operator"""

"""x = 5 
if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.0
if (type(x) is not float):
    print("true")
else:
    print("false")


x = 20 
y = 20
if (x is y):
    print("x & y SAME identity")

y=30
if (x is not y ):
    print("x & y have DIFFERENT identity")"""

"""Outline:
Write a program to apply the right shift and left shift bitwise operator."""

"""a = 10
b = -10

print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

print("a << 1 =", a << 1)
print("b << 1 =", b << 1)"""

"""Outline:
Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example,
 if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?"""

print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<=91:
    print("Your Grade is A2")
elif avg>=71 and avg<=81:
    print("Your Grade is B1")
elif avg>=61 and avg<=71:
    print("Your Grade is B2")
elif avg>=51 and avg<=61:
    print("Your Grade is C1")
elif avg>=41 and avg<=51:
    print("Your Grade is C2")
elif avg>=33 and avg<=41:
    print("Your Grade is D")
elif avg>=21 and avg<=33:
    print("Your Grade is E1")
elif avg>=0 and avg<=21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
