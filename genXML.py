#!/user/bin/env python3
# -*- coding: utf-8 -*-
import csv
tab='    '
def indentText(text,lineSep):
    afterText=''
    for line in str(text).split(lineSep):
        afterText = afterText + tab + line + lineSep
    return afterText

class Node(object):
    def __init__(self,nodeName,listAttr,listValue):
        self._children=list([])
        self._nodeName=nodeName
        self._listAttr=listAttr
        self._listValue=listValue
    def addChild(self,node):
        if(isinstance(node,Node)):
            self._children.append(node)
        else:
            raise Exception('not a valide node.')
    def genStr(self,sep):
        self._text='<'+ self._nodeName
        if(len(self._listAttr)==0):
            self._text += '>'
            self._text += sep
        else:
            for idx in range(len(self._listAttr)):
                self._text = self._text+' '+str(self._listAttr[idx])+'='+str(self._listValue[idx])
        if(len(self._children)!=0):
            self._text += '>'
            self._text += sep
            for children in self._children:
                self._text += indentText(children.genStr(sep),sep)
            self._text += '</'+self._nodeName+'>'
        else:
            self._text += '/>'
        return self._text


with open('D:\\code\\python\\para.csv',newline='') as csvfile:
    preader=csv.reader(csvfile)
    data = [row for row in preader]
        #data=data.append(row)
print(data)
del data[0]


def createCmdtree():
    text=''
    for row in data:
        text='<paraname = '+row[0]+' />'
        text = text+'\n'+tab+'<description = '+row[1]+' />'
    with open('D:\\code\\python\\cmdtree.txt','w') as f:
        f.write(text)

strlist=['name1','name2','name3']
vallist=[1,2,3]

root=Node('leve0',strlist,vallist)
node1=Node('leve1',strlist,vallist)
node2=Node('leve2',strlist,vallist)
root.addChild(node1)
node1.addChild(node2)
print(root.genStr('\n'))