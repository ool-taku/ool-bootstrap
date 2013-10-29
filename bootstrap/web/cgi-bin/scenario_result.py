#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb; cgitb.enable()
import sys
import urllib
#import os
#sys.path.append(os.getcwd() + "/../scripts")

def get_result(host):
        wp = urllib.urlopen(url='http://'+host+':18000/result.html')
        gwp = wp.read()
        return gwp

argvs = sys.argv
ret=get_result(argvs[1])
#f = open('result.txt', 'w')
#f.write(ret)
#f.close()
print 'Content-Type:text/html\n'
print get_result(argvs[1])
#print ret.encode('utf-8')
