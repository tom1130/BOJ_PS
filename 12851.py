# 숨바꼭질 2
from collections import deque
max=100000
dis_lst = [0 for _ in range(max+1)]
N,K = map(int,input().split())
q = deque()
q.append(N)
count = 0
way =0
while way==0:
    length = len(q)
    for _ in range(length):
        x = q.popleft()
        if x == K:
            way += 1
        for dx in [x+1,x-1,x*2]:
            if  dx>max or dx<0 :
                continue
            elif dis_lst[dx]==0 or dis_lst[dx]==dis_lst[x]+1:
                q.append(dx)
                dis_lst[dx]=dis_lst[x]+1
    count +=1

print(count-1)
print(way)