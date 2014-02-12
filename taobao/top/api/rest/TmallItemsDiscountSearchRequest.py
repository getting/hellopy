'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class TmallItemsDiscountSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auction_tag = None
		self.brand = None
		self.cat = None
		self.end_price = None
		self.post_fee = None
		self.q = None
		self.sort = None
		self.start = None
		self.start_price = None

	def getapiname(self):
		return 'tmall.items.discount.search'
