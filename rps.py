import random

player = input ("Please choose either rock/paper/scissor: ")
player = player.lower()
while (player != "rock" and player != "paper" and player != "scissor"):
    print(player);
    player = input("That choice is not valid. Enter your choice (rock/paper/scissor): ");
    player = player.lower();
