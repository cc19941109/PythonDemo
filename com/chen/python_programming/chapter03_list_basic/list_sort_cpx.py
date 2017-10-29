a = [{'x': 3}, {'x': 6}, {'x': 2}]
a.sort(key=lambda d: d['x'])
print(a)

b = list("xa12.124xeqXQeE26")
b.sort(key=lambda x:x.upper())
print(b)

s = "dsd123"
# s = s.upper()
s = s.title()
print(s)




