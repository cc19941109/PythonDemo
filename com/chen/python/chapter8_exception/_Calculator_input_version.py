class Calculator:
    def culc(self):

        try:
            x = int(input("x = "))
            y = int(input("y = "))
            z = x / y
        except (ZeroDivisionError) as e:
            print("division by zero is illegal")
            print(e)
        except(ValueError) as e:
            print("please input number")
            print(e)
        except:
            print("An Unexpected Error Occurred")
        else:
            print("test success...")

        return z


x = Calculator()
z = x.culc()
print('\nresult =', z)
