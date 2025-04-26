import random

# Rock, Paper, Scissors Game with Scoring System
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""

player_score = 0
computer_score = 0

while True:
    print(f"\nScore: You {player_score} - {computer_score} Computer")
    player_move = input("Choose [r]ock, [p]aper, or [s]cissors or [q]uit or [reset] score: ")

    if player_move == "q":
        print("Thanks for playing!")
        break
    elif player_move == "reset":
        player_score = 0
        computer_score = 0
        print("Scores have been reset!")
        continue

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid input. Please enter 'r', 'p', 's', 'q', or 'reset'.")
        continue

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
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
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1