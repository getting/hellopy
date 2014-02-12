'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class WangwangAbstractInitializeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None

	def getapiname(self):
		return 'taobao.wangwang.abstract.initialize'
