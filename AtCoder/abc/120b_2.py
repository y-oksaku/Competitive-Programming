A, B, K = map(int, input().split())

ans = []
for i in range(1, 1000):
    if A % i == 0 and B % i == 0:
        ans.append(i)

ans.sort(reverse=True)
print(ans[K - 1])
