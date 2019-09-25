import socket
#tcp客户端程序
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input('输入要连接的ip :')
port=int(input('输入要连接的端口 :'))
data=input('请输入要发送的内容 :')
clientsocket.connect((ip,port))
clientsocket.send(data.encode('gbk'))
rece=clientsocket.recv(1024)
print(rece.decode('gbk'))
clientsocket.close()