# 编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中
import logging
import os


def logging_writing(func):
    def wrapper():
        path = os.getcwd()
        logging.basicConfig(
            level=logging.INFO,
            filename=path + '/exe5/2.txt',
            format="%(asctime)s %(name)s %(levelname)s %(message)s"
        )
        logging.info('fun is running')
        func()
    return wrapper


@logging_writing
def fun():
    print('This is a function')


fun()
