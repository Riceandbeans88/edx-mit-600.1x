__author__ = 'Aaron Echavarria'

'''
PLAYING A HAND  (15/15 points)
In ps4a.py, note that in the function playHand, there is a bunch of pseudocode.
This pseudocode is provided to help guide you in writing your function.
Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:
'''

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    total_score = 0
    #event loop
    while calculateHandlen(hand) > 0:
        #Display the hand
        print 'Current hand:',
        displayHand(hand)
        #Prompt user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == '.':
            #Break the loop Goodbye to game state
            output = "Goodbye!"
            break
        else:
            #Invalid words are rejected
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.")
            else:
                word_score = getWordScore(word, n)
                total_score += word_score
                print word, 'earned', str(word_score), 'points. Total:', total_score, 'points'
                hand = updateHand(hand, word)
    print 'Run out of letters. Total score:', total_score, 'points.'