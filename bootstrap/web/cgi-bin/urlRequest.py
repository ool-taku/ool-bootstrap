#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()
import subprocess
import sys
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import db_manager
import db_wrapper

form = cgi.FieldStorage()
if not form.has_key("scenario"):
        sys.exit()
if not form.has_key("mode"):
	sys.exit()

rows=db_manager.select(u"select ip, netns from stacks where deleted = '0' and manager = '1' and scenario = '" + form['scenario'].value  + "'")
if form['mode'].value == 'verify':
	subprocess.call(['sudo', 'ip', 'netns', 'exec',
                        rows[0][1],
                        "/usr/bin/python", "/home/openstack/bootstrap/web/cgi-bin/scenario_verify.py" , rows[0][0]])
#	db_wrapper.update_scenarios(form['scenario'].value, "2")
	f=open(os.getcwd() + '/template/redirect.tmpl')
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'url':'index.py'})
	
	print "Content-type: text/html\n"
	print body.encode('utf-8')
else:
        subprocess.call(['sudo', 'ip', 'netns', 'exec',
                        rows[0][1],
                        "/usr/bin/python", "/home/openstack/bootstrap/web/cgi-bin/scenario_result.py" , rows[0][0]])
