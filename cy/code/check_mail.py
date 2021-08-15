from cy.code.base_code import Basecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class test_mails(Basecode):

    def scan_mail(self):
        scan_mail_content = self.base.check_mail(mail_title="Scan successful", usermail=self.account_ini['mail'],
                                                 env=self.test_env['env'])
        assert "Your Website scan is done!" in scan_mail_content
        print('======scan finish mail pass======\n\n')


    def reset_password_mail(self):
        reset_mail_content = self.base.check_mail(mail_title="Reset password", usermail=self.account_ini['mail'],
                                                  env=self.test_env['env'])
        assert "We've received a request to reset your account password. Please click on the link below to set a new " \
               "passowrd. If you didn't make this request, please contact us right away so we can ensure the security " \
               "of your account." in reset_mail_content
        print('======reset pw mail pass======\n\n')

    def password_changed_mail(self):
        change_pw_mail_content = self.base.check_mail(mail_title="Password changed", usermail=self.account_ini['mail'],
                                                      env=self.test_env['env'])
        assert "Password successfully changed!" in change_pw_mail_content
        print('======pw change mail pass======\n\n')

    def invitation_mail(self):
        invite_mail_content = self.base.check_mail(mail_title="invitation", usermail=self.account_ini['mail'],
                                                   env=self.test_env['env'])
        assert "Welcome to platform" in invite_mail_content
        print('======invite mail pass======\n\n')


if __name__ == "__main__":
    driver = None
    a = test_mails(driver=driver)
    a.invitation_mail()
    a.password_changed_mail()
    a.reset_password_mail()
    a.scan_mail()
