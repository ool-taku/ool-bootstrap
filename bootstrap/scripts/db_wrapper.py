#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import db_manager 

def insert_stacks(uuid, scenario, ip, netns, manager, host):
	sql=u"insert into stacks(uuid, scenario, ip, netns, manager, host) values (""'" + uuid + "', '" + scenario + "', '" + ip  + "', '" + netns  + "', '" + manager + "','" + host + "')"
	db_manager.execute(sql)

def delete_stack(uuid):
	sql=u"update stacks set deleted=1 where uuid='" + uuid  + "'"
	db_manager.execute(sql)

def insert_scenarios(scenario, status):
	sql=u"insert into scenarios(scenario, status) values (""'" + scenario + "', '" + status + "')"
	db_manager.execute(sql)

def update_scenarios(scenario, status):
        sql=u"update scenarios set status='" + status + "' where scenario='" + scenario + "'"
        db_manager.execute(sql)

def delete_scenario(scenario):
	sql=u"delete from scenarios where scenario='" + scenario + "'"
	db_manager.execute(sql)
