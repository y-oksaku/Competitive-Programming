N = int(input())
W = list(map(lambda s: s.replace('.', ''), input().split()))

ans = W.count('TAKAHASHIKUN') + W.count('Takahashikun') + W.count('takahashikun')
print(ans)
