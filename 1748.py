num = int(input())
num_length = len(str(num))
res = 0

for i in range(1,num_length):
    res += i*(10**i - 10**(i-1))
res += num_length*(num-10**(num_length-1)+1)
print(res)