A, B = map(int, input().split())

ans = 0
for i in range(A, B + 1):
    i = str(i)
    if all(s == t for s, t in zip(i, i[::-1])):
        ans += 1
print(ans)
