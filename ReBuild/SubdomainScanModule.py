#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import os

def subDomainScan(d,dict):
	# open dictionary file
	f = open(dict,'r')
	lines = f.readlines()
	# read every line in dictionary
	for line in lines:
		subdomain = line
		subdomain = subdomain.replace('\r','').strip('\n')
		test_payload = "http://"+subdomain+'.'+d
		print test_payload

if __name__ == '__main__':
	subDomainScan('360.cn','dic.txt')