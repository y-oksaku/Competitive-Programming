S = input()

if S == ''.join(['hi'] * (len(S) // 2)):
    print('Yes')
else:
    print('No')
