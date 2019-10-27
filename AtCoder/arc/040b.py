N, R = map(int, input().split())
S = list(input())

right = 0
for i, s in enumerate(S):
    if s == '.':
        right = i

if right == 0 and S[0] == 'o':
    print(0)
else:
    ans = 0
    for i, s in enumerate(S):
        if i + R - 1 >= right:
            ans += 1
            break
        if s == '.':
            for j in range(i, min(N, i + R)):
                S[j] = 'o'
            ans += 1
        if not '.' in S:
            break
        ans += 1

    print(ans)