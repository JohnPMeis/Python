
#rps.py
# a python versio of rock paper scissors
#

import random, sys

print('ROCK, PAPER, SCISSORS, LIZARD, SPOCK')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors (l)izard (sp)ock or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's' or playerMove == 'l' or playerMove == 'sp':
            break # Break out of the player input loop.
        print('Type one of r, p, s, l, sp or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    elif playerMove == 'l':
        print('LIZARD versus...')
    elif playerMove == 'sp':
        print('SPOCK versus...')
        

    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    elif randomNumber == 4:
        computerMove = 'l'
        print('LIZARD')
    elif randomNumber == 5:
        computerMove = 'sp'
        print('SPOCK')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Rock destroys scissors, You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'l':
        print('Rock kills Lizard, You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Paper covers rock, You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'sp':
        print('Paper dispoves Spock, You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Scissors shred paper, You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'l':
        print('Scissors kills lizard, You win!')
        wins = wins + 1
    elif playerMove == 'l' and computerMove == 'sp':
        print('Lizard poisons spock, You win!')
        wins = wins + 1
    elif playerMove == 'l' and computerMove == 'p':
        print('Lizard eats paper, You win!')
        wins = wins + 1
    elif playerMove == 'sp' and computerMove == 'r':
        print('Spock obliterates rock, You win!')
        wins = wins + 1
    elif playerMove == 'sp' and computerMove == 's':
        print('Spock dismantles scissors, You win!')
        wins = wins + 1
        
        
    elif playerMove == 'r' and computerMove == 'p':
        print('Paper covers rock, You lose!')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'sp':
        print('Spock obliterates rock, You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Scissors shred paper, You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'l':
        print('Lizard eats paper, You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Rock destroys scissors, You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'sp':
        print('Spock dismantles scissors, You lose!')
        losses = losses + 1
    elif playerMove == 'l' and computerMove == 'r':
        print('Rock kills lizard, You lose!')
        losses = losses + 1
    elif playerMove == 'l' and computerMove == 's':
        print('Scissors kills lizard, You lose!')
        losses = losses + 1
    elif playerMove == 'sp' and computerMove == 'l':
        print('Lizard poisons spock, You lose!')
        losses = losses + 1
    elif playerMove == 'sp' and computerMove == 'p':
        print('Paper dispoves spock, You lose!')
        losses = losses + 1


