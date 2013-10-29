#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb; cgitb.enable()
import sys
import threading
import shlex
import time
import subprocess
import os
from string import Template
sys.path.append(os.getcwd() + "/../scripts")
import db_manager
import db_wrapper
import credentials
import log

#def delete_stack(scenario):
#	auth_param="--os-auth-url=" + credentials._OS_AUTH_URL  +" --os-tenant-name=" + credentials._OS_TENANT_NAME + " --os-username=" + credentials._OS_USERNAME + " --os-password=" + credentials._OS_PASSWORD
#	rows=db_manager.select(u"select uuid from stacks where deleted=0 and scenario='" + scenario + "'")
#	for uuid in rows:
#		os.system("heat " + auth_param + " stack-delete " + uuid[0])
#		db_wrapper.delete_stack(uuid[0])
#	db_wrapper.delete_scenario(scenario)

class del_thread(threading.Thread):
	def __init__(self, key):
		threading.Thread.__init__(self)
		self.setDaemon(False)
		self.scenario = key

	def run(self):
		auth_param="--os-auth-url=" + credentials._OS_AUTH_URL  +" --os-tenant-name=" + credentials._OS_TENANT_NAME + " --os-username=" + credentials._OS_USERNAME + " --os-password=" + credentials._OS_PASSWORD
		rows=db_manager.select(u"select uuid from stacks where deleted=0 and scenario='" + self.scenario + "'")
		for uuid in rows:
			args="heat " + auth_param + " stack-delete " + uuid[0]
			subprocess.Popen(shlex.split(args))
			time.sleep(5)
			db_wrapper.delete_stack(uuid[0])
		db_wrapper.delete_scenario(self.scenario)

form = cgi.FieldStorage()
scenario = form['scenario'].value
log.debug("delete scenario : " + scenario)
th = del_thread(scenario)
th.start()
db_wrapper.update_scenarios(scenario, "3")
log.debug("delete thread start.")

with open(os.getcwd() + '/template/redirect.tmpl') as f:
	data=f.read()
	tmpl=Template(unicode(data, 'utf-8', 'ignore'))
	body=tmpl.substitute({'url':'index.py'})
	print "Content-type: text/html\n"
	print body.encode('utf-8')
	log.debug("redirect.tmpl print.")
