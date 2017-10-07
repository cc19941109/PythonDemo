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

name = input('Name: ')

request = input('phone(p) or address(a)?: ')

key = request
if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print(name, "'s", label, result)
