N = int(input())
ans = set()
for i in range(1, N + 1):
    j = N - i
    if i == j or i == 0 or j == 0:
        continue
    ans.add((min(i, j), max(i, j)))
print(len(ans))