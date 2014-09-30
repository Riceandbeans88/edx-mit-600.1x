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
