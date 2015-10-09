#coding=utf-8
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import socket
import time
import requests
import random
from tornado.options import define, options
from tornado import httpclient, gen, ioloop, queues
import datetime
import re
import sys
import json
from bs4 import BeautifulSoup
import multiprocessing
define("port", default=9999, help="run on the given port", type=int)

reload(sys)
sys.setdefaultencoding('utf8')
upload_path = '/root/xia/tornado-4.2.1/demos/helloworld/upload'
download_path = '/root/xia/tornado-4.2.1/demos/helloworld/download'
global list 
list = []
global path
path = ''
global dic
dic = {}
global filename
filename = ''
global probe_list
probe_list = []


#global total_time 
total_time = 0.00


def get_status(url):
        #start=time.time()
	s = requests.Session()
	#try:
	r = s.get(url, allow_redirects = True,headers=headers,timeout=30)
        #end = time.time()       
	#r.elapsed.microseconds        
	#except:
	#	return url,r.raise_for_status(),r.elapsed.microseconds/1000000.00000,r.text

	return url,r.status_code,r.elapsed.microseconds/1000000.00000,r.text#, r.headers
def pachong(url,i):
	#global dic	
#	dic = {}
	global probe_list
	global total_time
	probe_list1 = []
	try:
		tuple = get_status(url)
	except :
		dic['local_time'] = str(i)
		dic['url'] = url
		dic['http_code'] = '0'
		dic['probe_time'] = '0'
		dic['main'] = '1'
		probe_list1.append(dic)
		dic = {}
	#output.write('<span style="color:blue">'+str(i)+' || '+tuple[0]+' || '+str(tuple[1])+' || '+str(tuple[2])+'</span>'+'\n')
	dic['local_time'] = str(i)
	dic['url'] = tuple[0]
	dic['http_code'] = str(tuple[1])
	dic['probe_time'] = str(tuple[2])
	dic['main'] = '1'
	probe_list1.append(dic)
	print probe_list1,333
	dic = {}
	#global total_time
	total_time += float(tuple[2])
	soup = BeautifulSoup(tuple[3])

	link = soup.find_all('link')
	for link_url in link:
		href = link_url.get('href')
		#print 'href=',href
		if href:
			if 'http' not in href:
				href = list[url]+href
			try:
				data = get_status(href)
			except :
				dic['local_time'] = str(i)
				dic['url'] = href
				dic['http_code'] = '0'
				dic['probe_time'] = '0'
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
			#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
			dic['local_time'] = str(i)
			dic['url'] = data[0]
			dic['http_code'] = str(data[1])
			dic['probe_time'] = str(data[2])
			dic['main'] = '0'
			probe_list1.append(dic)
			dic = {}
			#global total_time
			total_time += float(data[2])
			#print 'total_time=',total_time
	img = soup.find_all('img')
	for picture in img:
		#print picture,1111111,type(picture)
		if 'data-original-src' in str(picture):
			link = picture.get('data-original-src')
			if link:
				if 'http:' not in link:
					link = list[url]+link
	#			print 'link=',link
				
				try:
					data = get_status(link)
				except :
					dic['local_time'] = str(i)
					dic['url'] = link
					dic['http_code'] = '0'
					dic['probe_time'] = '0'
					dic['main'] = '0'
					probe_list1.append(dic)
					dic = {}
				#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = str(data[1])
				dic['probe_time'] = str(data[2])
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
				total_time += float(data[2])
			#	print 'total_time=',total_time
		elif 'data-original' in str(picture):
			link = picture.get('data-original')
			if link:
				if 'http:' not in link:
					link = list[url]+link
	#			print 'link=',link
				
				try:
					data = get_status(link)
				except :
					dic['local_time'] = str(i)
					dic['url'] = link
					dic['http_code'] = '0'
					dic['probe_time'] = '0'
					dic['main'] = '0'
					probe_list1.append(dic)
					dic = {}
				#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = str(data[1])
				dic['probe_time'] = str(data[2])
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
				total_time += float(data[2])
		elif 'src2' in str(picture):
			link = picture.get('src2')
			if link:
				if 'http:' not in link:
					link = list[url]+link
				
				try:
					data = get_status(link)
				except :
					dic['local_time'] = str(i)
					dic['url'] = link
					dic['http_code'] = '0'
					dic['probe_time'] = '0'
					dic['main'] = '0'
					probe_list1.append(dic)
					dic = {}
				#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = str(data[1])
				dic['probe_time'] = str(data[2])
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
				total_time += float(data[2])
			#	print 'total_time=',total_time
				
		elif 'data-src' in str(picture):
			link = picture.get('data-src')
			if link:
				if 'http:' not in link:
					link = list[url]+link
				
				try:
					data = get_status(link)
				except :
					dic['local_time'] = str(i)
					dic['url'] = link
					dic['http_code'] = '0'
					dic['probe_time'] = '0'
					dic['main'] = '0'
					probe_list1.append(dic)
					dic = {}
				#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = str(data[1])
				dic['probe_time'] = str(data[2])
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
				total_time += float(data[2])
			#	print 'total_time=',total_time
		else:
			link = picture.get('src')
			if link:
				if 'http:' not in link:
					link = list[url]+link
	#			print 'link=',link
				
				try:
					data = get_status(link)
				except :
					dic['local_time'] = str(i)
					dic['url'] = link
					dic['http_code'] = '0'
					dic['probe_time'] = '0'
					dic['main'] = '0'
					probe_list1.append(dic)
					dic = {}
				#output.write(str(i)+' || '+data[0]+' || '+str(data[1])+' || '+str(data[2])+'\n')
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = str(data[1])
				dic['probe_time'] = str(data[2])
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
				#global total_time
				total_time += float(data[2])
			#	print 'total_time=',total_time
	script = soup.find_all('script')
	for src in script:
		link = src.get('src')
	#	print 'link=',link
		if link:
			
			try:
				data = get_status(link)
			except :
				dic['local_time'] = str(i)
				dic['url'] = link
				dic['http_code'] = '0'
				dic['probe_time'] = '0'
				dic['main'] = '0'
				probe_list1.append(dic)
				dic = {}
			#output.write(str(i)+' || '+str(data[0])+' || '+str(data[1])+' || '+str(data[2])+'\n')
			dic['local_time'] = str(i)
			dic['url'] = data[0]
			dic['http_code'] = str(data[1])
			dic['probe_time'] = str(data[2])
			dic['main'] = '0'
			probe_list1.append(dic)
			dic = {}
			#global total_time
			total_time += float(data[2])
			#print 'total_time=',total_time
	#probe_list[count]['probe_time'] = total_time
	for i in probe_list:
		if i['url']  == list[url]:
			i['probe_time'] = total_time
