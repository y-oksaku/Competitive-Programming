A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for gohyaku in range(A + 1):
    for hyaku in range(B + 1):
        for goju in range(C + 1):
            if gohyaku * 500 + hyaku * 100 + goju * 50 == X:
                ans += 1
print(ans)
