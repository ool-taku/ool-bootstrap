#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import db_manager 
import db_wrapper
import credentials
argvs = sys.argv
import log

ret=db_manager.select(argvs[1])

for row in ret:
	print row

#db_manager.execute(argvs[1])
