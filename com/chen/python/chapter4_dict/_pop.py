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

labels = {
    'phone': 'phone number',
    'addr': 'addersss'
}


x  = people.pop('Alice')
print(x)
print(people)

y = labels.pop('phone')
print(y)
print(labels)
