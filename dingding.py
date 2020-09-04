#王智
import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=98247d54b0b3569dab7db6658b08c3625112872ac63119bd1df653f5771046e6'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('执行完毕')
        },
        "at":{
            "atMobiles":[
                "13033795363"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()
