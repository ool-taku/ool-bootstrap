#!/usr/bin/env python
import os
import cgi
import cgitb; cgitb.enable()

def template_list():
        print "<select name=\"example\" size=\"1\">"
	senarios = os.listdir("../configure")
	for config in senarios:
                print "<option name=scenario value=\"%s\">%s</option>" % (config, config)
        print "</select>"

def main():
	print "Content-type: text/html\n"
	print "<html><body>"
	print """<form action="bootstrap.py" method="post">"""
	print "<center>"
	print "Bootstrap Top Page.<br>"
        if os.environ.has_key('HTTP_HOST') and os.environ.has_key('REQUEST_URI'):
                url = "http://" + os.environ['HTTP_HOST'] + os.environ['REQUEST_URI']
                print url
	print "<table border=\"0\">"
	print "<tr>"
	print "<th>Execute Scenario</th>"
	print "<th>"
	template_list()
	print "</th>"
	print "</table>"
	print "</from>"
	print "</body></html>"


if __name__ == "__main__":
    main()


f = cgi.FieldStorage()
print f.getfirst("scenario")      
