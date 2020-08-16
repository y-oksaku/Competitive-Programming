N = int(input())
ans = ''

if N < 100:
    ans = '00'

if 100 <= N <= 5000:
    ans = '%02d' % (N // 100)

if 6000 <= N <= 30000:
    ans = str(N // 1000 + 50)

if 35000 <= N <= 70000:
    ans = str((N // 1000 - 30) // 5 + 80)

if N > 70000:
    ans = '89'

print(ans)
