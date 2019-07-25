S = input()
T = input()

for i in range(len(S) - len(T), -1, -1) :
    for j, t in enumerate(T) :
        if S[i + j] == '?' :
            continue
        if S[i + j] != t :
            break
    else :
        ans = list(S)
        ans[i: i + len(T)] = T
        print(''.join(ans).replace('?', 'a'))
        break
else :
    print('UNRESTORABLE')