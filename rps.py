import random

# Choices for the game
choices=[" Rock"," Paper"," Scissors"]

# Computer randomly selects
computer_choice=random.choice(choices)
# User input
user_choice = input("Enter your choice (Rock, Paper, or Scissors): ")

# Determine the winner
if user_choice == computer_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
else:
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")
