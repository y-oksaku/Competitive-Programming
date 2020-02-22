A = int(input())
ans = A - 1

for x in range(1, A):
    y = A - x
    ans = max(ans, x * y)

print(ans)
