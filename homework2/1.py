# 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def length(a):
    return len(a)


print(length([1, 2, 3, 4]), end=" ")
print(length('python'), end=" ")
print(length((1, 2, 3, 4, 5)))
