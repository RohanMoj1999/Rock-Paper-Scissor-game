import random


def options(choice, choicePython):
  if (choice == 'r' and choicePython == 'scissor') or (choice == 's' and choicePython == 'paper') or (choice == 'p' and choicePython == 'rock'):
    return True  # in favour of player
  elif choice == choicePython:
    return 'noscore'    #   both chooses same
  else:
    return False  # in favour of python


def play(player):
  li = ['rock', 'paper', 'scissor', 'rock', 'paper', 'scissor']
  scorePlayer = 0
  scorePython = 0
  cond = True
  while cond:
    print("Press r for rock\nPress p for paper\nPress s for scissor\n")
    choice = input('Enter your choice:')
    if choice == 'r' or choice == 'p' or choice == 's':
        choicePython = random.choice(li)
        print('PYTHON chose:', choicePython)
        if options(choice, choicePython) == 'noscore':
            print("No score\n")
        elif options(choice, choicePython) == True:
            scorePlayer += 1
            print("Score of", player, ":", scorePlayer)
            print("Score of PYTHON:", scorePython, "\n")
        if scorePlayer == 5:
            print("\nCongratulations", player,"!")
            cond = False
        elif options(choice, choicePython) == False:
            scorePython += 1
            print("Score of", player, ":", scorePlayer)
            print("Score of PYTHON:", scorePython, "\n")
            if scorePython == 5:
                print("\nPYTHON won the game, BETTER LUCK NEXT TIME !")
                cond = False
    else:
        print("-------- Enter valid option ! --------")


player = input("Enter your name:")  # player

print("Let's start the game\nYour opponent is PYTHON\n")
print("- Guidelines: -\n")
print("A. A player will get 1 points for each winning\nB. The game will end when any player gets 5 points")
print("----------------------------------")
cond = True
while cond:
    try:
        print("Shall we start ?\nPress 1 to start or 0 to quit:")
        choice = int(input())
        print()
    except:
        print("Enter Valid option !")
    else:
        if choice == 1:
            play(player)
            cond = False
        elif choice == 0:
            print("Thank You !")
            cond = False
        else:
            print("Enter valid option !")
