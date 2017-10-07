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

if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'
else:
    print('input error .... please run again')

# locals().has_key('key')
if name in people and 'key' in dir() :
    print(name, "'s", labels[key], 'is', people[name][key])
elif 'key' in dir():
    print('name error ... please run again')


print(people)