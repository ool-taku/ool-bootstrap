#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import log
 
CONF_FILE = os.getcwd() + "/../settings/credentials" 
SECTION = "DEFAULT"

conf = ConfigParser.SafeConfigParser()

_OS_TENANT_NAME=""
_OS_USERNAME=""
_OS_PASSWORD=""
_OS_AUTH_URL=""

def read_config():
        global _OS_TENANT_NAME
        global _OS_USERNAME
        global _OS_PASSWORD
        global _OS_AUTH_URL
	conf.read(CONF_FILE)
	log.debug("read : " + CONF_FILE)
	_OS_TENANT_NAME=conf.get(SECTION, "os_tenant_name")
	_OS_USERNAME=conf.get(SECTION, "os_username")
	_OS_PASSWORD=conf.get(SECTION, "os_password")
	_OS_AUTH_URL=conf.get(SECTION, "os_auth_url")

def save_config():
        global _OS_TENANT_NAME
        global _OS_USERNAME
        global _OS_PASSWORD
        global _OS_AUTH_URL
	try:
		conf.set(SECTION, 'os_tenant_name', _OS_TENANT_NAME)
		conf.set(SECTION, 'os_username',  _OS_USERNAME)
		conf.set(SECTION, 'os_password',  _OS_PASSWORD)
		conf.set(SECTION, 'os_auth_url',  _OS_AUTH_URL)
		log.debug("save : " + CONF_FILE)
        	conf.write(open(CONF_FILE, 'w'))
		read_config()
	except Exception as e:
		log.error( str(type(e)) + str(e.args) + e.message)

read_config()
