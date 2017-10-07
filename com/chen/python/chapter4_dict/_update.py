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


d = {'a':123}
people.update(d)
print(people)

e = [('a',321)]
people.update(e)
print(people)

f = ()
people.update(f)
print(people)


