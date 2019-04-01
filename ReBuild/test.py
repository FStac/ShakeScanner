#!/usr/bin/python
#-*- coding:utf-8 -*-
import nmap
import optparse

def scan(tgtHost,tgtPort):
	nm = nmap.PortScanner()
	arguments='-Pn -O -sV '
	i = tgtPort
	s = nm.scan(tgtHost,tgtPort,arguments)
	try:
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
	if nm[tgtHost]['tcp'][int(i)]['state'] == 'open':
		print ScanResult1
	elif nm[tgtHost]['tcp'][int(i)]['state'] == 'filtered'or 'closed':
		print ScanResult2

def main():
	parser = optparse.OptionParser('usage%prog -H <target host> -P <target ports> ')
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	parser.add_option('-P',dest='tgtPorts',type='string',help='specify target port')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = options.tgtPorts
	try:
		Portlist = options.tgtPorts.strip(',').split(',')
		if (tgtHost ==None) | (Portlist[0]==None):
			print parser.usage
		for tgtPort in Portlist:
			scan(tgtHost,tgtPort)
	except Exception:
		print parser.usage

	#for tgtPort in Portlist:
		#scan(tgtHost,tgtPort)

if __name__ == '__main__':
	main()