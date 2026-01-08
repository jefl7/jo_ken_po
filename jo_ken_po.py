from random import randint
import time
options = ('Rock', 'Paper', 'Scissors')
computer = randint(0,2)
print('My name is The Turk, the master of Jo Ken Po')
time.sleep(2)
print('After leaving the chess behind, I decided to try a new game...')
time.sleep(2)
print('Do you have the courage to challenge me?')
time.sleep(2)
name = str(input('If you have, so enter your name:'))
print('<=>'* 20)
print('Welcome to Jo Ken Po game {}'.format(name).center(60))
print('<=>'* 20)
player = int(input('''Chose your option:
0.Rock
1.Paper
2.Scissors\n'''))

if  player < 0 or player > 2:
    print('Invalid moviment')
else:
    print('Jo')
    time.sleep(1)
    print('Ken')
    time.sleep(1)
    print('Po')
    time.sleep(1)

print('<=>'* 20)
print('The Turk chose {}'.format(options[computer]).center(60))
print('{} chose {}'.format(name, options[player]).center(60))
print('<=>'* 20)

if player == computer:
    print('We have a draw!')
elif player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
    print('You lose!')
elif player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print('You win!')
