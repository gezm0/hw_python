# "Old Style" String Formatting

my_name = 'Bob'
her_name = 'Alice'

print('Zero')
print("Hi, %(she)s, let's go to cafe with %(me)s" %{"she": her_name, "me": my_name})

# "New Style" String Formatting

print('First')
print('Hi {}'.format(my_name))

print('Second')
print('Hi {}, this is {}'.format(her_name, my_name))

# if we don't assign names at right and don't fill curve brackets at left, then
# there will be assigning variables in their order

print('Third')
print('Hi {she}, this is {me}'.format(she=her_name,me=my_name))

# String Interpolation / f-String (since Python 3.6)
print('Forth')
print(f"Hi {her_name}, this is {my_name}")

# a few more variables

import random
time_evening = random.randrange(18,23)
time_morning = random.randrange(7,11)
print('Fifth')
print(f"Hi {her_name}, this is {my_name}.")
print(f"Would you meet me at {time_evening} this evening or have a breakfast {time_morning} tomorrow morning?")
