#!/usr/bin/env python3


import requests
import json
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import my_logger


class ZabbixSendMail():
    def __init__(self,sys_argv):
        self.argv = sys_argv
        self.url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        self.value = {
            'corpid':"wx5a109e09d5044152",
            'corpsecret' : "0fiTLHoU0SBtNcBm4huzPILDt0QxjhdsVcnNBPVw9lVCR3vGVf7wf2p4HDTiilaQ"
        }
        self.sendmail_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
        self.access_resprons = requests.get(self.url, params=self.value)
        # self.token = json.loads(self.access_resprons.text)['access_token']
        self.respons = self.access_resprons.text  #获取返回结果


    def get_token(self):
        ret = json.loads(self.respons)
        return ret["access_token"]


    def send_mail(self):
        try:
            print(sys.path)
            send_mail_url = self.sendmail_url + "?access_token=%s"% self.get_token()
            payload = """{"touser": "%s",
                    "msgtype": "text",
                    "agentid": 1,
                    "text":{"content": "标题:%s\\n内容:%s"},"safe":0}""" % (self.argv[0], self.argv[1], self.argv[2])
            dic_payload = eval(payload)
            print(type(dic_payload))
            # ret = requests.post(send_mail_url, data=json.dumps(payload, ensure_ascii=False))

            ret = requests.post(send_mail_url, data=json.dumps(dic_payload, ensure_ascii=False).encode('UTF-8'))
            #发送中文时就需要ensure_ascii与.encode('utf-8')这两个参数配合才可以否则会报错
            print(ret.text)
        except Exception as e:
            # print(e)
            log = my_logger.MyLogger(e)
            log.savelog()

#
# if __name__ == "__main__":
#     send = ZabbixSendMail()
#     send.send_mail()
