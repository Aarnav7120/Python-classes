"""Well wishes
Outline:
Write a program to create a function name well wishes that will give output hello, how are you!"""

"""def well_wishes():
    print("hello")
    print("how are you?")

well_wishes()
well_wishes()"""

"""Weather condition
Outline:
Write a program to display the weather in autumn and spring :"""

"""spring="autumn"
autumn="winter"

def weather_condition():
    print("weather is pleasent in" ,spring)
    print("weather is same in" ,autumn)


weather_condition()"""

"""Calculator
Outline:
Write a program to make a calculator : For making a calculator create four functions add, subtract, 
multiply, divide. Ask for a choice from users which operation they want to
 perform. Take user input whatever operation they want to perform And call that function accordingly."""

def add(p, q):
    return p+q


def subtract(p, q):
    return p-q


def multiply(p, q):
    return p*q


def divide(p, q):
    return p/q

print("Please select operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

choice = input("Please enter choice (a/b/c/d):")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is an Invalid input")