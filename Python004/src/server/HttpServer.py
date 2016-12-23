#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer;
from SocketServer import StreamRequestHandler as SRH;
from time import ctime;

host = '0.0.0.0'  
port = 8080;
addr = (host, port)  

class Servers(SRH):  
    def handle(self):  
        print 'got connection from ', self.client_address
        request = self.request.recv(2048);
        print (request);
        print ("--------------------");
        # data
        body = '''
<html>
    <header>
        <meta charset="UTF-8">
        <title>Http Test</title>
    </header>
    <body>
        <p>简单的web程序</p>
    </body>
</html>''';
        # header
        header = "HTTP/1.1 200 OK\r\nContent-type:text/html\r\nContent-length:" + str(len(body)) + "\r\n\r\n";
        # 数据内容
        data = header + body;
        print("[" + data + "]");
        self.request.send(data);
        
print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr, Servers);
server.serve_forever();
