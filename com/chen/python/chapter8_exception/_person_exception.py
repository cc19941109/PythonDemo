class personException(Exception):
    def report(self):
        print("personal Exception occured")
    def __init__(self,value):
        self.value = value

try:
    raise personException('.test success..')
except personException as e:
    e.report()
    print(e)
