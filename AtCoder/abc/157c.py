N, M = map(int, input().split())

ans = [-1] * N

for _ in range(M):
    s, i = map(int, input().split())
    s -= 1
    if ans[s] != -1 and ans[s] != i:
        print(-1)
        exit()
    ans[s] = i

if N > 1 and ans[0] == -1:
    ans[0] = 1

for i in range(N):
    if ans[i] == -1:
        ans[i] = 0

ans = int(''.join(map(str, ans)))

if len(str(ans)) != N:
    print(-1)
    exit()

print(ans)