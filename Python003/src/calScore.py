#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys;
reload(sys);
sys.setdefaultencoding('utf-8');

# global wfile
# wfile = open('./score_all2.txt', "a");

# 幼儿园的ID|幼儿园的名称|年级|班级ID|班级名称|幼儿ID|领域|能力|分数值
def readFile():
    # 读取文件
    rfile = open("./score_all2.txt", "r");
    
    klist = {};
    
    # 循环读取每一行
    for line in rfile.xreadlines():
        # 解析每一行
        values = line.strip().split("|");
        if len(values) < 9:
            continue;
        # 幼儿园ID
        kid = int(values[0]);
        # 幼儿园名称
        kname = unicode(values[1], "utf-8");
        # 年级
        grade = int(values[2]);
        # 班级ID
        classId = int(values[3]);
        # 班级名称
        className = unicode(values[4], "utf-8");
        # 幼儿ID
        student = int(values[5]);
        # 领域
        area = int(values[6]);
        # 能力
        ability = unicode(values[7], "utf-8");
        # 分数
        score = int(values[8]);
        
        kitemTemp = {"kid":kid, "kname":kname, "ability":ability, "sum":score, "cnt":1};
        
        kitem = klist.get(kid);
        if kitem == None:
            klist[kid] = kitemTemp;
        else:
            klist[kid]["sum"] = klist[kid]["sum"] + score;
            klist[kid]["cnt"] = klist[kid]["cnt"] + 1;
        print(score);
    return klist;

# 计算平均分
def calAvg(klist):
    # 判断参数list是否为空
    if klist == None or len(klist) <= 0:
        return;
    for kitemKey in klist:
        kitem = klist[kitemKey];
        # TODO 判断参数是否合法
        avg = float(kitem["sum"]) / float(kitem["cnt"]);
        kitem["avg"] = avg;
    return klist;

# 写入新的文件
def writeResult(klist):
    # 判断参数list是否为空
    if klist == None or len(klist) <= 0:
        return;

    # 写入文件
    wfile = open("./score_result.txt", "w");
    for kitemKey in klist:
        # TODO 判断参数是否合法
        kitem = klist[kitemKey];
        print(kitem)
        wfile.write("{kid}|{kname}|{ability}|{avg}|{sum}|{cnt}\n".format(kid=kitem.get("kid"), kname=kitem.get("kname"), ability=kitem.get("ability"), avg=kitem["avg"], sum=kitem["sum"], cnt=kitem["cnt"]));
    wfile.flush();
    wfile.close();
    return;
        
def entry():
    klist = readFile();
    print(klist)
    calAvg(klist);
    print(klist)
    writeResult(klist);
    return;
# 入口
entry();
