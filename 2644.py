# 촌수 계산

# 인접 행렬 혹은 인접 리스트를 활용할 수 있음

# 인접 리스트를 활용한 해법
from queue import Queue

def bfs():
    queue = Queue()
    queue.put(start)
    while queue.qsize()>0:
        q = queue.get()
        if q==end :
            return dist[end]
        for i in lst[q]:
            if dist[i]==0:
                queue.put(i)
                dist[i]+=dist[q]+1
    return -1

n = int(input())
start, end = map(int,input().split())
m = int(input())
lst = [[] for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
for _ in range(m):
    num1, num2 = map(int,input().split())
    lst[num2].append(num1)
    lst[num1].append(num2)

print(bfs())