#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import db_manager
import log

def show_env(scenario):
        ret=""
#	rows=db_manager.select(u"select uuid, host, ip, netns, manager from stacks where scenario='%s' and deleted=0" % scenario)
	rows=db_manager.select(u"select host, ip, netns, manager from stacks where scenario='%s' and deleted=0" % scenario)
        ret=""
        tmp=[]
        for row in rows:
                log.debug(str(row))
#		ret+="""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>""" % (row[0], row[1], row[2], row[3], 'yes' if row[4]==1 else 'no')
		ret+="""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>""" % (row[0], row[1], row[2], 'yes' if row[3]==1 else 'no')
	
	return ret

form = cgi.FieldStorage()
if not form.has_key("scenario"):
        log.error("Not found Parametor scenario.")
        sys.exit(1)

scenario = form['scenario'].value

with open(os.getcwd() + '/template/show_environment.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'environment':show_env(scenario)})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
