from itertools import combinations, permutations

def genList(s):
    r = list()
    rl = list()
    for i in range(len(s)):
        for j in range(0, len(s)):
            sl = list(s)
            temp = sl.pop(i)
            sl.insert(j, temp)
            #print("{} {}".format(temp, sl))
            if sl not in rl:
                rl.append(sl)
                r.append("".join(sl))
    for i in range(len(r)):
        temp = "".join(reversed(r[i]))
        #print(temp)
        if temp not in r:
            r.append(temp)
    return r

def test(sample, result):
    if(len(sample) != 0 or len(result) != 0):
        print("sample {}".format(sample))
        print("result {}".format(result))
        print(set(sample).difference(set(result)))
        r = list()
        r = result
        for i in range(len(sample)):
            if sample[i] in r:
                continue
            else:
                print("1Failed")
                return False
        print("Success")
    else:
        print("2Failed")

def test2(s):
    rr = list()
    sll = list(s)
    comb = permutations(sll, 4)
    for i in list(comb):
        #print(i)
        rr.append("".join(i))
    #print(rr)
    return rr

r = genList("abcd")
sample = test2("abcd") 
test(sample, r)
