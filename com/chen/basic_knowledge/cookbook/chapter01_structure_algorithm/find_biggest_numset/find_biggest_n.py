import heapq

# nlargest() / nsmallest()


nums = [1,2,3,4,5,6,7,8,9,10,11,100,20]

lagest = max(nums)
print(lagest)

x = heapq.nlargest(3,nums)
print(x)

y = heapq.nsmallest(3,nums)
print(y)


portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
print(cheap)



