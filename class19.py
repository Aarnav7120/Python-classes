"""Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?"""

"""import random

while True:
    user_action = input("Enter a choice (rock, paper, sciccors): ")
    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print("user_choice = ",  user_action)
    print("computer_choice = ", computer_action)


    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper smashes rock! You win!")
        else:
            print("scissors cut paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cut paper! You win!")
        else:
            print("rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break"""

"""Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?"""

import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isnt quite right, try again. \n")

