class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1
        print(MemberCounter.members)


m1 = MemberCounter()
m1.init()

m2 = MemberCounter()
m2.init()

print(m1.members)
print(m2.members)


class sMemberCounter(MemberCounter):
    def init(self):
        print('init override ...', MemberCounter.members)


s1 = sMemberCounter()
s1.init()