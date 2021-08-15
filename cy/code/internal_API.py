import requests
import json
from time import sleep
import configparser
from cy.common_code.common import Base

class Login():
    def __init__(self, email="superuser", password="password", envside='sit', section='internalAPI', language_id=1):
        #read ini for env
        self.envside = envside
        self.section = section
        self.language_id = language_id
        readapi_ini = Base()
        global ini_url
        ini_url = readapi_ini.read_env_ini(self.section, self.envside)  #帶入 使用環境跟讀取資料的section
        self.internalURL = ini_url['loginapi']
        self.email = str(email)
        self.password = str(password)

        if self.envside == 'uat':
            self.industry = 22
        else:
            self.industry = 1

    def signinapi(self):
        body = {"email": self.email, "password": self.password}

        headers = {
            'Content-Type': 'application/json',
                   }
        postsignapi = requests.post(self.internalURL, headers=headers, json=body)
        apicookie = postsignapi.cookies #將 cookie 存入變數
        # print(apicookie)  # 印出全部 cookie
        # print(apicookie["INTERNAL-ACCESS-TOKEN"])
        print('sign in api  ', postsignapi.json)
        print('superuserlogin', postsignapi.status_code)

        global access_token   #  1.
        access_token = apicookie["INTERNAL-ACCESS-TOKEN"]
        result = postsignapi.json()  # 將 response 存入變數

        # print('response', result)   # 印出全部 response
        # print(result["email"]) #抓特定欄位的 值 因為整個是dic 輸入key值可以拿到value

    def create_userid(self, curl="https://www.example.com"):
        createapi = ini_url['create']
        body = {
                "customer_name": "Cname_Test",
                "customer_url": curl,
                "industry_id": self.industry,
                "size_id": 1
                }

        headers = {
             'Content-Type': 'application/json',
                  }
        cookies = {"INTERNAL-ACCESS-TOKEN": access_token}

        postcreateuserapi = requests.post(createapi, headers=headers, json=body, cookies=cookies)
        cuserresult = postcreateuserapi.json()
        print(cuserresult)
        global custmerid
        custmerid = cuserresult['data']['id']
        print('custmerid=   ', custmerid)
# write id to config.ini
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        config['account']['id'] = str(custmerid)
        with open('../config/config.ini', mode='w') as configfile:
            config.write(configfile)
 #=====================================
        return custmerid

    def createuseraccount(self, mail, fristname='Testq', lastname='Example'):
        create_user_api = ini_url['userapino']
        body = {
                "customer_id": custmerid,
                "first_name": fristname,
                "last_name": lastname,
                "email": mail,
                # "language_id": self.language_id
                }
        headers = {
            'Content-Type': 'application/json',
                  }
        cookies = {"INTERNAL-ACCESS-TOKEN": access_token}

        createuser = requests.post(create_user_api, headers=headers, json=body, cookies=cookies)

        account_result= createuser.json()
        print(account_result['status'])
        sleep(1)
        assert account_result['status'] == 0


    def check_PP(self, URL):

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/88.0.4324.104 Safari/537.36 ',
                   'Host': 'www.123.global'
                   # "User-Agent": "python-requests/2.20.1"
        }
        createuser = requests.get(URL, headers=headers)
        print(createuser)
        if 'https://' in createuser.text:
            print('pass')
        else:
            print('fail')





