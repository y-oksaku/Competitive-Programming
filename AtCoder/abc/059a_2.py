import string

ans = ''.join(map(lambda s: s[0], input().split()))
for s, S in zip(string.ascii_lowercase, string.ascii_uppercase):
    ans = ans.replace(s, S)
print(ans)
