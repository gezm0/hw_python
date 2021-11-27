# Functions

def greetings(name):
    print(f"Hello {name}!")

greetings('Misha')

# return
def greetings(name):
    hey = (f"Hello {name}!")
    return hey

print(greetings('Masha'))

# with list
def greetings(name):
    print(f"Hello {name}!")

names = ['Masha', 'Misha']

for name in names:
    greetings(name)

# default value
def greetings(name='Vasya'):
    print(f"Hello {name}!")

greetings()

