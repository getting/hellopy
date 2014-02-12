'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class AlipayPointOrderAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.memo = None
		self.merchant_order_no = None
		self.order_time = None
		self.point_count = None
		self.user_symbol = None
		self.user_symbol_type = None

	def getapiname(self):
		return 'alipay.point.order.add'
