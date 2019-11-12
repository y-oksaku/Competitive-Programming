import string
H, W = map(int, input().split())
ans = ''

for h in range(1, H + 1):
    line = input().split()
    for w, s in zip(string.ascii_uppercase[:W], line):
        if s == 'snuke':
            ans = '{}{}'.format(w, h)

print(ans)
