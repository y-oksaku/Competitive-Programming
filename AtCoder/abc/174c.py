K = int(input())

now = 7
r = 0
for d in range(1, K + 100):
    r = (r * 10 % K + 7) % K
    if r == 0:
        print(d)
        break
else:
    print(-1)
