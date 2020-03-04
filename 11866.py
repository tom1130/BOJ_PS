from collections import deque

N, K = map(int, input().split())

dq = deque([i for i in range(1,N+1)])
res = list()

while len(dq)>0:
    # rotate 방향 생각해야함
    dq.rotate(-K+1)
    res.append(dq.popleft())
print('<{}>'.format(str(res)[1:-1]))