N = int(input())
S = input()
base = ord('A')

ans = []
for s in S:
    a = ord(s) - base
    ans.append(chr((a + N) % 26 + base))
print(''.join(ans))