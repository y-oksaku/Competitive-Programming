S = input()
N = len(S)

if S[0] != '1' or S[-1] != '0':
    print(-1)
    exit()

for s, t in zip(S[: N - 1], S[:: -1][1:]):
    if s != t:
        print('-1')
        exit()

now = 1
branch = N
ans = []
for s in S[: N - 1]:
    if s == '1':
        ans.append('{} {}'.format(now, now + 1))
        now += 1
    else:
        ans.append('{} {}'.format(now, branch))
        branch -= 1

print(*ans, sep='\n')