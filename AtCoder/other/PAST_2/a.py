S = input()
T = input()

if S == T:
    print('same')
    exit()

if S.lower() == T.lower():
    print('case-insensitive')
    exit()

print('different')
