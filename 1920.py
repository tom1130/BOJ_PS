N = int(input())
A = list(map(int,input().split()))
M_length = int(input())
M = list(map(int,input().split()))

A.sort()

def binary_search_2(array, target, start ,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return 1
        if array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return 0

for i in range(M_length):
    print(binary_search_2(A, M[i], 0, N-1))
