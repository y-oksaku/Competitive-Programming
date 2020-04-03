N, M = map(int, input().split())
SC = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(10**N):
    i = str(i)
    if len(i) != N:
        continue
    for s, c in SC:
        if len(i) < s:
            break
        if i[s - 1] != str(c):
            break
    else:
        print(i)
        exit()

print(-1)
