H, W, N = map(int, input().split())
sh, sw = map(int, input().split())

S = input()
T = input()

def canTakaWin(toS, isInc, toT, R, c):
    now = c

    for s, t in zip(S, T):
        if s == toS:
            now = (now + 1) if isInc else (now - 1)

        if not 0 < now <= R:
            return True

        if t == toT:
            now = (now + 1) if not isInc else (now - 1)
            now = max(1, now)
            now = min(R, now)

    return False

ans = False
ans = ans or canTakaWin('U', False, 'D', H, sh)
ans = ans or canTakaWin('D', True, 'U', H, sh)
ans = ans or canTakaWin('L', False, 'R', W, sw)
ans = ans or canTakaWin('R', True, 'L', W, sw)

print('NO' if ans else 'YES')
