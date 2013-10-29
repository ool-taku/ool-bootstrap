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

def scenario_list():
	senarios = os.listdir(os.getcwd() + "/../scenario")
	rows=db_manager.select(u"select scenario from scenarios")
	ret=""
	tmp=[]
	for row in rows:
		tmp.append(row[0])
	for config in senarios:
		if len(rows) > 0:
			if config not in tmp:
				ret += """<li><span onclick="set_value('scenario','%s')"><a href="" onclick="return false;">%s</a></span></li>""" % (config, config)
		else:
			ret += """<li><span onclick="set_value('scenario','%s')"><a href="" onclick="return false;">%s</a></span></li>""" % (config, config)
	return ret

def check_scenario():
	form = cgi.FieldStorage()
	if form.has_key("scenario"):
		return form['scenario'].value
        else:
		return ''

with open(os.getcwd() + '/template/createScenario.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'scenario':scenario_list(),'select_scenario':check_scenario()})

	print "Content-type: text/html\n"
	print body.encode('utf-8')

