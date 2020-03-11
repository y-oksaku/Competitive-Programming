ans = 0
for _ in range(3):
    s, e = map(int, input().split())
    ans += (s // 10) * e
print(ans)
