import random

t = ["rock", "paper", "scissors"]
computer = random.choice(t)
player = False

while player == False:
    player = input(" Choose from rock, paper or scissors??")
    if player == computer:
        print("Tie!!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!!" +player+ " smashes " +computer)
        else:
            print("You lose!!" +computer+ " covers " +player)
    elif player == "paper":
        if computer=="rock":
            print("You Win!!"+player+ " covers "+computer)
        else:
            print("You lose!!" +computer+ " cuts "+player)
    elif player =="scissors":
        if computer == "rock":
            print("You Lose!!" +computer+ " smashes " +player )
        else:
            print("You Win!!" +player+ " cuts " +computer)
    else:
        print("That is not a valid play. Check your spelling!")
    player = False
    computer = random.choice(t)

