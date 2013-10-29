#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import db_manager

def scenario_status(value):
	if value == 0:
		return "Building"
	elif value == 1:
		return "Active"
	elif value == 3:
		return "Deleting"
	else:
		return "Validating"

def scenario_list():
        ret=""
        rows=db_manager.select(u"select * from scenarios")
        for row in rows:
		ret += """<tr><td>%s</td>""" % (row[0])
		status=scenario_status(row[1])
		ret += """<td>%s""" % (status)
		if row[1] == 1:
			ret += """</td><td><button type="button" class="sample" onclick="if(show_dialog('Do you validate?')){page_load('urlRequest.py?scenario=%s&mode=verify','GET',null)}">Verify</button><button type="button" class="sample" onclick="page_load('urlRequest.py?scenario=%s&mode=ref','GET',null)">Show Result</button><button type="button" class="sample" onclick="if(show_dialog('Do you want to delete this verification environment?')){page_load('scenario_delete.py?scenario=%s','GET',null)}">Delete</button><button type="button" class="sample" onclick="page_load('show_environment.py?scenario=%s','GET',null)">Environment</button><button type="button" class="sample" onclick="page_load('view_log.py?scenario=%s','GET',null)">Log</button></td>""" % (row[0], row[0], row[0], row[0], row[0])
		else:
			ret += """<br><progress max="100"></progress></td>"""
			ret += """<td><button type="button" class="sample" onclick="return false;" disabled>Verify</button><button type="button" class="sample" onclick="return false" disabled>Show Result</button><button type="button" class="sample" onclick="return false" disabled>Delete</button><button type="button" class="sample" onclick="return false" disabled>Environment</button><button type="button" class="sample" onclick="page_load('view_log.py?scenario=%s','GET',null)">Log</button></td>""" % (row[0])
		ret += """</tr>"""
        return ret


with open(os.getcwd() + '/template/index.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'scenario':scenario_list()})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
