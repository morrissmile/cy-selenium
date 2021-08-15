from cy.common_code.common import *
from time import sleep
from cy.locator.signpage import *
from cy.common_code.GmailReceiver import *

from cy.locator.signpage import *
from cy.common_code.GmailReceiver import *
from cy.code.sign_in import *


class Test_Authpage():



    def test_signin_signout(self):
        self.driver = webdriver.Chrome('../chromedriver')

        #signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        #signout
        login.user_signout()
        sleep(3)


    def test_forgetpasswd(self):
        self.driver = webdriver.Chrome('../chromedriver')

        #goto login page
        login = Sign_in(driver=self.driver)
        login.forgetpasswd()
        sleep(5)
        login.resetpassword()
