N = int(input())
A = list(map(int, input().split()))

negA = []
posA = []
for a in A:
    if a >= 0:
        posA.append(a)
    else:
        negA.append(a)

ans = sum(posA) - sum(negA)

if len(negA) % 2 == 1:
    ans -= min([abs(a) for a in A]) * 2

print(ans)
