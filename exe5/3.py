# 编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
def login(func):
    def wrapper():
        name = input('请输入账号：')
        if name == '12345':
            code = input('请输入密码:')
            if code == 'qwer':
                func()
            else:
                print('密码错误')
        else:
            print('账号错误')
    return wrapper


@login
def fun1():
    print('This is function 1')


@login
def fun2():
    print('This is function 2')


fun1()
fun2()
