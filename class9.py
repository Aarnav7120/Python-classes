"""medical_cause=input("did you have a medical cause Y or N: ")

atten= int(input("enter the attendance of teh student: "))

if medical_cause == 'Y':
    print ("You are allowed")
else:
    if atten>75:
        print("Allowed")
    else:
        print("Not Allowed")"""

"""choice = int( input("Enter your choice: ") )

if( choice == 1):
    print( "What type of bike? " )
    print("1.Scooty\n")
    print("2.Scooter\n")

    choice2 = int( input("Enter your choice2: ") )
    if choice2==1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")

elif(choice == 2 ): 
    print("what type of car")
    print("1.Sedan")
    print("2.XUV")
    choice3 = int( input("Enter your choice3: ") )

    if choice3==1:
        print("You have selected XUV")
else:
    print("Wrong choice!")"""

units = int(input(" Please enter Number of Units you Consumed : "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units < 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif(units < 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((units -200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.2f" %total)
