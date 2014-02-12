'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class TmallEaiOrderRefundBillsumGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bill_type = None
		self.end_time = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'tmall.eai.order.refund.billsum.get'
