def rock_paper_sci(p1, p2):
    if (p1 == 'scissors') and (p2 == 'paper'):
        print "Player 1 won!"
    elif (p1 == 'paper') and (p2 == 'rock'):
        print 'Player 1 won!'
    elif (p1 == 'rock') and (p2 == 'scissors'):
        print 'Player 1 won!'
    elif (p1 == 'paper') and (p2 == 'scissors'):
        print 'Player 2 won!'
    elif (p1 == 'rock') and (p2 == 'paper'):
        print 'Player 2 won!'
    elif (p1 == 'scissors') and (p2 == 'rock'):
        print 'Player 2 won!'
    elif (p1 == p2):
        print 'Draw!'

rock_paper_sci('rock','rock')

