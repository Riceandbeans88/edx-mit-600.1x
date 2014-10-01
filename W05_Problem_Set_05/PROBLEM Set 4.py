__author__ = 'AE'

'''
Big O
'''

def modten(n):
    return n%10

#4.1
#O()

def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result

#4.2
#O()

def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)

#4.3
#O()

def baz(n):
    for i in range(n):
        for j in range(n):
            print i,j

#4.4
#O()