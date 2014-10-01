def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    #while iterPower(base, exp) != exp
    ans = 1
    i = 1 
    while i <= exp: 
        ans = ans * base
        i += 1
    return ans