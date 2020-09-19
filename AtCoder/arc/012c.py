N = 19
A = [list(input()) for _ in range(N)]

black = sum(a.count('o') for a in A)
white = sum(a.count('x') for a in A)

def no():
    print('NO')
    exit()

if not (black == white + 1 or black == white):
    no()

def isWin(s):
    for top in range(N):
        for left in range(N):
            leng = 0
            while top + leng < N and A[top + leng][left] == s:
                leng += 1
            if leng >= 5:
                return True

            leng = 0
            while left + leng < N and A[top][left + leng] == s:
                leng += 1
            if leng >= 5:
                return True

            leng = 0
            while top + leng < N and left + leng < N and A[top + leng][left + leng] == s:
                leng += 1
            if leng >= 5:
                return True

            leng = 0
            while top + leng < N and left - leng >= 0 and A[top + leng][left - leng] == s:
                leng += 1
            if leng >= 5:
                return True

    return False

def canMake(s):
    if not isWin(s):
        return True

    for t in range(N):
        for l in range(N):
            if A[t][l] == s:
                A[t][l] = '.'
                if not isWin(s):
                    return True
                A[t][l] = s
    return False

if black > white:
    if isWin('x'):
        no()
    if not canMake('o'):
        no()
else:
    if isWin('o'):
        no()
    if not canMake('x'):
        no()

print('YES')
