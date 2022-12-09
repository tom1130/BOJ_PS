# 블랙잭
# 쌉 노가다 풀이
def blackJack():
    n, m = map(int, input().split())
    cards = list(map(int, input().strip().split()))
    res = 0
    for i in range(len(cards)-2):
        for j in range(i+1,len(cards)-1):
            for k in range(j+1,len(cards)):
                sum = cards[i]+cards[j]+cards[k]
                if sum==m:
                    return sum
                if sum<m and sum>res:
                    res = sum
    return res

print(blackJack())


