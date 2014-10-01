def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_keys = []
    if aDict == {}:
        return 0
    else:
        max_value = max([len(e) for e in aDict.values()])
    for k, v in aDict.iteritems():
        if len(v) == max_value:
            max_keys.append(k)
    biggest = "".join(max_keys)
    return biggest




animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)

print animals