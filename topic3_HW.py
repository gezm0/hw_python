print('3. Create functions')

print("Here i'm creating my function...")

def print_em():
    print('')

print('and using it')
print_em()

print('1. Create a shopping list')
print_em()
shopping_list = ['Milk', 'Bread', 'Eggs', 'Spaghetty', 'Butter', 'Olive oil']
number_item = 0

print('My shopping list:')
for item_of_list in shopping_list:
    number_item+=1
    print(f"{number_item}). {item_of_list}")

print_em()
print('2. Explain something with dictionary')
print_em()
phone = {'brand':'Apple', 'model':'iPhone 11', 'color':'red', 'memory':'128 Gb', 'date':'April'}
print(f"I bought myself in {phone['date']} new {phone['color']} {phone['brand']} {phone['model']} with {phone['memory']} onboard")

print_em()
print('4. Try to work with exceptions')
print_em()
print('Calculator for dividing')

while True:
    
    try:
        x = int(input("Please enter first number:  "))
    except ValueError:
        print("It's not number")
    try:
        y = int(input("Please enter second number: "))
    except ValueError:
        print("It's not number")
        break

    try:
        z = x / y
    except ZeroDivisionError:
        print("You can't divide by zero!")
        break
    print('Result is', z)
    break