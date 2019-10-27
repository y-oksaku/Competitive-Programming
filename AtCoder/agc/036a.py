S = int(input())
MOD = 10**9

y2 = -(-S // 10**9)
x2 = -(S - y2 * (10**9))

print('0 0 {} 1 {} {}'.format(MOD, x2, y2))