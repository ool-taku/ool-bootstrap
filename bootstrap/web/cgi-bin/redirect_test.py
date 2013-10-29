#!/usr/bin/env python


import cgitb; cgitb.enable()
import subprocess

#print 'Location: http://www.google.co.jp/\n\n'
#print "Location: http://webings.net/sample/sample.html\n\n"


subprocess.call(['sudo', 'ip', 'netns', 'exec',
				'qdhcp-506a91fe-f08f-469f-837d-3a3579fb1f50',
				"/usr/bin/python", "/home/openstack/bootstrap/web/cgi-bin/scenario_request.py" , "ping"])


