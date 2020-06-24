# 编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；
# 另外一个进程接收并打印消息
import threading
count = 0


def chat(strs):
    lock.acquire()
    strs = input('请输入信息：')
    if strs != '':
        print('输出信息：' + strs)
        strs = ''
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    st = ''
    t1 = threading.Thread(target=chat, args=(st,))
    t2 = threading.Thread(target=chat, args=(st,))
    threads = []
    threads.append(t1)
    threads.append(t2)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
