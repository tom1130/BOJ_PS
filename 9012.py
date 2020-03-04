# 스택 괄호 지우기
T = int(input())

def checkPS():
    ps = input()
    res = list()
    index = -1
    for p in ps:
        res.append(p)
        index+=1
        if len(res)>=2 and res[index]==')' and res[index-1]=='(':
            res.pop()
            res.pop()
            index-=2
    if len(res)>0:
        return 'NO'
    return 'YES'

for _ in range(T):
    print(checkPS())