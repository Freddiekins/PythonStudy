# 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
import socket

addr = ('', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)
while True:
    print('等待客户端消息...')
    data, addr = s.recvfrom(1024)
    print('接受>', str(data, 'utf-8'))
    strs = input('发送> ')
    if strs.strip() == '':
        print('输入为空')
    else:
        s.sendto(bytes(strs, 'utf-8'), addr)
