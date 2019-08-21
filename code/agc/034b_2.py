s = input()
N = len(s)

count = 0
ans = 0
left = N - 1

for i in range(N-1,-1,-1) :
    if s[i] == 'A' :
        j = i + 1
        for j in range(i+1,N,2) :
            if s[j] == 'C' :
                break
        if j == left :
            count += 1
        else :
            count = 0
        ans += int(j/2) - count

print(ans)