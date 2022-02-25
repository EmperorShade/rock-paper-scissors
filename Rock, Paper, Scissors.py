import random

while True:

    #play selections and variables
    user_action = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_selection = random.choice(options)
    print(f"\nYou chose {user_action}, the computer chose {computer_selection}.\n")

    #deciding a winner
    if user_action == computer_selection:
        print(f"It's a tie! Don't choose the same, idiots") 

    elif user_action == "rock" :
        if computer_selection == "scissors" :
            print(f"Your rock smashes the scissors. You win!")
        
        else:
            print(f"Paper chokes your rock. Goodbyee, looser!")

    elif user_action == "paper":
        if computer_selection == "scissors":
            print(f"Snip, snip! Your paper is cut by scissors.")

        else:
            print(f"Your paper chokes the poor rock. Are you happy now?")

    elif user_action == "scissors":
        if computer_selection == "paper":
            print(f"Good, you sharped your scissors. You win!")

        else:
            print(f"The rock smashes your scissor to death. Buh byee!")


    play_again = input("\nPlay Again? (y/n)\n")
    if play_again.lower() != "y":
        break