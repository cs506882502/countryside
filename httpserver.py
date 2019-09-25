# #coding=utf-8
# #创建一个带有http的tcp server
# import socket,re
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定服务器ip端口
# s.bind(('192.168.0.100',8000))
# #设置为监听模式
# s.listen(128)
# #等待客户端连接,循环服务
# while True:
#     childsocket,childaddress=s.accept()
#     c=childsocket.recv(1024).decode('utf-8')
#     d=re.match(r'GET /(.*) HTTP',c)
#     d1=d.group(1)
#     if d1:
#         try:
#             with open('{0}'.format(d1),'r') as f:
#                 b=f.read()
#                 response='HTTP/1.1\r\n'+'\r\n'
#                 r=response+b
#                 childsocket.send(r.encode('utf-8'))
#         except:
#             response='HTTP/1.1\r\n'+'\r\n'+'<body><h4>访问的页面不存在!!!</h4></body>'
#             childsocket.send(response.encode('gbk'))

#协程实现http server
import gevent,socket,re
from gevent import monkey
monkey.patch_all()

def recvf(s):
    res=s.recv(1024).decode('utf-8')
    print(gevent.getcurrent())
    return res
def send(s,res):
    print(gevent.getcurrent())
    rd=re.match(r'GET /(.*) HTTP/1.1',res)
    try:
        HTTP='HTTP/1.1\r\n'+'\r\n'
        if rd.group(1):
            with open('{0}'.format(rd.group(1)),'r') as f:
                read=f.read()
                read=HTTP+read
                s.send(read.encode('utf-8'))
        else:
            html='<body><h1>welcome to my page !</h1></body>'
            html=HTTP+html
            s.send(html.encode('utf-8'))
    except:
        data='<body><h6>访问的页面不存在!!!</h6></body>'
        HTTP = 'HTTP/1.1\r\n' + '\r\n'
        data=HTTP+data
        s.send(data.encode('gbk'))

def main():
    #创建套接字
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8080))
    s.listen(128)
    while True:
        childsocket,childaddress=s.accept()
        res=recvf(childsocket)
        g2=gevent.spawn(send,childsocket,res)
        g2.join()
        # send(childsocket,res)
if __name__ =='__main__':
    main()








