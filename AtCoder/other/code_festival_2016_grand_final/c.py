N = int(input())
A = [int(input()) for _ in range(N)]

digits = set()

for a in A:
    digits.add((a & -a).bit_length() - 1)

xor = 0
for a in A:
    xor ^= a

ans = 0

for digit in range(xor.bit_length() + 1)[:: -1]:
    if (xor & (1 << digit)) > 0:
        if digit in digits:
            ans += 1
            xor ^= ((1 << (digit + 1)) - 1)
        else:
            print(-1)
            exit()

print(ans)