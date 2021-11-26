# outer and inner functions

def sayhey(name):
    print(f"hey {name}")
    def inner_sayhey():
        print("I'm inner function")
    inner_sayhey()

sayhey('vv')

# we can't refer to inner functions on this level
# this cause an error

#inner_sayhey()