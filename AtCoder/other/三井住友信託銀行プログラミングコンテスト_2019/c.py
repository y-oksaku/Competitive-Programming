X = int(input())
m = X % 100

S = 0
for i in range(1, 6)[:: -1]:
    S += (100 + i) * (m // i)
    m -= m // i * i

if S > X:
    print('0')
else:
    print('1')
