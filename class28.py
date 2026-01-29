"""Is this a bus?
Outline:
Write a Python program to implement Inheritance by creating a Parent Class
 Vehicle with a constructor that has details like name, maximum speed, and mileage.
 Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase
 Inheritance to display the details of the Vehicle Bus named - School Volvo."""

"""class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
        pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage",
       School_bus.mileage)"""

"""Employee Inheritance
Outline:
Write a program to create a parent class Person (attributes - name, id number) 
with a method display to display the attributes. Next, create a child class
 Employee (attributes - name, id number, salary, post). Access the attributes of 
 parent class in child class. Then, create an object for
 child class and call the display method to display the name and id number."""

"""class Person( object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
    

        Person.__init__(self, name, idnumber)
    def display(self):
        print(self.salary)
        print(self.post)
        print(self.name)
        print(self.idnumber)

a = Employee('Rahul', 886012, 20000, "Intern")

a.display()"""

"""Super Penguin
Outline:
Write a program to create a base class Bird, with a constructor and two methods.
 Then, create a child class that inherits the constructor from Class Bird and has 
 two functions. Finally, display how you 
can use Super to access the parent class constructor inside the child class."""

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")
    
    def swim(self):
        print("swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    
    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()


    

