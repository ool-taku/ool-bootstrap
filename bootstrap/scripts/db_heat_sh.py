#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import log
import db_heat

argvs = sys.argv
if argvs[1] == 'select':
	rows=db_heat.select(db_heat.get_sql_connection(), argvs[2])
	ret=""
	for row in rows:
		if len(ret):
			ret+=" "
		ret+=str(row[0])
	sys.stdout.write(ret)
