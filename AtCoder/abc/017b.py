S = input()

for s in ['ch', 'o', 'k', 'u']:
    S = S.replace(s, '')

print('YES' if S == '' else 'NO')
