'''
Description: RPS Homework, Week 1
Written By: Avery Einhorn
Date: 10/6/18
Only got help from TA during discussion! 
I commented out my print() functions because TA said you would not be using them to grade my code.'''
# the choice function is needed in the last problem below
from random import choice
# a version of rock-paper-scissors where the computer cheats and always wins.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
#option for user choice: pChoice = input('Please enter either "rock", "paper", or "scissors" in lower case to the right ->')
def rpsCheat(pChoice):
    if pChoice == "rock"or"paper"or"scissors":
        return 'computer wins'
    else:  #just in case the user doesn't know how to type rock/paper/scissors
        return 'error. please try again.'
'''print('here is rpsCheat')
print('if rock,',rpsCheat('rock'))
print('if paper,',rpsCheat('paper'))
print('if scissors,',rpsCheat('scissors'))'''

# a version of rock-paper-scissors where the computer
# always chooses rock.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rpsRock(pChoice):
    if pChoice == 'rock':
        return 'tie game'
    elif pChoice == 'paper':
        return 'person wins'
    elif pChoice == 'scissors':
        return 'computer wins'
    else:
	    return 'error. please try again.'
'''print('here is rpsRock')
print('if rock,',rpsRock('rock'))
print('if paper,',rpsRock('paper'))
print('if scissors,',rpsRock('scissors'))'''

# an implementation of rock-paper-scissors for two players.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# cChoice is the computer's choice of a move, with the same three possible values.
# returns either 'person wins', 'computer wins', or 'tie game'.
# option for user input: cChoice = input("Now grab a second player. It's their turn to choose rock, paper, or scissors in lower case -> ")
def rps2(pChoice, cChoice):
    if ((pChoice == 'rock')and(cChoice == 'scissors'))or((pChoice == 'paper')and(cChoice == 'rock'))or((pChoice == 'scissors')and(cChoice == 'paper')):
        return 'person wins'
    elif ((cChoice == 'rock')and(pChoice == 'scissors'))or((cChoice == 'paper')and(pChoice == 'rock'))or((cChoice == 'scissors')and(pChoice == 'paper')):
        return 'computer wins'
    elif (pChoice == cChoice):
        return 'tie game'
    else:
        return 'error. please try again.'
'''print('here is rps2. The first argument is pChoice.')
print('if rock & rock,',rps2('rock','rock')) #which means if Person chooses rock AND computer chooses rock
print('if paper & paper,',rps2('paper','paper'))
print('if scissors & scissors,',rps2('scissors','scissors'))
print('if rock & scissors,',rps2('rock','scissors'))
print('if paper & rock,',rps2('paper','rock'))
print('if scissors & paper,',rps2('scissors','paper'))
print('if rock & paper,',rps2('rock','paper'))
print('if paper & scissors,',rps2('paper','scissors'))
print('if scissors & rock,',rps2('scissors','rock'))'''

# an implementation of rock-paper-scissors where the computer
# chooses its move randomly.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rpsRandom(pChoice):
    comp=choice(['rock','paper','scissors'])
    result=rps2(pChoice,comp)
    return result
'''print('here is rpsRandom')
print('if rock,',rpsRandom('rock'))
print('if paper,',rpsRandom('paper'))
print('if scissors,',rpsRandom('scissors'))'''