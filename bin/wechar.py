#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import weixinbaojing



if __name__ == '__main__':
    print(sys.argv)
    send = weixinbaojing.ZabbixSendMail(sys.argv[1:])
    send.send_mail()
