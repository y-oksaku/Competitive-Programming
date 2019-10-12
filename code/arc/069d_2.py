N = int(input())
S = [1 if s == 'o' else -1 for s in input()]

for first in [1, -1]:
    for second in [1, -1]:
        ans = [first, second]
        prev = first
        now = second
        for s in S[1:] + [S[0]]:
            if s == 1:
                if now == 1:
                    prev, now = now, prev
                else:
                    prev, now = now, -prev
            else:
                if now == 1:
                    prev, now = now, -prev
                else:
                    prev, now = now, prev
            ans.append(now)
        if first == ans[-2] and second == ans[-1]:
            print(*['S' if a == 1 else 'W' for a in ans[:-2]], sep='')
            exit()

print(-1)