animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
print animals
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    #return sum(someDictionary.values())
    return len([i for make_flat_list in aDict.values() for i in make_flat_list])

print animals
print howMany(animals)
#below is adding the amount of keys
print "Length : %d" % len(animals)
print len(animals.values())

def howMany2(aDict):
    list_of_lists = aDict
    for x in list_of_lists:
        for y in x:
            aDict.append(y)

    return len(aDict)

listValues = []
listKeys = []
listValues = animals.values()
listKeys = animals.keys()
print ("list values", listValues)
print ("list keys", listKeys)




def howMany3(aDict):
    flatList = aDict.values()
    return len(reduce(lambda x,y:x+y,flatList))

print howMany3(animals)



x = [1, 2, [3, 'John', 4], 'Hi']

print range(3)
print range(3, 10)
print range(3, 10, 3)
#print range(3, 10.5, 0.5)
print range(10, 3)
print range(10, 3, -1)
print range(len(x))
print sum(range(len(x)))

