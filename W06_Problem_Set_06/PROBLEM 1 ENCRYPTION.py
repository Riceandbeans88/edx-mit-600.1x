__author__ = 'Aaron Echavarria'

'''
You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.
Test Cases
buildCoder(3)
{'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
buildCoder(9)
{'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}

'''

# Hints
# Upper and Lower Case Letters
# Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
# If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:
# >>> import string
# >>> print string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz
# >>> print string.ascii_uppercase
# ABCDEFGHIJKLMNOPQRSTUVWXYZ


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO
    dict = {}
    upCase = string.ascii_uppercase
    lowCase = string.ascii_lowercase
    for char in range(len(upCase)):
        dict[upCase[char]] = upCase[(char+shift)%len(upCase)]
    for char in range(len(lowCase)):
        dict[lowCase[char]] = lowCase[(char+shift)%len(lowCase)]
    return dict


'''
Next, define the function applyCoder, which applies a coder to a string of text.

Test Cases

>>> applyCoder("Hello, world!", buildCoder(3))
'Khoor, zruog!'
>>> applyCoder("Khoor, zruog!", buildCoder(23))
'Hello, world!'
'''

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    encode = ""
    for char in text:
        if char in coder:
            encode += coder[char]
        else:
            encode += char
    return encode

'''
PROBLEM 1: ENCRYPTION  (5/5 points)
Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

Test Cases

>>> applyShift('This is a test.', 8)
'Bpqa qa i bmab.'
>>> applyShift('Bpqa qa i bmab.', 18)
'This is a test.'
'''

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))



'''
PROBLEM 2: DECRYPTION  (15/15 points)
Your friend, who is also taking 6.00.1x, is really excited about the program she wrote for Problem 1 of this problem set.
She sends you emails, but they're all encrypted with the Caesar cipher!

If you know which shift key she is using, then decrypting her message is an easy task.
If the string message is the encrypted message and k is the shift key she is using,
then calling applyShift(message, 26-k) returns her original message. Do you see why?

The problem is, you don't know which shift key she is using.
The good news is, you know your friend only speaks and writes English words.
So if you can write a program to find the decoding that produces the maximum number of real English words,
you can probably find the right decoding (there's always a chance that the shift may not be unique.
Accounting for this would use statistical methods that we won't require of you.)

PSEUDOCODE

Right now, you should take time to write some pseudocode!
Think about an algorithm you could use to solve this problem and write the steps down.
Then, you can verify your algorithm with the supplied pseudocode in ps6_pseudo.txt before coding.

After you've done writing and checking your pseudocode, implement findBestShift().
This function takes a wordList and a sample of encrypted text and attempts to find the shift that encoded the text.
A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words.
Note that this only means that most of the words obtained are actual words.
It is possible to have a message that can be decoded by two separate shifts into different sets of words.
While there are various strategies for deciding between ambiguous decryptions,
for this problem we are only looking for a simple solution.

To assist you in solving this problem, we have provided a helper function, isWord(wordList, word).
This simply determines if word is a valid word according to the wordList.
This function ignores capitalization and punctuation.
'''

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    best_shift_key = 0
    amt_matching_words = 0
    for search_key in range(26):
        amt_current_matching_words = 0
        decode_text = applyShift(text, search_key)
        decode_text_list = decode_text.split(' ')
        for search_word in decode_text_list:
            if isWord(wordList, search_word):
                amt_current_matching_words += 1
        if amt_current_matching_words > amt_matching_words:
            best_shift_key = search_key
            amt_matching_words = amt_current_matching_words
    return best_shift_key


'''
PROBLEM 2: DECRYPTION  (5/5 points)
Now that you have all the pieces to the puzzle,
please use them to decode the file story.txt.

In the skeleton file, you will see a method getStoryString() that will return the encrypted version of the story.
Fill in the following function; it should create the wordList, obtain the story,
and then decrypt the story.

Be sure you've read through the whole file to see what helper functions we've defined for you that may assist you in these tasks!
This function will be only a few lines of code
(our solution does it in 4 lines).
'''

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    crypto_text = getStoryString()
    word_list = loadWords()
    shift_key = findBestShift(word_list, crypto_text)
    return applyShift(crypto_text, shift_key)
