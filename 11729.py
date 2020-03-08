# 하노이 탑 이동 순서 -> 재귀

N = int(input())
def hanoi(start,end,sz):
    if sz==1 : return print(start,end)
    hanoi(start,6-start-end,sz-1)
    print(start,end)
    hanoi(6-start-end,end,sz-1)

print(2**N-1)
hanoi(1,3,N)