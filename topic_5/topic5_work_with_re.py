# working with regular expressions

import re

emails = '''
test@gmail.com
test@mail.ru
test1234@epam.com
'''

pattern = re.compile(r'[0-9a-zA-Z_.-]+@[a-zA-Z_.-]+\.[a-zA-Z]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

