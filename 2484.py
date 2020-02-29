lst_num = int(input())
# max_num = 0
def solve():
    lst = list(map(int, input().strip().split()))
    lst.sort()
    if len(set(lst))==1:
        return 50000+5000*lst[0]
    if len(set(lst))==2:
        if lst[1]==lst[2]: return 10000+1000*lst[1]
        return 2000+lst[1]*500+500*lst[2]
    for i in range(3):
        if lst[i]==lst[i+1]: return 1000+100*lst[i]
    return 100*lst[3]


# for _ in range(lst_num):
#     temp = list(map(int,input().strip().split()))
#     res = solve(temp)
#     if res>max_num:
#         max_num = res

print(max(solve() for i in range(lst_num)))