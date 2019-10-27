N = int(input())

for p in range(2, min(N, int(N**2) + 10)):
    if N % p == 0:
        print('NO')
        break
else:
    print('YES')