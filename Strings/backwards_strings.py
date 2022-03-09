# using for loop to iterate backwards
fruit = 'banana'
index = 0
for char in fruit:
    if index < len(fruit):
        char = fruit[index - 1]
        index -= 1
    print(char)  # for loop works perfectly and doesn't give any throwbacks
