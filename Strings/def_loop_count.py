def counter(word):
    """This function takes a word a counts the number of specified letters in the word"""
    word = word
    count = 0
    for char in word:
        if char == 'a':
            count = count + 1
    return count


print(counter('apple'))
# For some reason, the function is unable to return a value for the letter if not specified in the code
