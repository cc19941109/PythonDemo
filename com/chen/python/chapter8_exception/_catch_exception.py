try:
    x=int(input("first num:"))
    y = int(input("second num:"))
    print(x/y)
except ZeroDivisionError:
    print("the second number can't be zero")

