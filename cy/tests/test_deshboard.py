# import sys
# sys.path.append('../code')

import re  # regular expression
from cy.code.doshboard_page import *
from cy.common_code.GmailReceiver import *
from cy.common_code.common import *
from cy.common_code.GoogleOauth2 import Get_Gmail_API_Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from cy.code.create_account_ini import *



class Test_dashboard():
    def test_score_redirect(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        # score button
        dboard = Dashboard(driver=self.driver)
        dboard.check_score_btn()

    def test_Potential_btn(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        dboard = Dashboard(driver=self.driver)
        dboard.check_potential_btn()

    def test_overview_btn(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        dboard = Dashboard(driver=self.driver)
        dboard.check_overview_btn()

    def test_cal_score(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        dboard = Dashboard(driver=self.driver)
        dboard.cal_score()

    def test_check_score_comparison(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        dboard = Dashboard(driver=self.driver)
        score = dboard.cal_score()
        dboard.check_score_comparison(score)
