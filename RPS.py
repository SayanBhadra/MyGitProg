import random
option = ('rock', 'paper', 'scissors')
computer = random.choice(option)
player = input("Rock paper or scissors?")
print("Computer: ",computer)
print("Player: " ,player)
if computer == player:
    print("Its a tie!")
