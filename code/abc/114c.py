N = int(input())

def search(s) :
    if int(s) > N :
        return 0
    ret = 1 if all(s.count(i) > 0 for i in ['7', '5', '3']) else 0  # 753数
    for c in ['7', '5', '3'] :
        ret += search(s + c)
    return ret

ans = search('0')

print(ans)