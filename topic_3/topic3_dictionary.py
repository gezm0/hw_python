# Dictionaries (changeable, no duplicates)
# They are used to store data values in key:value

# since python 3.7 dictionaries are ordered

# no duplicates
car = {'brand':'Ford', 'brand':'BMW'}
print(car)

car = {'brand':'Ford', 'model':'Focus', 'color':'Black', 'year':2021}
print(car)
print('Brand:', car['brand'])
print('I have', car['brand'], 'and its color is', car['color'])
print(f"Hi Misha, I bought a new {car['year']}'s {car['brand']} {car['model']}")

# print dictionary keys and values
# as output we get lists
print('We have those', car.keys())
print('We have those', car.values())

# we can change something and print it with method get
car['color'] = 'Red'
print(car['color'])
print(car.get('color'))

# keys could be integers, strings or tuples (immutable)
# but not lists (mutable)
