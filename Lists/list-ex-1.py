def chop(t):
    del t[0], t[-1]
    return None


def middle(t):
    return t[1:-1]


letters = ['a', 'b', 'c', 'd', 'e']
print(middle(letters))
