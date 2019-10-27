N = int(input())
S = input()
T = input()

for start in range(N):
    for s, t in zip(S[start:], T[: N - start]):
        if s != t:
            break
    else:
        print(N + start)
        break
else:
    print(2 * N)