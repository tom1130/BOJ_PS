# 피보나치 수 5

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
N = int(input())
print(fibonacci(N))