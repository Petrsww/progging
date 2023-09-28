nums = list(map(int, input().split()))
obj = [i for i in nums if nums.count(i) == 1]
print(*obj)
