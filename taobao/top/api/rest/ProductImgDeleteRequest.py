'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class ProductImgDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.product_id = None

	def getapiname(self):
		return 'taobao.product.img.delete'
