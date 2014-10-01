def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')
testFib(10)
#slide Source
'''
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    for i in range(n+1):
        global numCalls #<------
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')
'''

'''
fib of 0 = 1
fib called 1 times
fib of 1 = 1
fib called 2 times
fib of 2 = 2
fib called 5 times
fib of 3 = 3
fib called 10 times
fib of 4 = 5
fib called 19 times
fib of 5 = 8
fib called 34 times
fib of 6 = 13
fib called 59 times
fib of 7 = 21
fib called 100 times
fib of 8 = 34
fib called 167 times
fib of 9 = 55
fib called 276 times
fib of 10 = 89
fib called 453 times
'''

#When numCall is commented out in testFib()
'''
fib of 0 = 1
fib called 1 times
fib of 1 = 1
fib called 2 times
fib of 2 = 2
fib called 5 times
fib of 3 = 3
fib called 10 times
fib of 4 = 5
fib called 19 times
fib of 5 = 8
fib called 34 times
fib of 6 = 13
fib called 59 times
fib of 7 = 21
fib called 100 times
fib of 8 = 34
fib called 167 times
fib of 9 = 55
fib called 276 times
fib of 10 = 89
fib called 453 times
'''

'''
fib of 0 = 1
fib called 0 times
fib of 1 = 1
fib called 0 times
fib of 2 = 2
fib called 0 times
fib of 3 = 3
fib called 0 times
fib of 4 = 5
fib called 0 times
fib of 5 = 8
fib called 0 times
fib of 6 = 13
fib called 0 times
fib of 7 = 21
fib called 0 times
fib of 8 = 34
fib called 0 times
fib of 9 = 55
fib called 0 times
fib of 10 = 89
fib called 0 times
fib of 11 = 144
fib called 0 times
fib of 12 = 233
fib called 0 times
fib of 13 = 377
fib called 0 times
fib of 14 = 610
fib called 0 times
fib of 15 = 987
fib called 0 times
fib of 16 = 1597
fib called 0 times
fib of 17 = 2584
fib called 0 times
fib of 18 = 4181
fib called 0 times
fib of 19 = 6765
fib called 0 times
fib of 20 = 10946
fib called 0 times
'''

