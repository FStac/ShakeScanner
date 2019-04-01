#!/usr/bin/python
#-*- coding:utf-8 -*-
import nmap


def scan(tgtHost,tgtPort):
	# set up port scanner
	nm = nmap.PortScanner()
	# set argument as default, this value are not support to define in this version, it probably add this function in next version :)
	arguments='-Pn -O -sV '
	# save port number at i value
	i = tgtPort
	# create a scan 
	s = nm.scan(tgtHost,tgtPort,arguments)
	try:
		# check does not have operation system characteristic , if it does  , show it on screen
		Operation_system=nm[tgtHost]['osmatch'][0].get('osclass')[0].get('osfamily')
		print "\033[1;42;40m [+] \033[0m" + 'Operation Plantform Maybe :'+"\033[1;42;40m "+ Operation_system +"\033[0m"
	except Exception:
		pass
	ScanResult1="\033[1;42;40m [+] \033[0m" + 'Target Host: \033[1;33;40m['+ tgtHost + ']\033[0m state:\033[1;33;40m[' + nm[tgtHost].state() + ']\033[0m'  \
	+ ' | Target Port: \033[1;33;40m['+ i + ']\033[0m state: \033[1;33;40m['+  nm[tgtHost]['tcp'][int(i)]['state'] +']\033[0m |'\
	+ ' Target Service :\033[1;33;40m['+ nm[tgtHost]['tcp'][int(i)]['name']  +']\033[0m'  \
	+ ' Target Product :\033[1;33;40m['+ nm[tgtHost]['tcp'][int(i)]['product']+']\033[0m Version: \033[1;33;40m[' +nm[tgtHost]['tcp'][int(i)]['version']+']\033[0m'

	ScanResult2="\033[1;42;40m [+] \033[0m" + 'Target Host: \033[1;33;40m['+ tgtHost + ']\033[0m state:\033[1;33;40m[' + nm[tgtHost].state() + ']\033[0m'  \
	+ ' | Target Port: \033[1;33;40m['+ i + ']\033[0m state: \033[1;33;40m['+  nm[tgtHost]['tcp'][int(i)]['state'] +']\033[0m | '\
	+ 'Target Service :\033[1;33;40m['+ nm[tgtHost]['tcp'][int(i)]['name']  +']\033[0m' 
	# check port state does not open , if it does, show product infomation and current version
	if nm[tgtHost]['tcp'][int(i)]['state'] == 'open':
		print ScanResult1
	# if port state are filtered or closed just print result on screen
	elif nm[tgtHost]['tcp'][int(i)]['state'] == 'filtered'or 'closed':
		print ScanResult2
