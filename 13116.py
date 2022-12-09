test_case = int(input())

def findNum():
    m,n = map(int,input().split())
    while True:
        if m==n:
            return 10*n
        if m>n:
            m//=2
        else:
            n//=2
for _ in range(test_case):
    print(findNum())