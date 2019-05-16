def getIndexFrmDic(di, item):
    lt = di.pop(item)
    temp = lt.pop(0)
    return temp, lt


def twoSum(nums, target):
    d = dict()
    r = list()
    for i in range(len(nums)):
        if nums[i] in d:
            lt = list()
            lt = d.get(nums[i])
            lt.append(i)
            d.update({nums[i]: lt})
        else:
            d.update({nums[i]: [i]})
    print(d)
    for i in nums:
        temp = target - i
        if temp in d:
            tempidx, lt = getIndexFrmDic(d, i)
            r.append(tempidx)
            if len(lt) > 0:
                d.update({i: lt})
            tempidx, lt = getIndexFrmDic(d, temp)
            r.append(tempidx)
            if len(lt) > 0:
                d.update({temp: l
            return r
    return

nums = [3, 3, 2, 2, 2]
target = 5
print(twoSum(nums, target))


