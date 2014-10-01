def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count

'''
Test Suite A:
 foo(2, 5),
 foo(5, 6),
 foo(9, 7)
Test A1 results X < A: 0
Test A2 results X < A: 0
Test A3 results X > A: 1

Winner!
Test Suite B:
 foo(10, 3),
 foo(1, 4),
 foo(10, 6)
Test B1 results X > A: 3
Test B2 results X < A: 0
Test B3 results X > A: 1

Test Suite C:
 foo(100, 5),
 foo(96, 5),
 foo(22, 5)
Test C1 results X > A: 20
Test C2 results X > A: 19
Test C3 results X > A: 4
'''

print "Test C1 results:", foo(100, 5)
print "Test C2 results:", foo(96, 5)
print "Test C3 results:", foo(22, 5)

