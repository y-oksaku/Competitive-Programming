s = input()

ans = 0
i = 0

while i < len(s) :
    if s[i] == 'A' :
        if s[i+1] == 'B' and s[i+2] == 'C' : # 置換可能
            j = 1
            for j in range(1,i+1) :
                if not s[i-j] == 'A' : # 後方置換
                    break
            k = 0
            for k in range(0,len(s)) :
                ans += j - 1 + k
                if not s[i+k] == 'A' :
                    break
            i += k + 3
    i += 1

print(ans + 1)