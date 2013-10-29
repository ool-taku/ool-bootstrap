#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb 
import os
import log
import urlparse
import ConfigParser
import glob

CONF_DIR="/etc/quantum"
conf = ConfigParser.SafeConfigParser()

#log._DEBUG=True

def get_mysql_info(sql_connection):
	log.debug(sql_connection)
	url = urlparse.urlparse(sql_connection)
	log.debug(url)
	if url.scheme != "mysql":
		log.error("Not MySQL")
	ret = {}
	ret["db"]=url.path.strip('/').split('?')[0]
	tmp = url.netloc.split('@')
	ret["host"]=tmp[1]
	ret["user"]=tmp[0].split(':')[0]
	ret["passwd"]=tmp[0].split(':')[1]
	log.debug(ret)
	return ret

def select(connection, sql):
	info = get_mysql_info(connection)
	conn = MySQLdb.connect(host=info["host"], db=info["db"], user=info["user"], passwd=info["passwd"], charset="utf8")
	cursor = conn.cursor()
	cursor.execute(sql)
	rows = cursor.fetchall()
	cursor.close()
	conn.close()
	return rows

def get_option(option, conf):
	for section in conf.sections():
		if conf.has_option(section, option):
			return conf.get(section, option)
	if conf.default() in option:
		return conf.get("DEFAULT", option)

def get_sql_connection():
	for (root, dirs, files) in os.walk(CONF_DIR):
		for f in files:
			try:
				conf.read(os.path.join(root, f))
				ret = get_option("sql_connection", conf)
				if ret:
					return ret
			except Exception as e:
				log.debug(str(type(e)) + str(e.args) + str(e.message))

#print get_sql_connection()

#ret = select(get_sql_connection(), "select * from ipallocations")
#for row in ret:
#	print row

#print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#ret = select("mysql://quantum:quantum@ubuntu-ct/ovs_quantum?charset=utf8", "select * from ipallocations")
#for row in ret:
#        print row	

