import random
while True:
    option = ('rock', 'paper', 'scissors')
    computer = random.choice(option)
    player = None
    while player not in option:
        player = input("Rock paper or scissors?").lower()

    if computer == player:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Its a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you lose")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you win")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you lose")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you win")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you lose")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("you win")


    choice = input("Do you want to play again? ")
    if choice != "yes":
        break
print("bye")
