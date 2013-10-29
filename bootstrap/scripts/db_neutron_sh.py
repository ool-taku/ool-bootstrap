#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import log
import db_neutron

argvs = sys.argv
if argvs[1] == 'select':
	rows=db_neutron.select(db_neutron.get_sql_connection(), argvs[2])
	ret=""
	for row in rows:
		if len(ret):
			ret+=" "
		ret+=row[0]
	sys.stdout.write(ret)
