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
        print('i')
        print(i)
        temp = target - i
        if temp in d:
            lt = d.pop(i)
            if i == temp and len(lt) == 1:
                continue
            r.append(lt.pop(0))
            if len(lt) > 0:
                d.update({i: lt})
            print('d')
            print(d)
            print('r')
            print(r)
           
            lt = d.pop(temp)
            r.append(lt.pop(0))
            if len(lt) > 0:
                d.update({temp: lt})
            print(d)
            print(r)

            return r
    return

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))


