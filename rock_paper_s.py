import random
import sys

print("Rock, Paper, Scissors!")

# use variables to keep track of score:
wins = 0
losses = 0
ties = 0

while True:  # main game loop
    while True:  # player's input loop
        print("\nEnter your move: (r)rock (p)paper (s)scissors OR (q)quit to stop playing")
        player_choice = input()
        if player_choice == 'q':
            sys.exit()  # to quit the game
        else:
            break   # to break out of player input loop and run rest of program

    # need to convert player's choices to integers to compare them with computer
    if player_choice == 'r':
        player_move = 'rock'
        player_choice = 1
    elif player_choice == 'p':
        player_move = 'paper'
        player_choice = 2
    elif player_choice == 's':
        player_move = 'scissors'
        player_choice = 3
    else:
        continue   # to jump up to start of while loop to get player to enter appropriate move or q

    # print player's move
    print(f"{player_move.upper()} versus...")

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_move = 'rock'
    elif computer_choice == 2:
        computer_move = 'paper'
    elif computer_choice == 3:
        computer_move = 'scissors'

    # print computer's move
    print(f"{computer_move.upper()}")

    # determine who won and print it
    if player_choice == computer_choice:
        ties += 1
        print("It's a tie!")
    elif player_choice == 1 and computer_choice == 2:
        losses += 1
        print("You lose!")
    elif player_choice == 1 and computer_choice == 3:
        wins += 1
        print("You win!")
    elif player_choice == 2 and computer_choice == 1:
        wins += 1
        print("You win!")
    elif player_choice == 2 and computer_choice == 3:
        losses += 1
        print("You lose!")
    elif player_choice == 3 and computer_choice == 1:
        losses += 1
        print("You lose!")
    elif player_choice == 3 and computer_choice == 2:
        wins += 1
        print("You win!")

    # print new score
    print(f"{wins} Wins, {losses} Losses, & {ties} Ties")
