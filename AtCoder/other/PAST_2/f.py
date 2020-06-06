N = int(input())
A = [set(list(input())) for _ in range(N)]

ans = []
for i, a in enumerate(A):
    b = A[-(i + 1)]
    A[i] = a & b

ans = []
for a in A:
    if len(a) == 0:
        break
    ans.append(list(a)[0])
else:
    print(''.join(ans))
    exit()

print(-1)
