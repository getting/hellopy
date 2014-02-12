'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class HanoiLabelFilterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.buyer_nick = None
		self.label_id = None
		self.seller_nick = None

	def getapiname(self):
		return 'taobao.hanoi.label.filter'
