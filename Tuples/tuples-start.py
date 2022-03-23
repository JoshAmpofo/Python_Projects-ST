# t = ('a', 'b', 'c', 'd')
# for item in t:
#     print(item)
# print(type(t))
# t = ('a',)  # creating a tuple with a single element. Take note of the 'comma' after the string
# print(type(t))
# t = ('a')
# print(type(t))
# t = tuple()  # creating an empty tuple
# print(t)
# t = tuple('lupins')  # prints out elements of the string
# print(t)

# dna = ('a', 'g', 't', 'c')
# print(dna[0])  # indexing can be performed on tuples
# print(dna[1:3])  # slicing

#  tuple elements cannot be modified but you can replace one tuple with another
# dna = ('A',) + dna[:-1]
# print(dna)

"""Comparing Tuples"""
# g = (0, 1, 2) < (0, 3, 4)
# print(g)
# g = (0, 1, 2000000) > (0, 3, 4)
# print(g)


t = tuple()
print(dir(t))  # methods of tuples are only index and count
