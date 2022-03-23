txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))  # builds a tuple list where each tuple is a word preceded by its length

# compare first element, length first and only consider second element to break ties. Do this in reverse order
t.sort(reverse=True)

#  loop traversal. Builds list in reverse alphabetical order
res = list()
for length, word in t:
    res.append(word)

print(res)