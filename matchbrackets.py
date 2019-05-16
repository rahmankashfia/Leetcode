def isValid(str) -> bool:
        if str == "" or len(str) % 2 == 1:
            return False
        else:
            i = 0
            ls = []
            while i != len(str):
                if str[i] == "(" or str[i] == "{" or str[i] == "[":
                   ls.append(str[i])
                   i = i + 1
                else:
                    if len(ls) > 0:
                        c = ls.pop()
                        print(c)
                        if (c == "(" and str[i] != ")") or (c == "{" and str[i] != "}") or (c == "[" and str[i] != "]"):
                            # return False]]j
                        i = i + 1
                        
            if len(ls) == 0:
                return True
            else:
                return False

print(isValid("[{}]"))
