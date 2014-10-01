__author__ = 'AE'


'''
*** ERROR ***
*** Incorect as of 9-30-14
YOU AND YOUR COMPUTER  (15 points possible)
Now that your computer can choose a word, you need to give the computer the option to play.
Write the code that re-implements the playGame function.
You will modify the function to behave as described below in the function's comments.
As before, you should use the HAND_SIZE constant to determine the number of cards in a hand.
Be sure to try out different values for HAND_SIZE with your program.

'''

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
