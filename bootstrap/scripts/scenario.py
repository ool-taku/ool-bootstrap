#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import log

SCENARIO_PATH=""
SECTIONS=["AUTH", "AP", "INSTANCE"]
 
conf = ConfigParser.SafeConfigParser()

_SSH_USER=""

_MAN_TMPL=""
_AG_TMPL=""

_INSTANCE_TYPE=""
_KEY_NAME=""
_SUBNET_NAME=""

def read_scenario():
	global _SSH_USER
	global _SSH_DIR
	global _MAN_TMPL
	global _AG_TMPL
	global _INSTANCE_TYPE
	global _KEY_NAME
	global _SUBNET_NAME
	conf.read(SCENARIO_PATH)
	_SSH_USER=conf.get("AUTH", "ssh_user")
	_MAN_TMPL=conf.get("AP", "manager_template")
	_AG_TMPL=conf.get("AP", "agent_template")
	_INSTANCE_TYPE=conf.get("INSTANCE", "instance_type")
	_KEY_NAME=conf.get("INSTANCE", "key_name")
	_SUBNET_NAME=conf.get("INSTANCE", "subnet_name")

def save_scenario():
        global _SSH_USER
        global _MAN_TMPL
        global _AG_TMPL
        global _INSTANCE_TYPE
        global _KEY_NAME
        global _SUBNET_NAME
	try:
                conf.set("AUTH", 'ssh_user', _SSH_USER)
                conf.set("AP", 'manager_template', _MAN_TMPL)
                conf.set("AP", 'agent_template', _AG_TMPL)
                conf.set("INSTANCE", 'instance_type', _INSTANCE_TYPE)
                conf.set("INSTANCE", 'key_name', _KEY_NAME)
                conf.set("INSTANCE", 'subnet_name', _SUBNET_NAME)
        	conf.write(open(SCENARIO_PATH, 'w'))
	except Exception as e:
		log.error( str(type(e)) + str(e.args) + e.message)

def set_scenario(path):
	global SCENARIO_PATH
	SCENARIO_PATH=path

