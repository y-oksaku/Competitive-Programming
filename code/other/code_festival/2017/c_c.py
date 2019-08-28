S = input()
N = len(S)

left = 0
right = N - 1

ans = 0
while left < right :
    if S[left] == S[right] :
        left += 1
        right -= 1
        continue
    if S[left] == 'x' :
        ans += 1
        left += 1
        continue
    if S[right] == 'x' :
        ans += 1
        right -= 1
        continue
    print('-1')
    break
else :
    print(ans)