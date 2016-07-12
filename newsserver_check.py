#!/usr/bin/env python

# Checks if given server is a newsserver

import sys
import telnetlib
import socket

newsserver = sys.argv[1].rstrip('\n')
print newsserver, 

try:
	tn = telnetlib.Telnet(newsserver,119,5)
	waarde = tn.read_until("\n",3)
	print "---", waarde.split(',')[0]
	else:
		pass
except:
	print "Exception. Connection not OK."
