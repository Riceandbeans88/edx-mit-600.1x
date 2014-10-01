def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    min_test = min(a,b)
    gcd = 1
    i = 1
    while (i <= min_test):
        if (a % i == 0 and b % i == 0):
            gcd = i
        i += 1
    return gcd

#print gcdIter(2, 12)    # = 2
#print gcdIter(6, 12)    # = 6
#print gcdIter(9, 12)    # = 3
#print gcdIter(17, 12)   # = 1


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

print gcdRecur(2, 12)    # = 2
print gcdRecur(6, 12)    # = 6
print gcdRecur(9, 12)    # = 3
print gcdRecur(17, 12)   # = 1

'''
A Java method that implements Euclid's algorithm is as follows:

   int gcd(int K, int M) {
      int k = K;   // In order to state a simple, elegant loop invariant,
      int m = M;   // we keep the formal arguments constant and use
                   // local variables to do the calculations.
      // loop invariant: GCD(K,M) = GCD(k,m)
      while (k != m) {
         if (k > m)
            { k = k-m; }
         else
            { m = m-k; }
      }
      // At this point, GCD(K,M) = GCD(k,m) = GCD(k,k) = k
      return k;
   }
'''


#Towers of Hanoi
def printMove(fr, to):
    print('move from' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print Towers(1, 'f', 't', 's')
