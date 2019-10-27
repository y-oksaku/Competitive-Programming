unitPrice, setPrice, nessNum, setNum = map(int, input().split())

allUnit = unitPrice * nessNum
allSet = (-(-nessNum // setNum)) * setPrice

lessNum = nessNum // setNum
comp = lessNum * setPrice + (nessNum - lessNum * setNum) * unitPrice
ans = min(allSet, comp)

print(ans)