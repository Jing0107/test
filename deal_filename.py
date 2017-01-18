#!/usr/local/bin/python
#coding:utf-8
#build by xujingjing  
#2017-01-17

import os
files = os.listdir(".")
for filename in files:
	portion = os.path.splitext()
	if portion[1] = ".vir"
		newname = portion[0] + ".exe"
		os.rename(filename,newname)