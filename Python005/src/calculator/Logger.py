# -*- coding: utf-8 -*-

class Logger:
    wfile = open('./logs.txt', "a");
    
    def log(self, msg):
        self.wfile.write(msg+"\n")
        self.wfile.flush();
        print (msg);
        
    def close(self):
        self.wfile.close();