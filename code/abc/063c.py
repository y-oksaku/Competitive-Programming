N = int(input())

score = []
ans = 0
for _ in range(N):
    s = int(input())
    ans += s
    score.append(s)

if ans % 10 == 0:
    score.sort()
    for s in score:
        if s % 10 != 0:
            ans -= s
            break
    else:
        ans = 0

print(ans)