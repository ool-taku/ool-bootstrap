#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import scenario

def param_list():
        ret=""
	ret += """<tr><td>ssh_user</td><td><input type="text" style="width:90%%" id="ssh_user" value=%s readonly></td></tr>""" % (scenario._SSH_USER)
	ret += """<tr><td>manager_template</td><td><input type="text" style="width:90%%" id="manager_template" value=%s readonly></td></tr>""" % (scenario._MAN_TMPL)
	ret += """<tr><td>agent_template</td><td><input type="text" style="width:90%%" id="agent_template" value=%s readonly></td></tr>""" % (scenario._AG_TMPL)
	ret += """<tr><td>instance_type</td><td><input type="text" style="width:90%%" id="instance_type" value=%s readonly></td></tr>""" % (scenario._INSTANCE_TYPE)
	ret += """<tr><td>key_name</td><td><input type="text" style="width:90%%" id="key_name" value=%s readonly></td></tr>""" % (scenario._KEY_NAME)
	ret += """<tr><td>subnet_name</td><td><input type="text" style="width:90%%" id="subnet_name" value=%s readonly></td></tr>""" % (scenario._SUBNET_NAME)
	return ret

if os.environ['REQUEST_METHOD'] != "POST":
        log.error("Not found POST method.")
        sys.exit(1)

form = cgi.FieldStorage()
if not form.has_key("scenario"):
        log.error("Not found Parametor scenario.")
        sys.exit(1)

script_path = os.path.abspath(os.path.dirname(__file__))

scenario_name = form['scenario'].value

scenario.set_scenario(script_path + "/../../scenario/" + scenario_name)
scenario.read_scenario()

with open(os.getcwd() + '/template/edit_scenario.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'scenario':param_list(),'select_scenario':scenario_name})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
