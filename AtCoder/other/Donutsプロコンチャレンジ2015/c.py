N = int(input())
H = list(map(int, input().split()))
st = [10**18]
ans = []
for h in H:
    ans.append(len(st) - 1)
    while st[-1] <= h:
        st.pop()
    st.append(h)
print(*ans, sep='\n')
