S = input()
T = input()

ans = 10**18
for l in range(len(S) - len(T) + 1):
    cnt = 0
    for s, t in zip(S[l:], T):
        if s != t:
            cnt += 1
    ans = min(ans, cnt)

print(ans)
