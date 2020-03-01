# 조건문+N진수 변환 방법을 해결

# 이게 빠름
def pow_custom(a,b,mod):
    res = 1
    while b:
        if b%2 == 1 : res = res*a%mod
        a = a*a%mod
        b//=2
    return res

# 매우 느림 -> 큰 수와 큰 수의 곱은 느리다
def pow_custom1(a,b,mod):
    res = 1
    while b:
        if b%2 == 1 : res = res*a
        a *=a
        b //= 2
    return res%mod

A, B, C = map(int,input().strip().split())
print(pow_custom(A,B,C))
