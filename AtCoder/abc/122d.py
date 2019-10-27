N = int(input())

MOD = 10**9 + 7

def isValid(text) :  # 有効な4文字の文字列かチェック
    for i in range(4) :
        t = list(text)
        if i >= 1 :
            t[i] , t[i-1] = t[i-1] , t[i]  # swap
        if ''.join(t).count('AGC') >= 1 :
            return False
    return True

memo = [{} for _ in range(N+1)]

def search(currentIndex, prevText) :
    if currentIndex >= N :
        return 1
    if prevText in memo[currentIndex] :
        return memo[currentIndex][prevText]
    ret = 0

    for addText in 'ACGT' :
        if isValid(prevText + addText) :
            ret = (ret + search(currentIndex + 1,prevText[1:] + addText)) % MOD  # 右にシフト

    memo[currentIndex][prevText] = ret
    return ret

print(search(0,'ZZZ'))
