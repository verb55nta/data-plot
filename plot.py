#!/usr/bin/env python3
from numpy import *
import pylab as plt
import sys

#x=linspace(-pi,pi,100)
#y=sin(x)
#plt.plot(x,y)
#plt.show()

def zero_bury(y,x):
    last_non_zero_index=-1
    for i in range(0,len(y)):
        if(y[i] != 0):
            if last_non_zero_index+1 != i:
                if last_non_zero_index == -1 :
                    for j in range(last_non_zero_index+1,i):
                        x[j] = x[i]
                else:
                    for j in range(last_non_zero_index+1,i):
                        x[j] = (x[last_non_zero_index] + x[i])/2
            last_nonzero_number=y[i]
            last_non_zero_index=i
    if last_non_zero_index+1 != len(y):
        for j in range(last_non_zero_index+1,len(y)):
            x[j] = x[last_non_zero_index]
        last_non_zero_index=len(y)-1
    return x
doll_rate_file=open(sys.argv[1])

line=doll_rate_file.readline()
doll_rate_bid=[]
doll_rate_ask=[]
i=0
while line:
    doll_rate_time=line.split(':')[0].split('m')[0]+'m'
    doll_rate_bid.append(float(line.split(':')[2]))
    doll_rate_ask.append(float(line.split(':')[4]))
    line=doll_rate_file.readline()
    i=i+1
x=[]
size=len(doll_rate_bid)
for j in range(0,1440):
    x.append(j)
doll_rate_bid=zero_bury(doll_rate_bid,doll_rate_bid)
doll_rate_ask=zero_bury(doll_rate_ask,doll_rate_ask)
#print(doll_rate_bid)
#print(doll_rate_ask)
plt.plot(x,doll_rate_bid)
plt.show()
