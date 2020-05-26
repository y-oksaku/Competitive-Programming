A = input()

if len(A) == 1:
    print(0)
    exit()

cnt = 0
for a, b in zip(A, A[::-1]):
    if a != b:
        cnt += 1

if cnt == 0 and len(A) % 2 == 1:
    print((len(A) - 1) * 25)
    exit()

if cnt != 2:
    print(len(A) * 25)
else:
    print(len(A) * 25 - cnt)
