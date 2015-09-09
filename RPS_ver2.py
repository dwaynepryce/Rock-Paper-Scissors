# program evaluates a two player's input for rock paper scissors and outputs the winners

SET_PLAYS = set(['rock', 'paper', 'scissors'])

# ensure that the input is within legal bounds of rock, paper, scissors
def test_input(x):
    return x in SET_PLAYS


# Compare the choices of player 1 and Player 2 and output the winner
def decide_winner(p1, p2):
    # print 'player 1 chooses', player1
    # print 'player 2 chooses', player2
    if p1 == p2:
        return "nobody! It's a tie"
    if p1 == 'rock' and p2 == 'paper':
        return 'Player Two'
    if p1 == 'rock' and p2 == 'scissors':
        return 'Player One'
    if p1 == 'paper' and p2 == 'rock':
        return 'Player One'
    if p1 == 'paper' and p2 == 'scissors':
        return 'Player Two'
    if p1 == 'scissors' and p2 == 'rock':
        return 'Player Two'
    if p1 == 'scissors' and p2 == 'paper':
        return 'Player One'

    # If an input that isn't rock, paper, or scissors gets through, let the players know they broke it
    else:
        print 'How did you break the game?'
        return 'nobody knows!'


print 'Welcome to ROCK, PAPER, SCISSORS!!!!!'

# while loop uses test_input() to ensure that the player inputs are rock, paper, or scissors
while True:

    # gather the player choices and convert to lowercase for easy comparison later
    player1 = raw_input('Player one.. Rock, Paper, or Scissors? ').lower()
    player2 = raw_input('Player two.. Rock, Paper, or Scissors? ').lower()

    # If the test_input() returns
    if test_input(player1) == True and test_input(player2) == True:
        break

    else:
        print 'Please enter a choice that is either Rock, Paper, or Scissors!'

# Test prints for the chosen input
# print player1, type(player1)
# print player2, type(player2)

# Compute who is the winner
winner = decide_winner(player1, player2)

# Who won?
print 'and the winner is....', winner + '!!!!'
