# touples are immutable (you can't change tuples)
# touples are shorter than lists

# touple
topics1 = ('lists', 'tuples', 'dictionary')
print(topics1)
print('Size of tuple is', topics1.__sizeof__())

# list
topics2 = ['lists', 'tuples', 'dictionary']
print(topics2)
print('Size of list is', topics2.__sizeof__())

# tuples can be used as a key for dictionary

fruits = ('melon', 'orange')
print('Fist item -', fruits[0])
print(type(fruits))

#print("This won't work because of immute")
#fruits[0] = 'pear'

fruits1 = ('orange', 'melon')
print(fruits + fruits1)

# check for presence item in the tuple 
print('pear' in fruits)

for fruit in fruits:
    print(fruit)

# tuple methods are limited by count() and index()

fruits_all = fruits + fruits1
print('Whole list of tuple :)', fruits_all)
print('How much selected items we have in tuple:', fruits_all.count('orange'))
print('First appearance of selected item in tuple:', fruits_all.index('orange'))
