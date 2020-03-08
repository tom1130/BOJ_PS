# 좋은 단어 찾기
def goodWord():
    word = input()
    lst = []
    for c in word:
        if len(lst)==0:
            lst.append(c)
        elif c =='A' and lst[-1]=='A':
            lst.pop()
        elif c=='B' and lst[-1]=='B':
            lst.pop()
        else: lst.append(c)
    return True if len(lst)==0 else False

N = int(input())
res = 0
for _ in range(N):
    if goodWord():
        res+=1
print(res)