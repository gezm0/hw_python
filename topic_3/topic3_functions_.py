# functions continue

#def greetings(name, m_text):
#    print(f"Hey {name}, {m_text}")

#greetings(m_text="let's go for cofe", name='Masha')

def greetings(*name):
    for name in names:
        print(f"Hey {name}")

names = ['Masha', 'Misha', 'Petya', 'Vova']
greetings(names)

