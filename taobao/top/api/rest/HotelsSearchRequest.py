'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class HotelsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.city = None
		self.country = None
		self.district = None
		self.domestic = None
		self.name = None
		self.page_no = None
		self.province = None

	def getapiname(self):
		return 'taobao.hotels.search'
