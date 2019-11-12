N = int(input())
K = 1
while (K * (K + 1) // 2) < N:
    K += 1
ans = []
for k in range(1, K + 1)[:: -1]:
    if N >= k:
        ans.append(k)
        N -= k
print(*ans, sep='\n')