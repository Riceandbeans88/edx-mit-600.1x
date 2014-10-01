listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA.sort
print listA
listA.sort()
print listA
listA.insert(0, 100)
print listA
listA.insert(0, 100)
print listA
listA.remove(3)
print listA
listA.append(7)
print listA
listA + listB
print listA
listB.sort()
print listB
listB.pop()
print listB
listB.remove('a')
print listB



'''

[1, 4, 3, 0]
[0, 1, 3, 4]
[100, 0, 1, 3, 4]
[100, 100, 0, 1, 3, 4]
[100, 100, 0, 1, 4]
[100, 100, 0, 1, 4, 7]
[100, 100, 0, 1, 4, 7]
['q', 't', 'x', 'z']
['q', 't', 'x']
['q', 't', 'x']
[100, 100, 0, 1, 4, 7, 4, 1, 6, 3, 4]
[100, 100, 0, 1, 4, 7, 4, 1, 6, 3, 4]
[100, 100, 0, 1, 4, 7, 4, 1, 6, 3, 4]
[100, 100, 0, 1, 7, 4, 1, 6, 3, 4]
[4, 3, 6, 1, 4, 7, 1, 0, 100, 100]
'''


