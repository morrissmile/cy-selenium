# import sys
# sys.path.append('../code')

import re  #regular expression
from cy.code.internal_API import *
from cy.common_code.GmailReceiver import *
from cy.common_code.common import *
from cy.common_code.GoogleOauth2 import Get_Gmail_API_Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from cy.code.create_account_ini import *


#
# class test_create_account():
#     # createacc = Test_cy(envside='sit', scanurl='https://stage-care.rightest.com/login') #input scan url  =>  scanurl=' ', envside='sit',language_id=1  1=en 2=zh_tw
#     createacc = Create_acc(envside='sit', language_id=1)  # input scan url  =>  scanurl=' ', envside='sit'  language_id=1  1=en 2=zh_tw
#     createacc.create_account()
#     sleep(5)
#     createacc.verify_mail()
#     createacc.write_ini()










