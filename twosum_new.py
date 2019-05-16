def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            d[num].append(i)
        else:
            d[num] = [i]

    for i in nums:
        temp = target - i
        if temp == i:
            if len(d[temp]) > 1:
                r = d[temp][0:2]
                return r
        else:
            if temp in d:
                r = [d[i][0], d[temp][0]]
                return r
    return

nums = [3, 2, 4, 3, 2]
target = 6
print(twoSum(nums, target))
print(twoSum(nums, 7))
print(twoSum(nums, 8))
print(twoSum(nums, 4))
