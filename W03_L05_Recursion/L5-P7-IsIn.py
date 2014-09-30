def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Base Cases
    length = len(aStr)
    if aStr == '':
        return False
    elif length == 1:
        return False
    # Recursive Cases
    midChar = aStr[length/2]

    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:length / 2])
    elif char > midChar:
        return isIn(char, aStr[length / 2:])



testStr = "a"
char = "aString"

print isIn("a", 'aaaaaa')
