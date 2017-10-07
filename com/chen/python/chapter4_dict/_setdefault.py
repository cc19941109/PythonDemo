people = {
    'Alice': {
        'phone': '2341',
        'addr': 'foo drive 23'

    },
    'Beth': {
        'phone': '1234',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3281',
        'addr': 'Baz avenue 90'
    },
    'a': {
        'phone': '1233',
        'addr': 'Baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'addersss'
}

x = people.setdefault('cc')
print(x)

y = people.get('cc')
print(y)
print(people)

z = people['cc'] = 'world'
print(z)
print(people)

x = people.setdefault('cc', 'hello ...')
print(x)
print(people)

print(people['cc'])
