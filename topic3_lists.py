# practice python topic 3
# lists

fruits = ['orange', 'apple', 'grape', 'melon', 'banana', 'pineapple', 'pear']

# prints all for selected list
print(fruits)

# prints only second item from list
print(fruits[1])

# prints only first item from the end of the list
# NOTICE! Normal count order starts from 0, but backward count order starts from -1
print(fruits[-1])

# print range as starts from
print(fruits[2:])
# print range as until
print(fruits[:4])

# items of the list can be changed
print('Unchanged list:')
print(fruits)
fruits[1] = 'grape'
fruits[2] = 'apple'
fruits[-1] = 'plum'
print('Changed list:')
print(fruits)

# insert as a 3'rd item of the list
fruits.insert(2, 'watermelon')
print(fruits)

# remove item by name from the list
fruits.remove('apple')
print(fruits)

# remove item by its number from the list
fruits.remove(fruits[1])
print(fruits)

# operations with lists

fruits1 = ['apple', 'orange', 'pear']
print (len(fruits1))

# iterative print
print('We have in our grocery:')
fruit_num = 1
for fruit in fruits:
    print(fruit_num, fruit)
    fruit_num += 1
print("Total:", (fruit_num)-1)

# sum
fruits_all = fruits + fruits1
print(fruits_all)
print('There are', len(fruits_all), 'fruits in grocery')

# longest (later) and shortest (earlier) item of the list

print("First item by alphabet is:", min(fruits_all))
print("Last item by alphabet is:", max(fruits_all))