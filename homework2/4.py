# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def strScan(str):
    letter = 0
    num = 0
    char = 0
    space = 0
    for i in str:
        if i.isdigit():
            num = num + 1
        elif i.isalnum():
            letter = letter + 1
        elif i.isspace():
            space = space + 1
        else:
            char = char + 1
    print('字母个数：', letter,)
    print('数字个数：', num)
    print('空格个数：', space)
    print('其他字符个数：', char)


str = input("请输入字符串：")
strScan(str)
