#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb; cgitb.enable()
import sys
import urllib
#import os
#sys.path.append(os.getcwd() + "/../scripts")

def get_result(host):
        wp = urllib.urlopen(url='http://'+host+':18000/cgi-bin/verify.py')
        #gwp = wp.read()
        #return gwp

argvs = sys.argv
#print 'Content-Type:text/html'
#print 
get_result(argvs[1])
