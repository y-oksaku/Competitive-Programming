ans = 0
V = set()
for _ in range(int(input())):
    a = input()
    if a in V:
        ans += 1
    V.add(a)
print(ans)
