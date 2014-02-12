'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class HotelOrderPayFeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.failed_reason = None
		self.message_id = None
		self.oid = None
		self.out_oid = None
		self.result = None
		self.session_id = None

	def getapiname(self):
		return 'taobao.hotel.order.pay.feedback'
