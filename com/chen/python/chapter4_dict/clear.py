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
    }
}

print("%(Alice)s"%people)

s = people.clear()
print(people)
print('s',s)