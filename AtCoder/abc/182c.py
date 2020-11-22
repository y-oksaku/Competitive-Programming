S = input()
N = len(S)

ans = 10**18
for state in range(1, 1 << N):
    T = [s for i, s in enumerate(S) if (state & (1 << i)) != 0]
    if sum(map(int, T)) % 3 == 0:
        ans = min(ans, N - len(T))
print(ans if ans < 10**18 else -1)
