# gcd

def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i

def gcdEuclidian(a,b):
    return b if a%b==0 else gcdEuclidian(b,a%b)

def lcm(a,b):
    return a*b//gcdEuclidian(a,b)

A,B = map(int,input().strip().split())
print(gcdEuclidian(A,B))
print(lcm(A,B))