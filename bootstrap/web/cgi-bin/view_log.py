#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
scenario = form['scenario'].value

log_path = os.getcwd() + "/../log/"+ scenario

print "Content-type: text/html\n"
print "<html><body>"
print """<table border="0"><tr><td style="width:60em; word-break:break-all;">"""
with open(log_path) as f:
	for line in f:
    		print line + "<br>"
print "</td></tr></table>"
print "</body></html>"