#			op = open(path)
#			for (num,value) in  enumerate(op):
#				if ' || '  in value:
#					if value.split(' || ')[1] == list[url]:
#						#print 1111111,total_time,list[url]
#						#modifyip(path,value.split(' || ')[3].split('<span>')[0],str(total_time+float(value.split(' || ')[3].split('</span>')[0]))+'</span>'+'\n')
#						modifyip(path,value.split(' || ')[3].split('<span>')[0],str(total_time)+'</span>'+'\n')
#			op.close()
	total_time = 0.00
	probe_list[0:0] = probe_list1
	print 'probe_list ==',probe_list

useragent_list = [                                                                                                   
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6' ,
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) ',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)' ,    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)' ,
    'Opera/9.20 (Windows NT 6.0; U; en) ',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.1; .NET CLR 1.1.4322)' ,
    'Opera/9.00 (Windows NT 5.1; U; en)' ,
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50' ,
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0' ,
    'Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.02 [en]' ,
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20060127 Netscape/8.1' ,
    ]   
size = len(useragent_list)
useragent = useragent_list[random.randint(0, size-1)] 
headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;",
	"Accept-Encoding":"gzip",
	"Accept-Language":"zh-CN,zh;q=0.8",
	'User-Agent':useragent
	}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	self.render('templates/index.html',)

	#self.redirect('/upload')
class Show(tornado.web.RequestHandler):
    def get(self):
	jsonStr = json.dumps(probedata)
	#probe_list = []
	#probedata = {}
	self.render('templates/show.html',content=jsonStr)
    def post(self):
	jsonStr = json.dumps(probedata)
	#probe_list = []
	#probedata = {}
	self.render('templates/show.html',content=jsonStr)
