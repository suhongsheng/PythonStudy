#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer;
from SocketServer import StreamRequestHandler as SRH; 
from time import ctime;

host = '0.0.0.0';
port = 8080;
addr = (host, port);

class Servers(SRH):  
    def handle(self):  
        print 'got connection from ', self.client_address;
        request = self.request.recv(2048);
        print (request);
        
        if(len(request) < 20):
            return;
        
        url = None;
        # 获取请求的URL
        for line in request.split("\n"):
            print(line);
            if(len(line) > 10 and line.index("GET") == 0):
                getHeader = line.split(" ");
                print(getHeader[1]);
                url = getHeader[1];
                break;
            else:
                pass;
        print ("--------------------");
        if(url == None):
            # header
            header = "HTTP/1.1 404 NotFound\r\nContent-type:text/html\r\n\r\n";
            # 数据内容
            self.request.send(header);
            return ;
        else:
            pass;
        # 读取相应的文件
        body = "";
        rfile = open("../root" + url, "r")
        for line in rfile.xreadlines():
            body += line;
        # data
        # header
        header = "HTTP/1.1 200 OK\r\nContent-type:text/html\r\nContent-length:" + str(len(body)) + "\r\n\r\n";
        # 数据内容
        data = header + body;
        self.request.send(data);
        
print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr, Servers);
server.serve_forever();
