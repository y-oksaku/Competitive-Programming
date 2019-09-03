N = int(input())
W = input().replace('.', '')
W = W.split()

matching = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']

ans = 0
for m in matching:
    for w in W:
        if m == w:
            ans += 1

print(ans)