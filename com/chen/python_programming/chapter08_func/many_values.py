def ptNames(*name):
    for x in name:
        print(x, end=" ")


ptNames("x", "y", "z")

print()


def keyNames(value=1, **name):
    for x, y in name.items():
        print(x, ':', y)


keyNames(name='cc', info="i am programmer")

