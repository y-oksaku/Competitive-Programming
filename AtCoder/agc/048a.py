def solve():
    S = input()

    if S.count('a') == len(S):
        print(-1)
        return

    if S > 'atcoder':
        print(0)
        return

    for i, s in enumerate(S):
        if s > 'a':
            print(i - (1 if s > 't' else 0))
            return

T = int(input())
for _ in range(T):
    solve()
