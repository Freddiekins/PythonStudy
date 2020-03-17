# 请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
# 例如，输入 aaaabbc，输出：a:4


def count(str):
    times = {}
    max = 0
    for i in str:
        times[i] = str.count(i)
    for key, value in times.items():
        if max < value:
            max = value
            maxchar = key
    print("出现次数最多的字符：", maxchar, "\n", "出现次数：", max)


str = input("请输入字符串：")
count(str)
