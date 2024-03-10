import random
import os
#from tkinter import *

#window = Tk() #instantiate an instance of a window
#window.geometry("360x360")
#window.title("Gold River 2.0")

#window.config(background="#181818")

class dice:
    name = ""
    values = []

d6 = dice()
d6.name = 'D6'
d6.value = [1,2,3,4,5,6]
d8 = dice()
d8.name = 'D8'
d8.value = [1,2,3,4,5,6,7,8]
d10 = dice()
d10.name = 'D10'
d10.value = [1,2,3,4,5,6,7,8,9,10]
d12 = dice()
d12.name = 'D12'
d12.value = [1,2,3,4,5,6,7,8,9,10,11,12]
d20 = dice()
d20.name = 'D20'
#d20 doesn't contain a 1 so you can play the first 4 levels without losing
d20.value = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def rollDie(score, stage):
    dieChoice_Value, dieChoice_name  = dieSelection(stage)
    dice1 = random.choice(dieChoice_Value)
    dice2 = random.choice(dieChoice_Value)
    print('Current Dice Set --> ', dieChoice_name,' <--')
    print('\nDice Number 1 : ',dice1)
    print('Dice Number 2 : ',dice2)
    if (dice1 == 1 or dice2 == 1):
        score = -1
        return score
    else:
        score += dice1 + dice2 + stage
        print("Score = ", score)
        return score
    
def decide(score):
    while True:
        try:
            keepPlaying = int(input('\nTest Your Luck?\nPress 1 to continue\nPress 2 if you are a quitter\nEnter here: '))
            if keepPlaying>2 or keepPlaying<1:
                raise ValueError
            break
        except ValueError:
            print("Invalid response. Please select 1 or 2!")
    if keepPlaying == 2:
        print("\nYour final score is ", score)
        write2File(score)
        score = -1
        print("Game over")
    return score

def write2File(score):
    with open('scoreFile.txt', 'a') as f:
        f.write('\nRun score: ' + repr(score) + ' points\n')
        f.close()

def dieSelection(stage):
    if stage<=4:
        return d20.value, d20.name
    elif stage<=7 and stage>=5:
        return d12.value, d12.name
    elif stage<=10 and stage>=8:
        return d10.value, d12.name
    elif stage<=13 and stage>=11:
        return d8.value, d8.name
    else:
        return d6.value, d6.name

def main():
    score = 0
    stage = 1
    playAgain = 1

    os.system('cls' if os.name == 'nt' else 'clear') #clears terminal on start/restart
    print('------------------------------------\nWelcome to the Game! Be Careful to Not Let Greed Consume You!\n')
    while True:
        try:
            startVar = int(input('Press 1 to Roll the Dice or Press 2 to Quit Out\nEnter Here: '))
            if startVar>2 or startVar<1:
                raise ValueError
            break
        except ValueError:
            print("Invalid response. Please select 1 or 2!")
    print('------------------------------------')

    while score != -1 and playAgain == 1 and startVar == 1:
        print('\n\nStage ', stage, ': Roll the Die or... die')
        print('------------------------------------')
        score = rollDie(score, stage)
        if score == -1:
            while True:
                try:
                    playAgain = int(input('\nPlay Again?\nPress 1 to retry\nPress 2 to quit\n'))
                    if playAgain>2 or playAgain<1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid response. Please select 1 or 2!")
            if playAgain == 1:
                main()
            else:
                print("\nGame over\n\n")
                break
        else:
            score = decide(score)
            stage = stage + 1
    return 0

main()