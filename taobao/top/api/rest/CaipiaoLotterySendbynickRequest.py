'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class CaipiaoLotterySendbynickRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.lottery_type_id = None
		self.stake_count = None
		self.sweety_words = None

	def getapiname(self):
		return 'taobao.caipiao.lottery.sendbynick'
