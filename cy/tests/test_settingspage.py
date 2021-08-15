from cy.code.settings_page import *
from cy.code.sign_in import *
from cy.common_code.GmailReceiver import *
from cy.common_code.common import *
import pytest


# @pytest.mark.run_settings
class Test_settings:
    @pytest.mark.run_settings
    def test_check_value(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')

        # sign-in
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        # setting page
        settings = Settings(driver=self.driver)
        sleep(3)
        settings.check_settings_value()

    def test_change(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        # sign-in
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        # setting page
        settings = Settings(driver=self.driver)
        sleep(3)
        settings.change_industry_csize_cancel()
        settings.change_industry_csize_save()

    def test_reset_passed(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        # sign-in
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        # setting page
        settings = Settings(driver=self.driver)
        settings.reset_passwd()
        # re-sign-in
        self.driver = webdriver.Chrome('../chromedriver')
        # sign-in
        login = Sign_in(driver=self.driver)
        login.user_signin(resetflag='Yes')
