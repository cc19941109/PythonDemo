import heapq

nums = [1,2,-1,3,4,5,6,7,8,9,10,11,100,20]

lagest = max(nums)
print(lagest)


# or :
heap = list(nums)
x = heapq.heapify(heap)
print(x)

print(heapq.heappop(heap))

# 1. 找到最大的元素: max / min
# 2. 在 n 个元素中 找到最大的x个元素, 当 x 较小时:  nsmallest ,nlargest
#                                  当 x 接近 n: 排序切片
#  不管怎么样,  nsmallest ,nlargest 会做优化,你用就行了
