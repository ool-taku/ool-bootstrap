#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os
import log

_db_path=os.getcwd() + "/../db/bootstrap.db"

def execute(sql):
	con=sqlite3.connect(_db_path)
	cur=con.cursor()
	log.debug(sql)
	cur.execute(sql)
	try:
        	con.commit()
	finally:	
		cur.close()
		con.close()

def select(sql):
	log.debug(sql)
        con=sqlite3.connect(_db_path)
	try:
		cur=con.execute(sql)
		ret=cur.fetchall()
		log.debug(ret)
	finally:
		cur.close()
		con.close()
	return ret

def connect():
	return sqlite3.connect(_db_path)

_is_new = not os.path.exists(_db_path)
if _is_new:
	con=sqlite3.connect(_db_path)
	cur = con.cursor()
	cur.execute("""create table stacks (
	             id integer primary key  autoincrement not null,
	             uuid text not null,
	             deleted bool default 0,
	             scenario text not null,
	             ip text not null,
	             netns text,
	             manager bool default 0,
		     host text)""")

	cur.execute("""create table scenarios (
	             scenario text primary key not null,
	             status integer default 0)""")
	con.commit()
	con.close()
