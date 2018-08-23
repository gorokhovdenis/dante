#!/usr/bin/python
import os
a=os.system('ps -aux | grep bot_old>>/tmp/ps.txt')
print a

#
#def process():
#        f=open('/tmp/ps.txt','r')
#        array=[]
#        for line in f:
#                ip = line.split(' ')[0]#split each line and copy ip
#                array.append(ip)#append ip into array
#        for i,j in [(array[k],array[k+1])#collate each element of array
#                for k in range(len(array)-1)]:
#                        if i!=j:#print unique elements
#                                print(i)
#process()

