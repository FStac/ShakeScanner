#!/usr/bin/python
#-*- coding:utf-8 -*-

from ScannerModule import *
from DirectoryBruteModule import *
import optparse

print "======================================================"
print "|  \033[1;31;40m    Cautions: This version still in testing.      \033[0m|"
print "|  \033[1;31;40mShakeScanner Version:1.1 FStac@wearehackerone.com \033[0m| "
print "======================================================"

def main():
	# Create usage
	parser = optparse.OptionParser('usage%prog -H <target host> -P <target ports> -U <directory brute>')
	# add scanner module target host options
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	# add scanner module target port options
	parser.add_option('-P',dest='tgtPorts',type='string',help='specify target port')
	# add directory bruteforce module url options
	parser.add_option('-U',dest='url',type='string',help='specify target url')
	#add directory bruteforce module dictionary options  ===CAUTION===: There are a bug with -D options
	parser.add_option('-D',dest='directory',action='store_false',help='specify directory name') 
	(options,args) = parser.parse_args()
	# set target host
	tgtHost = options.tgtHost
	# set target port
	tgtPorts = options.tgtPorts
	# set url 
	url = options.url
	# set dictionary path
	directory = options.directory
	try:
		Portlist = tgtPorts.strip(',').split(',')
		if (tgtHost ==None) | (tgtPorts[0]==None):
			print parser.usage
		#ergodic target port in port list
		for tgtPort in Portlist:
			# create a scan
			scan(tgtHost,tgtPort)
	except Exception:
		pass
	if url != None:	
		# use default directionary
		if directory == None:
			directory = '/root/directory-list.txt'
			directoryScan(url,directory)
		else:
			# Will trigger a bug over here
			directory = options.directory
			directoryScan(url,directory)


if __name__ == '__main__':
	main()