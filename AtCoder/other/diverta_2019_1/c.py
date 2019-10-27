N = int(input())
S = [input() for _ in range(N)]

tailA = 0
headB = 0
same = 0
inside = 0
for s in S:
    inside += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        same += 1
    else:
        if s[0] == 'B':
            headB += 1
        if s[-1] == 'A':
            tailA += 1

ans = 0

if same >= 1:
    if tailA >= 1:
        ans += same
        tailA -= 1
    else:
        ans += same - 1

    if headB >= 1:
        ans += 1
        headB -= 1

ans += max(min(tailA, headB), 0)
print(ans + inside)