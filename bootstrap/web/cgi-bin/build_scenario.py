#!/usr/bin/env python 
# coding: utf-8

import os
import sys
import cgi
import pwd
import cgitb; cgitb.enable()
import threading
import subprocess
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import credentials 
import log

#print "Content-type: text/html\n"
#print "Location: index.py\n\n"
#print """<META HTTP-EQUIV="Refresh" CONTENT="5"; URL="index.py" />"""

if os.environ['REQUEST_METHOD'] != "POST":
	log.error("Not found POST method.")
	sys.exit(1)

form = cgi.FieldStorage()
if not form.has_key("scenario"):
	log.error("Not found Parametor scenario.")
	sys.exit(1)

script_path = os.path.abspath(os.path.dirname(__file__))

scenario = form['scenario'].value
log_path=script_path + "/../../log/" + scenario

try:
	f=open(log_path, "w")
except IOError as e:
	log.error("can not open :" + log_path)
	log.error( str(type(e)) + str(e.args) + e.message)
	sys.exit(1)

try:
	log.info("start to build scenario:" + scenario)
	subprocess.Popen([script_path + "/../../scripts/bootstrap", scenario, "credentials"], stdout=f, stderr=f)
except OSError as e:
	log.error( str(type(e)) + str(e.args) + e.message)
	sys.exit(1)

with open(os.getcwd() + '/template/redirect.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'url':'index.py'})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
