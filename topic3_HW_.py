# More complicated variant

print('')

m_whom = [
    '"Masha Mashina" <masha@yandex.ru>', 
    '"Misha Mishin" <misha@yandex.ru>', 
    '"Petya Petin" <petya@yandex.ru>', 
    '"Vova Vovin" <vova@yandex.ru>'
    ]
m_who = '"Santa Claus" <santa@north.pole>'
m_subj = 'Merry Christmas and the Happy New Year!'
m_body = '''Hello dear friend! 
Your behaviour last year was very badly. 
So, no presents this New Year. 
Sorry.'''
m_bottom = '''Best wishes, 
yours Santa.'''

def write_a_message(m_who, name, m_subj, m_body, m_bottom):
    for name in m_whom:
        print(f"From: {m_who}")
        print(f"To: {name}")
        print(f"Subject: {m_subj}")
        print('')
        print(m_body)
        print('')
        print(m_bottom)
        print('')
        print('=== cut here ===')
        print('')

write_a_message(m_who, m_whom, m_subj, m_body, m_bottom)
