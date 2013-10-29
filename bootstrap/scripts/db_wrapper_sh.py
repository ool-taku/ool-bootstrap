#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import db_wrapper

argvs = sys.argv

if argvs[1] == 'stacks':
	db_wrapper.insert_stacks(argvs[2], argvs[3], argvs[4], argvs[5], argvs[6], argvs[7])
if argvs[1] == 'stacks_del':
	db_wrapper.delete_stack(argvs[2])
elif argvs[1] == 'scenarios_in':
	db_wrapper.insert_scenarios(argvs[2], "0")
elif argvs[1] == 'scenarios_up':
	db_wrapper.update_scenarios(argvs[2], argvs[3])
