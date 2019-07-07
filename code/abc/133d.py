N = int(input())
A = list(map(int,input().split()))

ss = 0
for i in range(N) :
    ss += (-1)**i * A[i]

ans = []

for i in range(N) :
    ss = -ss + 2*A[i]
    ans.append(ss)

print('{} '.format(ans[-1]), end='')
ans.pop()

for a in ans :
    print('{} '.format(a), end='')
print('')