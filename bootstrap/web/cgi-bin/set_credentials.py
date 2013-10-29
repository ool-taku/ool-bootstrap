#!/usr/bin/env python
# coding: utf-8

import os
import sys
import cgi
import cgitb; cgitb.enable()
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import credentials 

def credentials_list():
        ret=""
        ret += """<tr><td>os_tenant_name</td><td><input type="text" style="width:90%%" id="os_tenant_name" value=%s></td></tr>""" % (credentials._OS_TENANT_NAME)
	ret += """<tr><td>os_username</td><td><input type="text" style="width:90%%" id="os_username" value=%s></td></tr>""" % (credentials._OS_USERNAME)
	ret += """<tr><td>os_password</><td><input type="text" style="width:90%%" id="os_password" value=%s></td></tr>""" % (credentials._OS_PASSWORD)
	ret += """<tr><td>os_auth_url</td><td><input type="text" style="width:90%%" id="os_auth_url" value=%s></td></td></tr>""" % ( credentials._OS_AUTH_URL)
	return ret

def save_credentials():
	credentials.save_config()

with open(os.getcwd() + '/template/set_credentials.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'credentials':credentials_list()})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
