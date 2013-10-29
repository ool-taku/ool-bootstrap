#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scenario

scenario.set_scenario("/home/openstack/bootstrap/configure/base")
scenario.read_scenario()

print scenario._SSH_USER
print scenario._SSH_DIR

print scenario._MAN_TMPL
print scenario._AG_TMPL

print scenario._INSTANCE_TYPE
print scenario._KEY_NAME
print scenario._SUBNET_NAME

