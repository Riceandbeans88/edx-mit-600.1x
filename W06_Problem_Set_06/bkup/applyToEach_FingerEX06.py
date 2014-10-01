
L = []


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

#you are counting from teh assumed array from 0
#fn should be simple and independent
def ifEven(inputList):
    for i in range(len(inputList)):
        if i % 2 == 0:
            inputList[i] = inputList[i] * -1
    return inputList

testList = [1, -4, 8, -9]
# Given => testList = [1, -4, 8, -9]
# run abs() make so much more sense
# Goal
# print testList
# [1, 4, 8, 9]


print applyToEach(testList, abs())
