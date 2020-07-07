N = int(input())
S = input()

if S == 'b':
    print(0)
    exit()

T = 'b'
for i in range(1, 101):
    if i % 3 == 1:
        T = 'a' + T + 'c'
    if i % 3 == 2:
        T = 'c' + T + 'a'
    if i % 3 == 0:
        T = 'b' + T + 'b'

    if S == T:
        print(i)
        exit()

print(-1)
