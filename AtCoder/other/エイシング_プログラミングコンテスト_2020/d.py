N = int(input())
X = input()

cnt = X.count('1')
if cnt == 1:
    for x in X[:-1]:
        if x == '0':
            print(1)
        else:
            print(0)
    if X[-1] == '1':
        print(0)
    else:
        print(2)
    exit()

M = 0
for x in X:
    M <<= 1
    if x == '1':
        M += 1

def solve(n):
    ret = 1
    while n > 0:
        ret += 1
        n %= bin(n).count('1')
    return ret

ans = []
p = M % (cnt + 1)
m = M % (cnt - 1)

for i in range(N):
    if X[i] == '0':
        ans.append(solve((p + pow(2, N - i - 1, cnt + 1)) % (cnt + 1)))
    else:
        ans.append(solve((m - pow(2, N - i - 1, cnt - 1)) % (cnt - 1)))
print(*ans, sep='\n')
