import datetime
import configparser
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from cy.common_code.GmailReceiver import GmailReceiver
from cy.common_code.GoogleOauth2 import Get_Gmail_API_Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep
import re  # regular expression


class Base:
    def __init__(self):
        CURRENT_DIR = os.path.abspath(__file__)
        PARENT_DIR = os.path.dirname(CURRENT_DIR)
        CY_DIR = os.path.dirname(PARENT_DIR)

        self.config_path = os.path.join(CY_DIR, "config", 'config.ini')
        # print(self.config_path)
        self.test = PARENT_DIR + '\cy\config\config.ini'

    @staticmethod
    def timestamp():
        datetime.datetime.now()
        datetime_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return datetime_str

    def read_ini(self, section):
        ini_result = {}
        config = configparser.ConfigParser()
        config.read(self.config_path)
        ini_file = config.items(section)
        # print(ini_file)
        for items in ini_file:
            ini_result.setdefault(str(items[0]), str(items[1]))
        # print(ini_result)
        return ini_result

    @staticmethod
    def read_env_ini(section, env='sit'):
        ini_result = {}
        config = configparser.ConfigParser()
        config.read(rf'../config/{env}_env.ini')
        ini_file = config.items(section)
        for items in ini_file:
            ini_result.setdefault(str(items[0]), str(items[1]))
        # print(ini_result)
        return ini_result

    @staticmethod
    def path():
        CURRENT_DIR = os.path.abspath(__file__)
        PARENT_DIR = os.path.dirname(CURRENT_DIR)
        CY_DIR = os.path.dirname(PARENT_DIR)
        return CY_DIR

    @staticmethod
    def wait_element_display(driver, locator, time=15):
        try:
            # from selenium.webdriver.common.by import By
            # (By.XPATH, f".//span[text()='{i18n.t('Cigna_TW.500_review_bt1')}']")
            WebDriverWait(driver, time, 2).until(EC.presence_of_element_located(locator))

        except Exception as e:
            print(e)
            raise

    def wait_element_clickable(self, driver, locator, time=15):
        try:
            WebDriverWait(driver, time, 1).until(EC.element_to_be_clickable(locator))

        except Exception as e:
            print(e)
            raise

    @staticmethod
    def getElementExistanceById(driver, locators):
        # 確認元素是否存在
        element_existance = True

        try:
            # 找不到會噴異常
            element = driver.find_element(locators)
        except:
            element_existance = False

        return element_existance

    def reset_passwd_mail(self, mail_title, usermail, env, passwd):
        mail_receiver = GmailReceiver("sit")
        html = mail_receiver.get_gmail_html(msg_to=usermail,
                                            msg_subject=rf"[{env}]Platform - " + str(mail_title))
        maillink = re.findall(r'https://\w+.ct.sendgrid.net/\w+/click\?upn=[a-zA-Z0-9_-]+', html)
        redirect_maillink = requests.get(str(maillink[0]))
        print(redirect_maillink.url)

        if env == 'uat':
            regex = re.findall('cy.*', str(redirect_maillink.url))
            verifylink = 'https://admin@' + str(regex[0])
        else:
            verifylink = redirect_maillink.url

        driver = webdriver.Chrome('../chromedriver')
        driver.get(str(verifylink))
        # print(verifylink)
        driver.implicitly_wait(15)
        sleep(1)
        driver.find_element(By.ID, 'set-password-input').send_keys(passwd)
        driver.find_element(By.ID, 'set-confirm-password-input').send_keys(passwd)
        driver.find_element(By.XPATH, "//div[contains(text(), 'Set your password')]").click()
        driver.find_element(By.XPATH, "//span[text()='Set password']").click()
        sleep(5)
        driver.close()

    @staticmethod
    def check_mail(mail_title, usermail, env):
        mail_receiver = GmailReceiver("sit")
        content = mail_receiver.get_gmail_content(msg_to=usermail,
                                                  msg_subject=rf"[{env}]Platform - " + str(mail_title))
        re_content = re.sub(r'(\n){1,}', '\n', content) # 多餘1個 \n換行替換成1個
        print(re_content)
        return re_content
