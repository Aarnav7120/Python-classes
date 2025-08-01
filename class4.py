"""Average
Outline:
There are five trees in Jack's front yard. He checks each tree to find out how tall it is
 in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11.
   What is the average height of a tree in Jack's front yard?"""

"""tree1=int(input("enter the height of tree1: "))
tree2=int(input("enter the height of tree2: "))
tree3=int(input("enter the height of tree3: "))
tree4=int(input("enter the height of tree4: "))
tree5=int(input("enter the height of tree5: "))

average=(tree1+tree2+tree3+tree4+tree5)/5
print("the average of all the trees are ",average)"""

"""Percentage calculation
Outline:
Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?"""

"""subject1=int(input("enter the marks of subject1: "))
subject2=int(input("enter the marks of subject2: "))
subject3=int(input("enter the marks of subject3: "))
subject4=int(input("enter the marks of subject4: "))
sum=subject1+subject2+subject3+subject4
percentage=(sum/400)*100
print("the percentage of all subjects are", percentage)"""

"""Count the notes
Outline:
Write a program to calculate the number of notes in the given amount?"""

"""amount=int(input("Please enter the amount: "))
note10=amount/10
note50=amount/50
note100=amount/100
note500=amount/500
print("requierd 10 rs notes are ",note10)
print("requierd 50 rs notes are ",note50)
print("requierd 100 rs notes are ",note100)
print("requierd 500 rs notes are ",note500)"""

import math
number = float(input("Please enter a number: "))

if number < 0:
        print("Sorry, square root of a negative number is not real.")
else:
        square_root = math.sqrt(number)
        print(f"The square root of {number} is {square_root}")
