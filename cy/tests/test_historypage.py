from cy.code.history_page import *
from cy.code.sign_in import Sign_in
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def init_driver():
    driver = webdriver.Chrome(executable_path='../chromedriver')
    login = Sign_in(driver=driver)
    login.user_signin()
    return driver

class Test_history():
    def test_check_page_download_files(self, init_driver):
        self.driver = init_driver
        sleep(5)
        history = History_page(driver=self.driver)
        history.check_history_page()

    def test_open_download_files(self, init_driver):
        self.driver = init_driver
        sleep(5)
        history = History_page(driver=self.driver)
        history.check_scan_result()
        history.check_recent_result()

    # def test_history(self):
    #     self.driver = webdriver.Chrome(executable_path='../chromedriver')
    #     login = Sign_in(driver=self.driver)
    #     login.user_signin()
    #     sleep(5)
    #     # history page
    #     history = History_page(driver=self.driver)
    #     history.check_history_page()
    #     history.check_scan_result()
    #     history.check_recent_result()
    #     history.download_file()
    #     sleep(3)
    #     print('download pass')
    #
    #     history.check_file_exist()
    #     print('open file pass')
