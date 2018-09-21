import random

moves = ['rock', 'paper', 'scissors']
player_wins = ['rockscissors', 'scissorspaper', 'paperrock']

player_move = input ("Please choose either rock/paper/scissor: ")
computer_move = random.choice(moves)


print ("Your move was: ", player_move)
print ("Computer choosed", computer_move)

if player_move == computer_move:
    print("It's a tie")
elif player_move + computer_move in player_wins:
    print("You win!")
else:
    print("You lose..."")