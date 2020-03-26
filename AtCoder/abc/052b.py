_ = int(input())

x = 0
ans = 0
for s in input():
    x += 1 if s == 'I' else -1
    ans = max(x, ans)
print(ans)