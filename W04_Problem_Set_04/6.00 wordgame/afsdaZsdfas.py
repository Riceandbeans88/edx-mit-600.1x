__author__ = 'Scarlett'
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
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


