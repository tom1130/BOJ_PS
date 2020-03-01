# 소수(에라토스테네스의 체)

M ,N = map(int, input().strip().split())

lst = [False for _ in range(N+1)]
res = []
for i in range(2,N+1):
     if lst[i]==True:continue
     res.append(i)
     for j in range(i*i,N+1,i):
         lst[j]=True

for num in res:
    if num>=M:
        print(num)