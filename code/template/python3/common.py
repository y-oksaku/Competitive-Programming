# 辞書のフィルター
def dictFilter (filter, dic) :
    return { key : val for key, val in dic.items() if filter(key, val)}
