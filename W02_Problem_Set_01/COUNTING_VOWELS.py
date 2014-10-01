__author__ = 'Aaron Echavarria'

'''
COUNTING VOWELS  (10/10 points)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

For problems such as these, do not include raw_input statements or define the variable s in any way.
Our automated testing will provide a value of s for you -
so the code you submit in the following box should assume s is already defined.
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

'''

sentence = s
count = 0
vowels = "aeiuoAEIOU"
for letter in sentence:
    if letter in vowels:
        count += 1

print"Number of vowels:", count