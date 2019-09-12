from collections import Counter

N = int(input())
V = list(map(int, input().split()))

evenCnt = Counter(V[::2]).items()
oddCnt = Counter(V[1::2]).items()

evenCnt = list(evenCnt)
oddCnt = list(oddCnt)

evenCnt.sort(key=lambda A: A[1], reverse=True)
oddCnt.sort(key=lambda A: A[1], reverse=True)

if evenCnt[0][0] != oddCnt[0][0]:
    ans = (-(-N // 2) - evenCnt[0][1]) + (N // 2 - oddCnt[0][1])
    print(ans)
else:
    ans = min(
        (-(-N // 2) - evenCnt[0][1]) + N // 2,
        -(-N // 2) + (N // 2 - oddCnt[0][1])
    )
    if len(evenCnt) > 1:
        ans = min(ans, (-(-N // 2) - evenCnt[1][1]) + (N // 2 - oddCnt[0][1]))
    if len(oddCnt) > 1:
        ans = min(ans, (-(-N // 2) - evenCnt[0][1]) + (N // 2 - oddCnt[1][1]))

    print(ans)