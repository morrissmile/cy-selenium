from selenium.webdriver.common.by import By
from cy.code.create_account_ini import *
from cy.code.scan_page import *
import unittest

# class BaseTest(unittest.TestCase)

class Test_scan():
# class Test_scan(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Chrome('../chromedriver')

    def test_scan_defaulweb(self):
        self.driver = webdriver.Chrome('../chromedriver')

        #signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        #scan page
        scan = Scan_page(driver=self.driver)
        sleep(2)
        scan.start_scan()

    def test_add_new_domain(self):
        self.driver = webdriver.Chrome('../chromedriver')

        #signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        #add domain
        scan = Scan_page(driver=self.driver)
        scan.add_domain()


    def test_edit_unverify_domain(self):
        self.driver = webdriver.Chrome('../chromedriver')

        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        scan = Scan_page(driver=self.driver)
        scan.edit_unverify_domain()


    def test_del_domain(self):
        self.driver = webdriver.Chrome('../chromedriver')
        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
        scan = Scan_page(driver=self.driver)
        scan.del_domain()

    def test_set_schedule(self):
        self.driver = webdriver.Chrome('../chromedriver')
        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        scan = Scan_page(driver=self.driver)
        scan.set_schedule()
    def test_verify_scan_2nd_domain(self):
        self.driver = webdriver.Chrome('../chromedriver')
        # signin
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)

        scan = Scan_page(driver=self.driver)
        scan.add_domain(websitename='motest', weburl='http://')
        scan.verify_scan_2nd_domain()
        sleep(2)
