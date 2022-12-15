N = int(input())

table = [0]*N
total = 0

def checking(x):
    for i in range(x):
        if table[x] == table[i] or abs(table[x] - table[i]) == abs(x-i):
            return False
    return True

def tracking(x):
    global total
    if x == N:
        total += 1
        return
    else:
        for i in range(N):
            table[x] = i
            if checking(x):
                tracking(x+1)
tracking(0)
print(total)