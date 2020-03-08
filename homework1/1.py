# 元素输出和查找：
# 请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数

print("奇数：", end="")
for num in range(0, 51):
    if num % 2 != 0:
        print(num, " ", end="")
print()


print("偶数：", end="")
for num in range(0, 51):
    if num % 2 == 0:
        print(num, " ", end="")
print()

print("质数：", end="")
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, " ", end="")
print()


print("被2和3整除的数：", end=""),
for num in range(0, 51):
    if num % 2 == 0 and num % 3 == 0:
        print(num, " ", end="")
