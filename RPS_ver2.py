import sys

# program evaluates a two player's input for rock paper scissors and outputs the winners

player_one = "Player One"
player_two = "Player Two"

rps_string = "Player {0}: Rock, Paper, or Scissors? "

rock = "rock"
paper = "paper"
scissors = "scissors"
SET_PLAYS = set([rock, paper, scissors])


# Compare the choices of player 1 and Player 2 and output the winner
def decide_winner(p1, p2):
    # print 'player 1 chooses', player1
    # print 'player 2 chooses', player2
    if p1 == p2:
        return "Nobody! It's a tie"
    if p1 == rock and p2 == paper:
        return player_two
    if p1 == rock and p2 == scissors:
        return player_one
    if p1 == paper and p2 == rock:
        return player_one
    if p1 == paper and p2 == scissors:
        return player_two
    if p1 == scissors and p2 == rock:
        return player_two
    if p1 == scissors and p2 == paper:
        return player_one

    # If an input that isn't rock, paper, or scissors gets through, let the players know they broke it
    # this is impossible
    else:
        print 'How did you break the game?'
        return 'Nobody knows!'

print 'Welcome to ROCK, PAPER, SCISSORS!!!!!'

# while loop uses test_input() to ensure that the player inputs are rock, paper, or scissors
while True:

    # gather the player choices and convert to lowercase for easy comparison later
    player_one_input = raw_input(rps_string.format("One")).lower()
    player_two_input = raw_input(rps_string.format("Two")).lower()

    # If the test_input() returns
    if player_one_input not in SET_PLAYS or player_two_input not in SET_PLAYS:
        # ghetto way to quit, but going for it.
        print 'Please enter a choice that is either Rock, Paper, or Scissors!'
    else:
        # Test prints for the chosen input
        # print player1, type(player1)
        # print player2, type(player2)

        # Compute who is the winner
        winner = decide_winner(player_one_input, player_two_input)

        # Who won?
        print 'And the winner is... {0}!!!!'.format(winner)

    play_again_input = raw_input("Play again?  y/n ").lower()

    if play_again_input != 'y':
        sys.exit(0)
