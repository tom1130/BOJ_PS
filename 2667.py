# 단지 번호 붙이기
N = int(input())
houses = [list(map(int,input())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
res_lst=list()
def dfs(x,y):
    global count
    count+=1
    houses[y][x]=-1
    for i in range(4):
        x_p=x+dx[i]
        y_p=y+dy[i]
        if x_p<0 or y_p<0 or x_p>=N or y_p>=N:
            continue
        if houses[y_p][x_p]==1:
            dfs(x_p,y_p)

for i in range(N):
    for j in range(N):
        if houses[i][j]==1:
            count = 0
            dfs(j,i)
            res_lst.append(count)
print(len(res_lst))
res_lst.sort()
for i in range(len(res_lst)):
    print(res_lst[i])