#! /usr/bin/env python  
#coding=utf-8
from collections import OrderedDict  
from pyexcel_xls import get_data  
from pyexcel_xls import save_data 
import urllib.request
from urllib.parse import quote

def download_little_file(from_url,to_path):
	from_url = quote(from_url, safe='/:?=')
	conn = urllib.request.urlopen(from_url)
	f = open(to_path,'wb')
	f.write(conn.read())
	f.close()

def read_xls_file():  
	xls_data = get_data(r"data.xlsx")  
	for sheet_n in xls_data.keys():
		data=xls_data[sheet_n]
	for i in range(1,len(data)):
		print (data[i][0])
		download_little_file(data[i][15],'mp3/'+data[i][0]+'.mp3')

if __name__ == '__main__':  
    read_xls_file()  
