import random

def options(choice,choicePython):
  if choice == 'r' and choicePython == 'scissor' or choice == 's' and choicePython == 'paper' or choice == 'p' and choicePython == 'rock':
    return True  # in favour of player
  elif choice == choicePython:
    return 0
  else:
    return False  # in favour of python

def play(player):
  li = ['rock','paper','scissor']
  scorePlayer=0
  scorePython=0
  cond = True
  while cond:
    print("Press r for rock\nPress p for paper\nPress s for scissor\n")
    choice= input('Enter your choice:')
    choicePython=random.choice(li)
    print('PYTHON chose',choicePython)
    if options(choice,choicePython) == 0:
      print("No score\n")
    elif options(choice,choicePython):
      scorePlayer += 1
      print("Score of",player,":",scorePlayer)
      print("Score of PYTHON:",scorePython,"\n")
      if scorePlayer == 5:
        print("Congratulations",player)
        cond = False
    else:
      scorePython += 1
      print("Score of",player,":",scorePlayer)
      print("Score of PYTHON:",scorePython,"\n")  
      if scorePython == 5:
        print("PYTHON won the game, BETTER LUCK NEXT TIME !")
        cond = False

player = input("Enter your name:")  #player

print("Let's start the game\nYour opponent is PYTHON\n")
print ("- Guidelines: -\n")
print("A. A player will get 1 points for each winning\nB. The game will end when any player gets 5 points")
print("----------------------------------")
print("Shall we start ?\nPress 1 to start or 0 to quit:")
choice = int(input())
print()
if choice == 1:
  play(player)
else:
  print("Thank You !")
