sx, sy, tx, ty = map(int, input().split())

holizontal = tx - sx
vertical = ty - sy

ans = ['L']
ans += ['U'] * (vertical + 1)
ans += ['R'] * (holizontal + 1)
ans += ['D']
ans += ['L'] * holizontal
ans += ['D'] * (vertical + 1)
ans += ['R'] * (holizontal + 1)
ans += ['U'] * (vertical + 1)
ans += ['L']
ans += ['D'] * vertical
ans += ['L'] * holizontal

print(''.join(ans))
