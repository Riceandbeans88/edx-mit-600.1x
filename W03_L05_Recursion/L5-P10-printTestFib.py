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

testFib(10)

'''
fib of 0 = 1
fib called 1 times
fib of 1 = 1
fib called 1 times
fib of 2 = 2
fib called 3 times
fib of 3 = 3
fib called 5 times
fib of 4 = 5
fib called 9 times
fib of 5 = 8
fib called 15 times
fib of 6 = 13
fib called 25 times
fib of 7 = 21
fib called 41 times
fib of 8 = 34
fib called 67 times
fib of 9 = 55
fib called 109 times
fib of 10 = 89
fib called 177 times

'''
