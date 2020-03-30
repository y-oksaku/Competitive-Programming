# 幾何ライブラリ

def distPointToLine(P, L1, L2):
    """
    点P - 線分L1L2 間の距離
    P, L1, L2: tuple
    """
    P = complex(*P)
    L1 = complex(*L1) - P
    L2 = complex(*L2) - P
    return (L1.real * L2.imag - L1.imag * L2.real) / abs(L1 - L2)
