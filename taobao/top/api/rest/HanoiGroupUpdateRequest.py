'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class HanoiGroupUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.description = None
		self.gmt_modified = None
		self.group_code = None
		self.id = None
		self.name = None
		self.open = None
		self.scene = None
		self.type = None

	def getapiname(self):
		return 'taobao.hanoi.group.update'
