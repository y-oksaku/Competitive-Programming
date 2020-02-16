S = input()
X, Y = map(int, input().split())

A = [0]
for s in S:
    if s == 'T':
        A.append(0)
    else:
        A[-1] += 1

B = [n for n in A[1:: 2]]
X -= A[0]
A = [n for n in A[2:: 2]]

def canGo(nums, g):
    if not nums:
        return g == 0

    bias = sum(nums) + 10
    g += bias
    if g < 0:
        return False

    dp = (1 << bias)

    for n in nums:
        dp = (dp << n) | (dp >> n)
    return (dp & (1 << g)) > 0

if canGo(A, X) and canGo(B, Y):
    print('Yes')
else:
    print('No')
