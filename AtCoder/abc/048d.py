S = input()

if S[0] == S[-1]:
    print('First' if len(S) % 2 == 0 else 'Second')
else:
    print('First' if len(S) % 2 == 1 else 'Second')
