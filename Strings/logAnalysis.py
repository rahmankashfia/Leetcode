ls = ["a1 9 2 3 1","g1 act coo","zo4 4 7","ab1 off key dog","a8 act coo"]
ld = []
la = []

for item in ls:
    temp = item.split(" ")
    if temp[1].isdigit():
        ld.append(temp)
    elif temp[1].isalpha():
        la.append(temp)

la = [" ".join(item) for item in la]
ld = [" ".join(item) for item in ld]
def sortSecond(val):
    i = val.index(" ") + 1
    return val[i:] + val[0:i-1]
la.sort(key = sortSecond)
la.extend(ld)
print(la)