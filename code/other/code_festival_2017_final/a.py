S = input() + '$'
T = 'AKIHABARA$'

s = 0
t = 0
while s < len(S) or t < len(T):
    if s >= len(S) or t >= len(T):
        break

    if S[s] == T[t]:
        s += 1
        t += 1
    else:
        if T[t] == 'A':
            t += 1
        else:
            break
else:
    print('YES')
    exit()

print('NO')