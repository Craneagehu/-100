import json
import re
import requests
import urllib3
import time
urllib3.disable_warnings()

class KuaiDi100(object):

    def __init__(self,num):
        self.num = num
        self.code_url= 'https://m.kuaidi100.com/apicenter/kdquerytools.do?method=autoComNum&text={}'.format(self.num)
        self.index_url = f'https://m.kuaidi100.com/result.jsp?nu={self.num}'
        self.post_url = 'https://m.kuaidi100.com/query'

    #获取快递公司名
    def get_comCode(self):
        response = requests.get(self.code_url,verify=False)
        html = json.loads(response.text)
        comCode = html["auto"][0]['comCode']

        return comCode

    def get_csrftoken(self):
        response = requests.get(self.index_url, verify=False)
        cookies = response.headers["Set-Cookie"]
        csrftoken = re.findall('csrftoken=(.*?);',cookies,re.S)[0]

        return csrftoken

    def post(self):
        code = self.get_comCode()
        token = self.get_csrftoken()
        data = f'postid={self.num}&id=1&valicode=&temp=0.6532440784811175&type={code}&phone=&token=&platform=MWWW'

        post_headers = {
            'Host': 'm.kuaidi100.com',
            'Connection': 'keep-alive',
            'Content-Length': '103',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://m.kuaidi100.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; vivo X9 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.4.2',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #'Referer': f'https://m.kuaidi100.com/result.jsp?nu={self.num}&com={code}',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.9',
            'Cookie': f'csrftoken={token};Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c={int(time.time())},WWWID=WWW3245D723AFA7E7067FEA03AD77E7BB36; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1564562633,1566819248,1566868938,1566870642; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1566882549'
        }

        res = requests.post(self.post_url,data=data,headers=post_headers,verify=False)
        data = res.json()['data']

        context_list = []
        for each in data:
            context_dic = {}
            context_dic['time'] = each['time']
            context_dic['context'] = each['context']
            context_list.append(context_dic)

        return context_list


if __name__ == '__main__':
    num = '75170192491523'
    kd100 = KuaiDi100(num)
    result = kd100.post()
    print(result)





















