N = int(input())
H = [int(input()) for _ in range(N)]

ans = [0] * N

st = [(10**18, 0)]
for i, h in enumerate(H):
    while st[-1][0] <= h:
        st.pop()
    ans[i] += i - st[-1][1]
    st.append((h, i + 1))

st = [(10**18, 0)]
for i, h in enumerate(H[::-1]):
    while st[-1][0] <= h:
        st.pop()
    ans[-(i + 1)] += i - st[-1][1]
    st.append((h, i + 1))

print(*ans, sep='\n')
