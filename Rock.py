# Simple rock paper scissors game
# 2022-09-27
# Jackson Blackman


import random
import os
from time import sleep

while True:
    os.system('cls')
    types = ['Rock', 'Paper', 'Scissors']

    randomchoice = random.choice(types)

    playerchoice = input('Choose an input R = Rock, S = Scissors, P = Paper \n:').capitalize()

    print("the computer chose", randomchoice)

    if playerchoice == 'R' and randomchoice == 'Scissors' or playerchoice == 'P' and randomchoice == 'Rock' or playerchoice == 'S' and randomchoice == 'Paper':
        print('You win, the game will continue in 5 seconds')
        sleep(5)

    if playerchoice == 'R' and randomchoice == 'Rock' or playerchoice == 'P' and randomchoice == 'Paper' or playerchoice == 'S' and randomchoice == 'Scissors':
        print('Draw, the game will continue in 5 seconds')
        sleep(5)

    if randomchoice == 'Rock' and playerchoice == 'S' or randomchoice == 'Paper' and playerchoice == 'R' or randomchoice == 'Scissor' and playerchoice == 'P':
        print('You lose, the game will continue in 5 seconds')
        sleep(5)
