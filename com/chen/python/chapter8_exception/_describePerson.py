def describePerson(person):
    print('Description of ',person['Name'])
    print('Age:',person['Age'])
    try:
        print('Occupation:',person['Occupation'])
    except KeyError as e:
        pass


person ={'Name':'cc','Age':18}
describePerson(person)

print('\n')

person ={'Name':'cc','Age':18,'Occupation':'Engineer'}

describePerson(person)


