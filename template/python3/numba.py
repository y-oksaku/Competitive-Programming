import sys
import numpy as np

def main(A):
    return 0

def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8[:])')(main)
    cc.compile()

if sys.argv[-1] == 'ONLINE_JUDGE':
    cc_export()
    exit(0)
if sys.argv[-1] != 'LOCAL':
    from my_module import main

A = np.ones(10, dtype=np.int64)
ans = main(A)
print(ans)
