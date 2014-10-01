__author__ = 'Aaron Echavarria'

'''
*** ERROR ***
*** Incorect as of 9-30-14
COMPUTER PLAYS A HAND  (10 points possible)
Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to Part A's playHand function (get the hint?).

Implement the compPlayHand function. This function should allow the computer to play a given hand, using the procedure you just wrote in the previous part. This should be very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand will be different.

Be sure to test your function on some randomly generated hands using dealHand.

Test Cases
Test Cases

Paste your definition of compChooseWord, in addition to your definition of compPlayHand, in the box below.
'''


def compPlayHand(hand, wordList, n):
    total_score = 0
    #event loop
    while calculateHandlen(hand) > 0:
        #Display the hand
        print 'Current hand:',
        displayHand(hand)
        #Prompt user for input
        word = compChooseWord(hand, wordList, n)
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

  def compChooseWord(hand, wordList, n):
    max = 0
    max_value_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > max:
                max = score
                max_value_word = word
    return max_value_word
    print compChooseWord(hand, wordList, n):