#encoding=utf-8

import dircache
import sys
import os

class BaiduImporter(object):
    """docstring for BaiduImporter"""
    def __init__(self):
        self.typeDict = {}
        self.typeIdx = {}
       
    def loadTypeList(self, filename):
        f = open(filename)
        for line in f:
            lineArr = line.split("\t")
            typename = lineArr[0]
            typeidx = lineArr[1].replace("\n","")
            #load item type, make a dict
            self.typeDict[typename] = typeidx

        
    def loadItemType(self, filename):
        f = open(filename)
        for line in f:
            lineArr = line.split("\t")
            itemhash = lineArr[0]
            itemtype = lineArr[3]
            #load item type, make a dict
            self.typeDict[itemhash] = self.typeDict[itemtype]

    def processFile(self, dirname, outputname):
        ofs = open(outputname, 'w')
        filelist = os.listdir(dirname)
        for f in filelist:
            ifs = open(dirname+"/"+f, 'r')
            fileContent = ifs.read()
            fileContent = fileContent.decode("gbk")
            fileContent = fileContent.replace("\n", " ")
            fileContent = fileContent.replace("\t", " ")
            ofs.write(fileContent.encode("utf-8") + "\t" + self.typeDict[f] + "\n")


if __name__ == "__main__":
    baiduimporter = BaiduImporter()
    baiduimporter.loadTypeList("type.list")
    baiduimporter.loadItemType("item.out.txt")
    baiduimporter.processFile("db.page", "train.txt")
    baiduimporter.processFile("test", "test.txt")
     
    