class MainHandler1(tornado.web.RequestHandler):
    def get(self):
	#filename = download_path + '/result.txt'
	global path
	filename = path 
        with open(filename, "rb") as f:
            self.set_header('Content-Type','application/octet-stream')
            self.write(f.read())
    def post(self):
        #Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        #self.set_header ('Content-Type', 'application/octet-stream')
        #self.set_header ('Content-Disposition', 'attachment; filename='+'')
	#filename = download_path + '/result.txt'
	global path
	filename = path 
        #读取的模式需要根据实际情况进行修改
        with open(filename, 'rb') as f:
            while True:
                readdata = f.readline()
                if not readdata:
                    break
                self.write(readdata)
		self.write('<br>')
        #记得有finish哦
	self.finish()

class UploadFileHandler(tornado.web.RequestHandler): 
	def get(self):
#        self.write('''
#        <html>
#          <head><title>Upload File</title></head>
#          <body>
#            <form action='upload' enctype="multipart/form-data" method='post'>
#            <input type='file' name='file'/><br/>
#            <input type='submit' value='submit'/>
#            </form>
#          </body>
#        </html>
#        ''')
		self.render('templates/upload.html',)
#
	def post(self):
		#文件的暂存路径
		#upload_path=os.path.join(os.path.dirname(__file__),'files')  
		#提取表单中‘name’为‘file’的文件元数据
		file_metas=self.request.files['file']    
		for meta in file_metas:
			global upload_filename
			upload_filename=meta['filename']
			#global filepath
			filepath=os.path.join(upload_path,upload_filename)
			#有些文件需要已二进制的形式存储，实际中可以更改
			with open(filepath,'wb') as w:
				w.write(meta['body'])
		with open(filepath,'r') as f:
			try:
				for line in f:
					line=line.strip()
					if line.find('http')>-1:
						#self.write(line)
						#self.write('<br>')
						list.append(line)
			except:
				self.write('check your file!')
				return
		#self.redirect('/')
		t = datetime.datetime.now()
		#t = filter(str.isdigit,str(t))
		#global path
		#path = download_path+'/'+upload_filename.split('.')[0]+'/'+str(t).strip()+'.txt'
	#	with open(path,'w') as wr:
	#		wr.write('<h3>data begin......</h3>')
	#		wr.write('<pre><h3 style="color:blue">local_time		||url			||http_code||probe_time</h3></pre>')
		global dic
		global probe_list
		global total_time
		#try:
		#	os.makedirs(download_path+'/'+upload_filename.split('.')[0])
		#except:
		#	pass
		probe_data = {}
		probe_data['data'] = probe_list
		probe_data['version'] = '1.0'
		pool = multiprocessing.Pool(processes=14)
		#with open(path,'w') as output:
			#output.write('<h3>data begin......</h3>')
			#output.write('<pre><h3 style="color:blue">local_time		||url			||http_code||probe_time</h3></pre>')
		for url in range (0,len(list)):
			i = datetime.datetime.now()
			pool.apply_async(pachong, (list[url],i))
		pool.close()
		pool.join()
		print probe_list,222
		list[:] = []	
		#global probedata
		#print probedata['version'],probe_list[0]
		json_str = json.dumps(probe_data)
		#probe_list =[]
		#probe_data = {}
		self.render('templates/show.html',content=json_str)

#@async
def main():
	tornado.options.parse_command_line()
	settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"tempalte_path": os.path.join(os.path.dirname(__file__), "templates"),
	"cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
	"login_url": "/login",
	"xsrf_cookies": False,
	} 
	application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/upload", UploadFileHandler),
		#(r"/download",MainHandler1),
		(r"/download",Show),
	#	(r"/show",Show),
		(r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),

	
	],**settings)


	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()

def modifyip(tfile,sstr,rstr):
    try:
        lines=open(tfile,'r').readlines()
        flen=len(lines)-1
        for i in range(flen):
            if sstr in lines[i]:
                lines[i]=lines[i].replace(sstr,rstr)
        open(tfile,'w').writelines(lines)
    
    except Exception,e:
        print e
if __name__ == "__main__":

    main()

