#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import dns.resolver

with open(r"C:\Users\Marchen\Desktop\dns.csv",'r') as f:
    alist = [line.rstrip() for line in f]

#output = open(r"C:\Users\Marchen\Desktop\dns-output.txt",'w')

for i in alist:
    try:
        answers = dns.resolver.query(i,'SOA')
    except Exception:
        pass
#    time.sleep(1)
#    for a in soa:
#        print(i)
#        print(a)
#        for j in soa
    for rdata in answers:
#       print(rdata.serial, rdata.rname)
        print(i,rdata.rname) 
#        if i not in rdata.rname:
#            print(i)
#       print(rdata.refresh, rdata.retry)
#       print(rdata.expire, rdata.minimum)
#        print(rdata.mname)

