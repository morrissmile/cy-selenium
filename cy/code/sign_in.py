from time import sleep
from cy.common_code.GmailReceiver import GmailReceiver
from selenium import webdriver
from selenium.webdriver.common.by import By
from cy.code.base_code import Basecode


class Sign_in(Basecode):

    def user_signin(self, resetflag='No'):
        self.driver.get(self.envinifile['signinpage'])
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.path_signin.mail_input_field).send_keys(self.account_ini['mail'])

        if resetflag == 'No':
            self.driver.find_element(*self.path_signin.password_input_field).send_keys(self.account_ini['password'])
        elif resetflag == 'Yes':
            self.driver.find_element(*self.path_signin.password_input_field).send_keys(self.account_ini['reset_passwd'])

        self.driver.find_element(*self.path_signin.Log_in_button).click()
        self.driver.implicitly_wait(10)
        # check page items
        user_name = self.driver.find_element(By.XPATH, "//div[text()='Testq Example']").text
        if user_name == 'Testq Example':
            print('sign in pass')
        else:
            print('sign in fail')
        sleep(4)

        # 避開 UAT環境第一次login會顯示key的問題
        if self.test_env['env'] == 'uat':
            self.driver.refresh()
        else:
            pass
        sleep(6)


    def resetpassword(self):

        self.driver.get(self.envinifile['signinpage'])
        self.driver.implicitly_wait(15)

        self.driver.find_element(*self.path_signin.forgetpasswd_button).click()
        sleep(1)
        self.base.wait_element_display(driver=self.driver, locator=self.path_signin.verify_forgetpage)
        assert "Forgot password?" == self.driver.find_element(*self.path_signin.verify_forgetpage).text

        self.driver.find_element(*self.path_signin.back_btn).click() # test back btn
        self.base.wait_element_display(driver=self.driver, locator=self.path_signin.forgetpasswd_button)
        self.driver.find_element(*self.path_signin.forgetpasswd_button).click()

        self.base.wait_element_display(driver=self.driver, locator=self.path_signin.forgetinput)
        self.driver.find_element(*self.path_signin.forgetinput).send_keys(self.account_ini['mail'])
        self.driver.find_element(*self.path_signin.forgetbutton).click()
        sleep(3)
        assert "Email sent" == self.driver.find_element(*self.path_signin.verify_forgetsentpage).text

        self.driver.find_element(*self.path_signin.back_btn).click()  # test back btn
        self.driver.close()

        sleep(5)
        self.base.reset_passwd_mail(mail_title='Reset password', usermail=self.account_ini['mail'],
                                    env=self.test_env['env'], passwd=self.account_ini['reset_passwd'])

    def user_signout(self):
        # Sign_in_out.user_signin(self)
        # read locator
        # super().__init__()
        # super().user_signin()
        self.driver.find_element(*path.Avastar_button).click()
        self.driver.find_element(*path.Logout_button).click()
        sleep(10)
