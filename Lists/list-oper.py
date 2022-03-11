# """Concatenation"""
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)
# print(a)
# print(b)

# """list slicing"""
t = [9, 41, 12, 3, 74, 15]
t2 = [17, 45]
# print(t[1:3])
# print(t[::-1])

# """List Methods"""
# print(type(t))
# print(dir(t))
# t.extend(t2)  # takes a list as an argument and appends all the elements
# print(t)

# t.sort()  # arranges list elements from low to high
# print(t)

# """Deleting"""
# print(t.pop(1))  # used if you know the position of the element you want to delete
# pop() returns the element that was removed
# if no index is provided, pop deletes the last element in the list

# del t[1]  # used when the element/value is not needed
# print(t)

# t.remove(74)  # used when you know the element in the list but not the index
# print(t)
# to remove more than one element, use the list slicing method [:]

# """List Functions"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print('Max num:', max(nums))  # shout out the largest number in the list
print('Min num:', min(nums))
print('Total:', sum(nums))
avg = sum(nums)/len(nums)
print('Average:', avg)
