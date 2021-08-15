# import sys
# sys.path.append('../code')

import re  # regular expression
from cy.code.internal_API import Login
from cy.common_code.GmailReceiver import GmailReceiver
from cy.common_code.common import Base
from cy.common_code.GoogleOauth2 import Get_Gmail_API_Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from time import sleep
import requests


class Create_acc():
    def __init__(self, mail='timestamp', scanurl='https://www.example.com', password='Aa12345678',
                 section='internalAPI', language_id=1):
        self.scanurl = scanurl
        self.password = password
        # self.envside =envside
        self.section = section
        self.language_id = language_id
        self.mail = mail
        base = Base()
        self.timeformat = base.timestamp()
        self.time = base.timestamp()
        self.test_env = base.read_ini('testenv')  # input section
        self.envside = self.test_env['env']

        if self.mail == 'timestamp':
            self.usermail = 'mo' + str(self.timeformat) + '@gmail.com'

        else:
            self.usermail = str(self.mail) + '@gmail.com'

    def create_account(self):
        superacc = Login(envside=self.envside, section=self.section)
        superacc.signinapi()
        print(self.scanurl)
        superacc.create_userid(self.scanurl)
        create_user = superacc.createuseraccount(self.usermail)
        print("scan url", self.scanurl)
        # assert create_user == 'create user pass'

    def verify_mail(self):
        # global userpasswd
        # userpasswd = 'Aa12345678'
        invitemail = GmailReceiver("sit")
        html = invitemail.get_gmail_html(msg_to=self.usermail,
                                         msg_subject=rf"[{self.envside}]platform - invitation")
        maillink = re.findall(r'https://\w+.ct.sendgrid.net/\w+/click\?upn=[a-zA-Z0-9_-]+', html)
        redirect_maillink = requests.get(str(maillink[0]))
        print(redirect_maillink.url)

        if self.envside == 'uat':
            regex = re.findall('cy.*', str(redirect_maillink.url))
            verifylink = 'https://' + str(regex[0])
        else:
            verifylink = redirect_maillink.url

        driver = webdriver.Chrome('../chromedriver')
        driver.get(str(verifylink))
        # print(verifylink)
        driver.implicitly_wait(15)
        sleep(1)
        driver.find_element(By.ID, 'set-password-input').send_keys(self.password)
        driver.find_element(By.ID, 'set-confirm-password-input').send_keys(self.password)
        driver.find_element(By.XPATH, "//div[contains(text(), 'Set your password')]").click()
        driver.find_element(By.XPATH, "//span[text()='Set password']").click()
        sleep(5)
        driver.close()


    def user_signin(self):

        driver = webdriver.Chrome(executable_path='../chromedriver')
        driver.get('https://')
        driver.implicitly_wait(15)
        driver.find_element(By.ID, 'login-email-input').send_keys(self.usermail)
        driver.find_element(By.ID, 'login-password-input').send_keys(self.password)
        driver.find_element(By.XPATH, "//span[text()='Log in']").click()
        sleep(10)
        return self.usermail


    def write_ini(self):
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        sleep(1)
        config['account']['mail'] = self.usermail
        config['account']['password'] = self.password
        config['account']['scanurl'] = self.scanurl
        with open('../config/config.ini', mode='w') as configfile:
            config.write(configfile)


if __name__ == "__main__":
    signup = Create_acc()
    """input scan url  =>  scanurl='https://', mail ='none' => timestamp"""
    signup.create_account()
    sleep(5)
    signup.verify_mail()
    signup.write_ini()
    sleep(2)