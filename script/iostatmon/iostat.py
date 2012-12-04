#!/usr/bin/env python

import sys
import os
import re
import getopt
import csv
FILENAME='/var/cache/snmp/iostat'
def usage():
	print "%s [Util|Index|DeviceDescr]"

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "")
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(1)
	
	if len(args) > 1:
		usage()
		sys.exit(1)
	
	if len(args) == 0:
		action = 'Util'
	else:
		action=args[0]
	
	if not os.path.exists(FILENAME):
		sys.exit(1)
	
	fin = open(FILENAME, 'rt')
	lines = fin.readlines()
	lines2 = [(i, lines[i]) for i in xrange(len(lines)) ]
	last = filter(lambda a: a[1].startswith('Device:'), lines2)
	if type(last) != type([]) and len(last) == 0:
		return
	lineno = last[-1][0]
	reader = csv.reader(lines[lineno:], delimiter=' ',skipinitialspace=True)
	header = reader.next()
	idxDevice = header.index('Device:')
	idxUtil =  header.index('%util')
	index = 0
	for row in reader:
		if len(row) <= max(idxDevice, idxUtil):
			continue
		if not re.match('^[h|s]d.$', row[idxDevice]):
			continue
		if action == 'Util':
			print row[idxUtil]
		elif action == 'Index':
			print index
			index += 1
		elif action == 'DeviceDescr':
			print row[idxDevice]

if __name__ == '__main__':
	main()
