'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class CrmMembersGroupsBatchdeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_ids = None
		self.group_ids = None

	def getapiname(self):
		return 'taobao.crm.members.groups.batchdelete'
