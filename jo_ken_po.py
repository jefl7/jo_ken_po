from random import randint
options = ('Rock', 'Paper', 'Scissors')
computer = randint(0,2)
player = int(input('''Chose your option:
0.Rock
1.Paper
2.Scissors\n'''))
print('The computer chose {}'.format(options[computer]))
if 0 > player or player > 2:
    print('Invalid moviment')
elif player == computer:
    print('We have a draw!')
elif (player == 0 and computer == 1) or player == 1 and computer == 2 or player == 1 and computer == 0:
    print('You lose!')
else:
    print('You win!')
