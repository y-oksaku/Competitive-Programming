X = int(input())

q, r = divmod(X, 500)
ans = q * 1000 + (r // 5) * 5
print(ans)
