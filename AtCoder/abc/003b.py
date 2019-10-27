S = input()
T = input()
at = set(list('atcoder@'))

for s, t in zip(S, T):
    if s == '@' or t == '@':
        if s in at and t in at:
            continue
        else:
            print('You will lose')
            break
    if s != t:
        print('You will lose')
        break
else:
    print('You can win')