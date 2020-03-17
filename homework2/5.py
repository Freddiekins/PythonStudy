# 写函数，检查传入字典的每一个value长度
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;


def dictEdit(dic):
    newdict = {}
    for key, value in dic.items():
        if len(value) > 2:
            newdict[key] = value[0:2]
    return newdict


dict = {"k1": "v1v1", "k2": [11, 22, 33, 44], "k3": "12"}
newdict = dictEdit(dict)
print(newdict)
