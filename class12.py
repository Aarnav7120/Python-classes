"""string = input("Please enter your own word : ")

char = input("Please enter your own Character : ")
i = 0
count = 0

while(i < len(string)):
      if(string[i] == char): 
        count = count + 1
      i = i + 1

print("The total Number of Times ", char, " has Occurred = " , count)"""


"""lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print("Prime numbers between", lower, "and", upper,"are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else: 
            print(num)"""

num = int(input("Enter the number : "))
t = num
numLen = 0

while t>0: 
  numLen = numLen+1
  t = int(t/10)

if numLen>=4: 
  numLen = int(numLen/2)
  chk = 0
  while num>0:
    rem = num%10
    if chk==numLen: 
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo 

  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")

