T = input()

N = T.count('N')
S = T.count('S')
W = T.count('W')
E = T.count('E')

if N > 0 and S == 0 or S > 0 and N == 0:
    print('No')
elif W > 0 and E == 0 or E > 0 and W == 0:
    print('No')
else:
    print('Yes')
