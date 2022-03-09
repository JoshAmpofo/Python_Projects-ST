"""Counting in a loop"""
# count = 0
# print('Before: ', count)
# for item in [9, 41, 12, 3, 74, 15]:
#    count = count + 1
#    print(count, item)
# print('After count: ', count)

# """Summing in a Loop"""
# sum = 0
# print('Before: ', sum)
# for item in [9, 41, 12, 3, 74, 15]:
#    sum = sum + item
#    print(sum, item)
# print('After sum: ', sum)

"""Average in a Loop"""
count = 0
sum = 0
print('Before: ', count, sum)
for item in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + item
    print(count, sum, item)
print('After counting and summing, Average: ', count, sum, sum/count)


