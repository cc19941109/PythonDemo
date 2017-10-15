while True:
    try:
        x = float(input("x = "))
        y = float(input('y = '))
    except:
        print('please input again')
    else:
        z = x+y
        print('result =',z)
        break

