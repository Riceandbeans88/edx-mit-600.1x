__author__ = 'Scarlett'

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    # return (len(word) * sum(SCRABBLE_LETTER_VALUES[x] for x in word)) + (50 if len(word) == n else 0)
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter] * len(word)
    if len(word) == n:
        score += 50
    return score



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function

    updated_hand = hand.copy()
    for letters in word:
        updated_hand[letters] = updated_hand.get(letters,0) - 1

    return updated_hand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    copy_hand = hand.copy()
    ans = False
    if word in wordList:
        ans = True

    for letter in word:
        if copy_hand.get(letter,0) == 0:
            return False
        else:
            copy_hand[letter] = copy_hand.get(letter,0) - 1

    return ans

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    ans = sum(hand.values())
    return ans


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
    # BEGIN PSEUDOCODE (download ps4a.py to see)

    total_score = 0
    notification = "Run out of letters."

    #event loop
    while calculateHandlen(hand) > 0:
        #Display the hand
        displayHand(hand)
        #Prompt user for input
        input_word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
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
                print selectedWord, 'earned', str(word_score), 'points. Total:', total_score, 'points'
                hand = updateHand(hand, word)
    print notification 'Total score:', total_score, 'points.'

#correct

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



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

    hand = {}
    while choice != 'e':
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand.copy(), wordList, HAND_SIZE)
        elif choice == 'r':
            if len(hand) == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                playHand(hand.copy(), wordList, HAND_SIZE)
        else:
            print 'Invalid command.'
        choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max = 0
    max_value_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > max:
                max = score
                max_value_word = word
    return max_value_word


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
    # TO DO ...




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





















































def compPlayHand(hand, wordList):
    """
Allows the computer to play the given hand, following the same procedure
as playHand, except instead of the user choosing a word, the computer
chooses it.

1) The hand is displayed.
2) The computer chooses a word.
3) After every valid word: the word and the score for that word is
displayed, the remaining letters in the hand are displayed, and the
computer chooses another word.
4) The sum of the word scores is displayed when the hand finishes.
5) The hand finishes when the computer has exhausted its possible
choices (i.e. compChooseWord returns None).
hand: dictionary (string -> int)
wordList: list (string)
"""
    # Keep track of two numbers: the number of letters left in your hand and the total score
    remainingLetters = calculateHandlen(hand)
    totalScore = 0

    # As long as there are still letters left in the hand:
    while remainingLetters > 0:
        # Display the hand
        print 'Current hand:',
        displayHand(hand)
        # Ask user for input
        selectedWord = compChooseWord(hand, wordList)
        if selectedWord == None:
            break

        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        score = getWordScore(selectedWord, HAND_SIZE)
        totalScore += score
        print selectedWord, 'earned', str(score), 'points. Total:', totalScore, 'points'
        # Update the hand
        hand = updateHand(hand, selectedWord)
        remainingLetters = calculateHandlen(hand)


    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if remainingLetters == 0:
        print 'Run out of letters. Total score:', totalScore, 'points.'
    else:
        print 'Goodbye! Total score:', totalScore, 'points.'





def playHand(hand, wordList, n):

    # Keep track of two numbers: the number of letters left in your hand and the total score
    remainingLetters = calculateHandlen(hand)
    totalScore = 0

    # As long as there are still letters left in the hand:
    while remainingLetters > 0:

        # Display the hand
        print 'Current hand:',
        displayHand(hand)
        # Ask user for input
        selectedWord = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if selectedWord == '.':
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(selectedWord, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(selectedWord, n)
                totalScore += score
                print selectedWord, 'earned', str(score), 'points. Total:', totalScore, 'points'
                # Update the hand
                hand = updateHand(hand, selectedWord)
                remainingLetters = calculateHandlen(hand)


    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if remainingLetters == 0:
        print 'Run out of letters. Total score:', totalScore, 'points.'
    else:
        print 'Goodbye! Total score:', totalScore, 'points.'










def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    max = 0
    max_value_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > max:
                max = score
                max_value_word = word
    return max_value_word



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
    notification = "Run out of letters."

    #event loop
    while calculateHandlen(hand) > 0:
        #Display the hand
        displayHand(hand)
        #Prompt user for input
        input_word = compChooseWord(hand, wordList, n)
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
                print selectedWord, 'earned', str(word_score), 'points. Total:', total_score, 'points'
                hand = updateHand(hand, word)
    print notification 'Total score:', total_score, 'points.'


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    max = 0
    max_value_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > max:
                max = score
                max_value_word = word
    return max_value_word



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