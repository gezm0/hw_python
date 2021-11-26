# *args and **kwargs

#args here
#def dog_info(ownder, *dogs):
#    print(f"The owner of the dog is {ownder}")
#    for dog in dogs:
#        print(f"the dog is {dog}")


#dog_info('Petr', 'shepherd', 'aussie')


#kwargs here
def dog_info(ownder, **dogs):
    print(f"The owner of the dog is {ownder}")
    for dog, name in dogs.items():
        print(f"{name} is {dog}")


dog_info('Petr', shepherd='Grace', aussie='Meonia')