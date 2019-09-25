#tcp服务端程序
def main():
    #导入socket模块
    import socket
    #创建server 套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定server端口
    tcp_socket.bind(('',8080))
    #将server调整为linster模式
    tcp_socket.listen(128)
    #将创建clientsocket服务端套接字
    #循环接受客户端发送过来的信息
    while True:
        print('等待客户端连接')
        clientsocket,clientaddress=tcp_socket.accept()
        print('客户端连接成功,正在服务')
        while True:
            serce=clientsocket.recv(1024)
            #server发送给client的信息
            if serce.decode('gbk')=='close':
                print('{0}服务结束'.format(clientaddress))
                clientsocket.close()
                break
            elif serce:
                print(serce.decode('gbk'))
                data=input('请输入要发送的内容 :')
                clientsocket.send(data.encode('gbk'))
            else:
                print('{0}服务结束,{0}客户端关闭'.format(clientaddress))
                clientsocket.close()
                break

    print('服务结束')
    clientsocket.close()

if __name__=='__main__':
    main()
