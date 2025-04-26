import random
# Rock, Paper, Scissors Game

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""

player_move = input("Choose [r]ock, [p]aper, or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Please enter 'r', 'p', or 's'.")

computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
    print(f"Computer's move: {computer_move}")
elif computer_random_number == 2:
    computer_move = paper
    print(f"Computer's move: {computer_move}")
elif computer_random_number == 3:
    computer_move = scissors
    print(f"Computer's move: {computer_move}")

# Determine the winner

if player_move == computer_move:
    print("The game is a tie!")
elif (player_move == rock and computer_move == scissors) or \
     (player_move == paper and computer_move == rock) or \
     (player_move == scissors and computer_move == paper):
    print("You win!")
else:
    print("You lose!")