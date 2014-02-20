# coding=UTF-8
import json
from urllib import urlopen, urlencode


class BaiduTranslate():
    """百度翻译
    """
    #翻译接口地址
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate?'

    def __init__(self, client_id, q='', fm='auto', to='auto'):
        #Baidu API Key
        self.client_id = client_id
        #源语言语种
        self.fm = fm
        #目标语言语种
        self.to = to
        #要翻译的原文
        self.q = q

    def get_url(self):
        """
        获取查询结果返回地址
        """
        data = {
            'client_id': self.client_id,
            'from': self.fm,
            'to': self.to,
            'q': self.q,
        }
        return BaiduTranslate.url + urlencode(data)

    def translate(self, q, fm='auto', to='auto'):
        self.fm = fm
        self.to = to
        self.q = q
        response = urlopen(self.get_url())
        result = json.loads(response.read())
        if result.get('error_code', None):
            #当发生错误是抛出异常
            raise Exception(result['error_msg'])
        else:
            return result['trans_result'][0]['dst']