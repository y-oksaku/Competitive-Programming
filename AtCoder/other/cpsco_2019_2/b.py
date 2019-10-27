N = int(input())
ans = 0
prd = 1

for _ in range(N):
    c, a = input().split()
    a = int(a)

    if c == '-' or a == 0:
        continue

    if c == '+':
        ans += a
    if c == '*':
        prd *= a

print(ans * prd)