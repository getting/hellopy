'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class SpmeffectGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.date = None
		self.module_detail = None
		self.page_detail = None

	def getapiname(self):
		return 'taobao.spmeffect.get'
