N = int(input())
B = []
R = []

for _ in range(N):
    x, c = input().split()
    x = int(x)
    if c == 'R':
        R.append(x)
    else:
        B.append(x)

B.sort(reverse=True)
R.sort(reverse=True)

while R:
    print(R.pop())
while B:
    print(B.pop())

