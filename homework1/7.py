# 打印输出9*9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "×", i, "=", i*j, end="")
        print("    ", end="")
    print()
