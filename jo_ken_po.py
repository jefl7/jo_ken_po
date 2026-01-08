from random import randint
import time
options = ('Rock', 'Paper', 'Scissors')
computer = randint(0,2)
name = str(input('Enter your name:'))
print('<=>'* 20)
print('Welcome to Jo Ken Po game {}'.format(name).center(60))
print('<=>'* 20)
player = int(input('''Chose your option:
0.Rock
1.Paper
2.Scissors\n'''))
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Po')
time.sleep(1)

print('<=>'* 20)
print('The computer chose {}'.format(options[computer]))
print('The player chose {}'.format(options[player]))
print('<=>'* 20)
if 0 > player or player > 2:
    print('Invalid moviment')
elif player == computer:
    print('We have a draw!')
elif player == 0 and computer == 1 or player == 1 and computer == 2 or player == 1 and computer == 0:
    print('You lose!')
else:
    print('You win!')
