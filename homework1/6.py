# 前面2个元素为0，1，输出100以内的斐波那契数列；
a = 0
b = 1
sum = 0
print(a, b, end=" ")
while sum < 100:
    sum = a + b
    if sum > 100:
        break
    print(sum, end=" ")
    a = b
    b = sum
