def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n #return 1
   else:
      return n * f(n-1)

