# setting variables
a = 821
b = 621

# comparing variables
#if a > b:
#    print('a > b')
#elif a == b:
#    print('a == b')
#else:
#    print('a < b')

#if a <= b:
#    print('a <= b')
#    if a == b:
#        print('a == b')
#else:
#    print('a >= b')

#list_num = [1, 2, 4, 6, 10]
#for nums in list_num:
#    print(nums)

#for x in range(2,12,3):
#    print(x)

#number = 0
#while number <= 10:
#    print(number)
#    number+=1

#number = 0
#while True:
#    print(number)
#    number+=1
#    if number >= 5:
#        break

#for x in range(10):
#    if x % 2 == 0:
#        continue
#    print(x)

#fruits = ['apple', 'orange', 'melon', 'pear']
#fruit = 'date'

#if fruit in fruits:
#    print('yes')
#else:
#    print('no')

fruits1 = ['apple', 'orange', 'melon', 'pear']
fruits2 = ['apple', 'orange', 'melon']
fruits3 = fruits1

print(fruits1)
print(fruits2)
print(fruits3)

if fruits1 is fruits2:
    print('fruit1 the same as fruit2')
else:
    print('fruit1 NOT the same as fruit2')
if fruits1 is fruits3:
    print('fruit1 is the same as fruit3')
else:
    print('fruit1 is NOT the same as fruit3')