# 设计一个数据结构，用来存放10个员工的信息并初始化;
# 每个员工信息包括：工号，姓名，工龄，工资;
# 将这10个员工，按照工资从高到低打印输出;


def fifth(elem):
    return elem[3]


list = [
    # ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    # [3, 9, 1, 5, 2, 4, 7, 6, 3, 8],
    # [2000, 7000, 4000, 2500, 5000, 6500, 5200, 4500, 6700, 2300]
    ('001', 'a', 3, 2000),
    ('002', 'b', 9, 7000),
    ('003', 'c', 1, 4000),
    ('004', 'd', 5, 2500),
    ('005', 'e', 2, 5000),
    ('006', 'f', 4, 6500),
    ('007', 'g', 7, 5200),
    ('008', 'h', 6, 4500),
    ('009', 'i', 3, 6700),
    ('010', 'j', 8, 2300)
]
list.sort(key=fifth, reverse=True)
print(list)