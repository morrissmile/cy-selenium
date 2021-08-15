from cy.code.base_code import Basecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Settings(Basecode):
    def check_settings_value(self):
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.section_settings)
        self.driver.find_element(*self.path_settings.section_settings).click()  # *可以解開tuple
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.custom_name)
        assert 'Cname_Test' == self.driver.find_element(*self.path_settings.custom_name).text
        assert 'Testq Example' == self.driver.find_element(*self.path_settings.username).text
        assert self.account_ini['mail'] == self.driver.find_element(*self.path_settings.contact_mail).text
        assert 'Education Services' == self.driver.find_element(*self.path_settings.industry).text
        assert '1~20' == self.driver.find_element(*self.path_settings.c_size).text

    def change_industry_csize_cancel(self):
        # change and cancel
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.section_settings)
        self.driver.find_element(*self.path_settings.section_settings).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.edit_btn).click()
        self.driver.find_element(*self.path_settings.industry).click()
        sleep(1)
        if self.test_env['env'] == 'uat':
            self.driver.find_element(*self.path_settings.uat_indu_Pharmaceutical).click()
        else:
            self.driver.find_element(*self.path_settings.indu_Pharmaceutical).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.c_size).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.c_size_sel).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.set_cancel_btn).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.industry)
        assert 'Education Services' == self.driver.find_element(*self.path_settings.industry).text
        assert '1~20' == self.driver.find_element(*self.path_settings.c_size).text
        print('cancel pass')

    def change_industry_csize_save(self):
        # change and save
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.section_settings)
        self.driver.find_element(*self.path_settings.section_settings).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.edit_btn).click()
        self.driver.find_element(*self.path_settings.industry).click()
        sleep(1)
        if self.test_env['env'] == 'uat':
            self.driver.find_element(*self.path_settings.uat_indu_Pharmaceutical).click()
        else:
            self.driver.find_element(*self.path_settings.indu_Pharmaceutical).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.c_size).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.c_size_sel).click()
        sleep(1)
        self.driver.find_element(*self.path_settings.set_save_btn).click()
        sleep(2)
        # 抓元件的style
        test1 = self.driver.find_element(*self.path_settings.industry).value_of_css_property('cursor')
        self.base.wait_element_display(driver=self.driver, locator=self.path_settings.industry)
        assert 'Pharmaceutical' == self.driver.find_element(*self.path_settings.industry).text
        assert '51~200' == self.driver.find_element(*self.path_settings.c_size).text

        # check dashboard
        self.driver.find_element(*self.path_dashboard.section_home).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_dashboard.c_size)
        assert '51~200' == self.driver.find_element(*self.path_dashboard.c_size).text
        assert 'Pharmaceutical' == self.driver.find_element(*self.path_dashboard.i_avg_lv).text
        print('save pass')

    def reset_passwd(self):
        self.driver.find_element(*self.path_settings.section_settings).click()
        sleep(3)
        self.driver.find_element(*self.path_settings.reset_passwd_btn).click()
        sleep(15)
        self.driver.close()
        sleep(15)
        self.base.reset_passwd_mail(mail_title='Reset password', usermail=self.account_ini['mail'],
                                    env=self.test_env['env'], passwd=self.account_ini['reset_passwd'])

    def check_PP_TOU(self):
        pass
