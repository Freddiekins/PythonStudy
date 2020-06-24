# 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
import socket

addr = ('127.0.0.1', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    strs = input('发送> ')
    if strs.strip() == '':
        print('输入为空')
    else:
        s.sendto(bytes(strs, 'utf-8'), addr)
    print('等待服务器消息...')
    data, addr = s.recvfrom(1024)
    print('收到>', str(data, 'utf-8'))
