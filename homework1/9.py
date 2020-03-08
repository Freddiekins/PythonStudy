# 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
count = 5
num = 11
while count != 0:
    print("请输入数字，剩余", count, "次：", end="")
    a = int(input())
    if a == num:
        print("正确！")
        break
    count = count - 1
if count == 0:
    print("失败！无剩余次数")
