# Errors and exceptions

while True:
    try:
        x = int(input("Please provide number 1:  "))
    except ValueError:
        print("It's not number")
    try:
        y = int(input("Please provide number 2:  "))
    except ValueError:
        print("It's not number")
        break

    z = x + y
    print(z)
    break