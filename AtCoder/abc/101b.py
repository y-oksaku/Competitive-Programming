N = input()
S = sum(map(int, N))

print('Yes' if int(N) % S == 0 else 'No')
