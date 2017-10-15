class Calculator:
    def calc(self):
        while True:
            try :
                x= int(input("x = "))
                y = int(input("y = "))
                value = x/y
                print('\nvalue =',value)
            except (Exception) as e:
                print("\ninvalid input .Please try again")
                print("more info:\n\t",e)
            else:
                break
            finally:
                # value = None
                del value
                print('cleaning up...')
        raise Exception('too big')

x = Calculator()
try:
    x.calc()
except:
    print("too big get...")


