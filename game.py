import random
#from tkinter import *

#window = Tk() #instantiate an instance of a window
#window.geometry("360x360")
#window.title("Gold River 2.0")

#window.config(background="#181818")

def rollDie(score, stage):
    dieChoice = dieSelection(stage)
    dice1 = random.choice(dieChoice)
    dice2 = random.choice(dieChoice)
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
    keepPlaying = input('\nTest Your Luck?\nPress 1 to continue\nPress 2 if you are a quitter\n')
    if keepPlaying == '2':
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
    d6List = [1,2,3,4,5,6]
    d8List = [1,2,3,4,5,6,7,8]
    d10List = [1,2,3,4,5,6,7,8,9,10]
    d12List = [1,2,3,4,5,6,7,8,9,10,11,12]
    #d20 doesn't contain a 1 so you can play the first 4 levels without losing
    d20List = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    if stage<=4:
        return d20List
    elif stage<=7 and stage>=5:
        return d12List
    elif stage<=10 and stage>=8:
        return d10List
    elif stage<=13 and stage>=11:
        return d8List
    else:
        return d6List

def main():
    score = 0
    stage = 1
    playAgain = '1'
    while score != -1 and playAgain == '1':
        print('\n\nStage ', stage, ': Roll the Die or... die')
        print('------------------------------------')
        score = rollDie(score, stage)
        if score == -1:
            playAgain = input('\nPlay Again?\nPress 1 to retry\nPress 2 to quit\n')
            if playAgain == '1':
                score = 0
                stage = 1
            else:
                print("\nGame over\n\n")
                break
        else:
            score = decide(score)
            stage = stage + 1
    return 0

main()