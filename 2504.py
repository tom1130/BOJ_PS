# ()[] 점수 계산

ps = input()
def getNum(ps):
    lst = list()
    res = 0
    for p in ps:
        if len(lst)==0:
            lst.append(p)
            continue
        elif type(lst[-1]) == int:
            if len(lst)>=2 and type(lst[-2]) == int:
                temp_num=lst.pop()+lst.pop()
                lst.append(temp_num)
        if p==')':
            if lst[-1]=='(':
                lst.pop()
                lst.append(2)
            elif type(lst[-1]) == int :
                if len(lst)>=2 and lst[-2]=='(':
                    temp_num = lst.pop()
                    lst.pop()
                    lst.append(temp_num*2)
                else: lst.append(p)
        elif p==']':
            if lst[-1]=='[':
                lst.pop()
                lst.append(3)
            elif type(lst[-1]) == int :
                if len(lst)>=2 and lst[-2]=='[':
                    temp_num = lst.pop()
                    lst.pop()
                    lst.append(temp_num*3)
                else: lst.append(p)
        else:
            lst.append(p)
    for l in lst:
        if type(l)==int:
            res+=l
        else:
            return 0
    return res

print(getNum(ps))