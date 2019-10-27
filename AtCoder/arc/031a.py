S = input()
for s, t in zip(S, reversed(S)):
    if s != t:
        print('NO')
        break
else:
    print('YES')
