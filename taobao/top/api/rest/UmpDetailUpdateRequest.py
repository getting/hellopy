'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class UmpDetailUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None
		self.detail_id = None

	def getapiname(self):
		return 'taobao.ump.detail.update'
