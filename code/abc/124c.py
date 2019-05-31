S = input()

B = [] * len(S)
ans = 0

for i in range(len(S)) :
    if not int(S[i]) == (i%2) :
        ans += 1

ans = min(ans , len(S) - ans)

print(ans)