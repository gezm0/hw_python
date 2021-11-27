# Sets (arrays)
# set items are unordered, unchangeable and don't allow duplications

fruits = {'apple', 'banana', 'orange', 'pear'}
fruits1 = {'apple', 'banana', 'orange', 'pear'}

# Kinda HW. Compare arrays in loop and find if they are different
# I'm not sure it's works
# output result differ in serveral starts, but in one start output not differ 

#number = 0
#not_equal = 0

#while number < 10:
#    number+=1
#    if print(fruits) != print(fruits1):
#        print("I've found not equal output")
#        not_equal+=1
#    else:
#        continue
#print('Not equal outputs:', not_equal)

fruits1 = {'apple', 'banana', 'orange', 'pear', 'melon'}
print(fruits1.difference(fruits))

print(fruits1.intersection(fruits))
