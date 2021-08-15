from time import sleep
from cy.code.base_code import Basecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from cy.common_code.read_download_data import Check_download_file


class History_page(Basecode):
    def check_history_page(self):
        self.driver.find_element(*self.path_history.history_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_history.history_title)
        assert 'History' == self.driver.find_element(*self.path_history.history_title).text
        assert 'Scan Results' == self.driver.find_element(*self.path_history.scan_result_title).text
        assert 'Overall' == self.driver.find_element(*self.path_history.filter).text
        self.driver.find_element(*self.path_history.filter).click()
        sleep(2)
        assert 'Overall' == self.driver.find_element(*self.path_history.filter_overall).text
        assert 'Cname_Test' == self.driver.find_element(*self.path_history.filter_domain).text
        self.driver.find_element(*self.path_history.filter_domain).click()
        sleep(2)
        assert 'Cname_Test' == self.driver.find_element(*self.path_history.filter).text
        self.driver.get_screenshot_as_file(
            rf'C:\Users\morris.lin\Documents\autopic\normal\{self.time}_history_page.png')


    def check_scan_result(self):
        self.driver.find_element(*self.path_history.history_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_history.history_title)
        self.driver.find_element(*self.path_history.domain_section).click()
        self.driver.find_element(*self.path_history.hacking_btn).click()
        self.driver.find_element(*self.path_history.h_issue_btn).click()
        sleep(2)
        assert len(self.driver.find_element(*self.path_history.h_desc_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.h_cwe_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.h_miti_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.h_recom_content).text) > 1
        self.driver.get_screenshot_as_file(
            rf'C:\Users\morris.lin\Documents\autopic\normal\{self.time}_scan_result.png')


    def check_recent_result(self):
        self.driver.find_element(*self.path_history.history_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_history.history_title)
        sleep(2)
        self.driver.find_element(*self.path_history.domain_section).click()
        self.driver.find_element(*self.path_history.overview_tab).click()
        self.driver.find_element(*self.path_history.recent_btn).click()
        self.driver.find_element(*self.path_history.r_issue_btn).click()
        sleep(2)
        assert len(self.driver.find_element(*self.path_history.r_desc_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.r_cwe_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.r_miti_content).text) > 1
        assert len(self.driver.find_element(*self.path_history.r_recom_content).text) > 1
        self.driver.get_screenshot_as_file(
            rf'C:\Users\morris.lin\Documents\autopic\normal\{self.time}_Recent_Vulnerabilities.png')


    def download_file(self):
        # options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0,
        #          'download.default_directory': 'C:/Users/morris.lin/Downloads'}
        # options.add_experimental_option('prefs', prefs)

        # self.driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
        self.driver.find_element(*self.path_history.history_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_history.domain_section)
        self.driver.find_element(*self.path_history.domain_section).click()
        self.driver.find_element(*self.path_history.overview_tab).click()
        self.driver.find_element(*self.path_history.download_btn).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_history.modal_cn_btn)
        # download CN PDF
        self.driver.find_element(*self.path_history.modal_cn_btn).click()
        self.driver.find_element(*self.path_history.modal_pdf_btn).click()
        self.driver.find_element(*self.path_history.modal_download_btn).click()
        sleep(12)
        # download EN excel
        self.driver.find_element(*self.path_history.download_btn).click()
        self.driver.find_element(*self.path_history.modal_en_btn).click()
        self.driver.find_element(*self.path_history.modal_excel_btn).click()
        self.driver.find_element(*self.path_history.modal_download_btn).click()
        sleep(6)


    @staticmethod
    def check_file_exist():
        check_file = Check_download_file()
        check_file.check_file_exist()
        check_file.open_pdf()
        check_file.open_excel()
        sleep(3)



