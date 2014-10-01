__author__ = 'Aaron Echavarria'

'''
ALPHABETICAL SUBSTRINGS  (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or define the variable s in any way.
Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined.
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
'''

testingStr = s[0]
longStr = s[0]
for i in range(1, len(s)):
    if s[i] >= testingStr[-1]:
        testingStr += s[i]
        if len(testingStr) > len(longStr):
            longStr = testingStr
    else:
        testingStr = s[i]
print 'longStr substring in alphabetical order is:', longStr