N = int(input())
S = [input() for _ in range(5)]

T = [
    '.###..#..###.###.#.#.###.###.###.###.###.',
    '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
    '.#.#..#..###.###.###.###.###...#.###.###.',
    '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
    '.###.###.###.###...#.###.###...#.###.###.',
]

nums = []
for i in range(0, 10):
    l = 4 * i
    sub = []
    for s in T:
        sub.append(s[l: l + 4])
    nums.append(tuple(sub))

nums = {n: str(i) for i, n in enumerate(nums)}

ans = []
for i in range(0, N):
    l = 4 * i
    sub = []
    for s in S:
        sub.append(s[l: l + 4])
    ans.append(nums[tuple(sub)])

print(''.join(ans))
