A, B, C = map(int, input().split())
ans = 0

D = [[], []]
D[A % 2].append(A)
D[B % 2].append(B)
D[C % 2].append(C)

D.sort(key=lambda a: len(a))

if len(D[-1]) == 2:
    ans += 1
    D[-1][0] += 1
    D[-1][1] += 1

    A, B, C = D[0][0], D[1][0], D[1][1]

mx = max(A, B, C)
ans += sum((mx - a) // 2 for a in (A, B, C))
print(ans)
