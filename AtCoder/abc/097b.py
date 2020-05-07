X = int(input())

ans = 0
for b in range(1, 1001):
    for p in range(2, 10):
        if pow(b, p) <= X:
            ans = max(ans, pow(b, p))
print(ans)
