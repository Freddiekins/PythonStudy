# 判断用户输入的年份是否为闰年
a = int(input("输入年份："))
if a % 4 == 0:
    print("是闰年")
else:
    print("不是闰年")
