#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer  
from SocketServer import StreamRequestHandler as SRH;
from time import ctime;

host = '0.0.0.0';
port = 9999;
addr = (host, port);


# 加法
def add(a, b):
    return a + b;

# 减法
def sub(a, b):
    return a - b;

# 乘法
def mul(a, b):
    return a * b;

# 除法
def dev(a, b):
    return a / b;

operator = {1:add, 2:sub, 3:mul, 4:dev};

class Servers(SRH):  
    def handle(self):  
        print 'got connection from ', self.client_address;
        print('connection %s:%s at %s succeed!' % (host, port, ctime()));
        while True:  
            data = self.request.recv(1024)  
            if not data:   
                break  
            print (data);
            items = data.split(" ");
            print(items);
            print ("RECV from ", self.client_address[0]);
            result = operator.get(int(items[1]))(float(items[0]), float(items[2]));
            self.request.send(str(result));
print 'server is running....';
server = SocketServer.ThreadingTCPServer(addr, Servers);
server.serve_forever();
