S = list(input())

ans = float('inf')
for i in range(len(S)) :
    n = int(''.join(S[i: i + 3]))
    ans = min(ans, abs(753 - n))

print(ans)