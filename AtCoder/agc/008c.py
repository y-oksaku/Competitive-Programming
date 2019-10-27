I, O, _, R, L, _, _ = map(int, input().split())

ans = O
if I * R * L == 0:
    ans += (I // 2 + L // 2 + R // 2) * 2
else:
    M = I % 2 + L % 2 + R % 2
    if M <= 1:
        ans += (I // 2 + L // 2 + R // 2) * 2
    else:
        ans += 3
        I -= 1
        L -= 1
        R -= 1
        ans += (I // 2 + L // 2 + R // 2) * 2

print(ans)
