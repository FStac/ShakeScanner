#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import os

try:
	def directoryScan(url,directory):
		# open file
		f = open(directory,'r')
		# travel every line in dictfile,save the results in buffer
		lines = f.readlines()
		# read every line in buffer
		for line in lines:
			
			# save test directory name
			direct = line
			# connect url with test directory 
			directPayload = url + str(direct)
			# strip 
			directPayload = directPayload.strip('\n')
			# send a request with http-get to test url which have test url path
			response = requests.get(directPayload,headers={'Connection': 'close'})
			i = 0
			# check response code does not 200, if it does, save to log
			if response.status_code == 200:
				# show current test url path
				print '['+i+'/446875]'+'[+] ' + directPayload+"     |      status:\033[1;33;40m  %s \033[0m" % response.status_code
				i=i+1
				# open log file
				a = open('log','a')
				# save url path to log file
				a.write(directPayload + '\n')
				# close file
				a.close()
			else:
				# if response code not 200 then just show it on screen
				print '['+bytes(i)+'/446875]'+'[*] Testing:' + directPayload
				i=i+1
		f.close()
except Exception:
	pass