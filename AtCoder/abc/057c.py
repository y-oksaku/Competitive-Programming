N = int(input())

def factor(n):
    factList = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factList.append(i)
            factList.append(n // i)
        i += 1

    factList.sort()
    return factList

fact = factor(N)

ans = float('inf')
for i in range(len(fact)):
    f = max(len(str(fact[i])), len(str(fact[-1 - i])))
    ans = min(ans, f)

print(ans)