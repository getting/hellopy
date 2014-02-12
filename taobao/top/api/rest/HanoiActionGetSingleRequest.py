'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class HanoiActionGetSingleRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.action_code = None
		self.id = None
		self.name = None

	def getapiname(self):
		return 'taobao.hanoi.action.get.single'
