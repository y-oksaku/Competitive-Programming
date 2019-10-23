S = input()

for left in range(len(S) + 1):
    for right in range(len(S) + 1):
        T = list(S[:left]) + list(S[right:])
        if ''.join(T) == 'keyence':
            print('YES')
            exit()
print('NO')