N = int(input())
S, T = input().split()

for s, t in zip(S, T):
    print('{}{}'.format(s, t), end='')
print('')