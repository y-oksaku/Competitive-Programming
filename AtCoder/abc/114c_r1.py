N = int(input())

def dp(now) :
    if int(now) > N :
        return 0
    count = 0
    if all(x in now for x in ['7', '5', '3']) :
        count += 1
    for x in ['7', '5', '3'] :
        count += dp(now + x)
    return count

ans = dp('0')
print(ans)