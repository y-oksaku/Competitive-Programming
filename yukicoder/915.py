Q = int(input())

ans = []
for _ in range(Q):
    A, B, C = map(int, input().split())
    if C == 1:
        ans.append(-1)
        continue

    cnt = 0
    digits = []
    while A > 0:
        digits.append(A % C)
        if A % C > 0:
            cnt += 1
        cnt += 1
        A //= C

    if len(digits) >= 2 and digits[-1] == 1 and 1 <= digits[-2] <= C - 2:
        cnt -= 1

    ans.append(B * (cnt - 1))

print(*ans, sep='\n')