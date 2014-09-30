def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    count = 0
    length = []
    length = aStr
    for i in length:
        count += 1
    return count


#aStr = "testTEST"

#print lenIter(aStr)

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == "":
        return 0
    else:
        return 1 + lenRecur(aStr[1: ])

aStr = "testTEST"
print lenRecur(aStr)



