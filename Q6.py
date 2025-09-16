import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
ties = 0

print("Rock, Paper, Scissors! Type 'quit' to stop.")

while True:
    player = input("Your choice: ").lower()
    if player == "quit":
        break
    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")
        ties += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

print("Final Scores - Player:", player_score, "Computer:", computer_score, "Ties:", ties)
