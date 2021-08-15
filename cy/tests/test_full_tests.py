from cy.code.create_account_ini import Create_acc
from cy.code.sign_in import Sign_in
from cy.code.scan_page import Scan_page
from cy.code.doshboard_page import Dashboard
from cy.code.history_page import History_page
from cy.code.settings_page import Settings
from cy.code.check_mail import test_mails
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import datetime

"""pytest use"""
@pytest.fixture()
def init_driver_signin(browser):
    driver = browser()
    login = Sign_in(driver=driver)
    login.user_signin()
    sleep(6)
    return driver


class Test_fulltest():
    @pytest.mark.run_scan
    def test_create_account(self):
        signup = Create_acc()
        signup.create_account()
        sleep(5)
        signup.verify_mail()
        signup.write_ini()

    @pytest.mark.run_scan
    def test_scan_full(self, init_driver_signin):
        self.driver = init_driver_signin
        """scan_defaulweb"""
        scan = Scan_page(driver=self.driver)
        sleep(2)
        scan.start_scan()
        """add_new_domain"""
        sleep(5)
        scan.add_domain(websitename='incorr', weburl='https://www.123.global')
        """edit_unverify_domain"""
        sleep(5)
        scan.edit_unverify_domain()
        """del_domain"""
        sleep(5)
        scan.del_domain()
        """set_schedule"""
        sleep(5)
        scan.set_schedule()
        """add domain and verify it"""
        scan.add_domain(websitename='motest', weburl='http://')
        scan.verify_scan_2nd_domain()
        sleep(2)
        self.driver.close()

    @pytest.mark.run_dashboard
    def test_dashboard_full_test(self, init_driver_signin):
        self.driver = init_driver_signin

        """score_redirect"""
        dboard = Dashboard(driver=self.driver)
        dboard.check_score_btn()
        """potential_btn"""
        sleep(5)
        dboard.check_potential_btn()

        """overview_btn"""
        sleep(5)
        dboard.check_overview_btn()

        """cal_score"""
        sleep(3)
        dboard.cal_score()

        """score_comparison"""
        sleep(3)
        score = dboard.cal_score()
        dboard.check_score_comparison(score)
        sleep(5)
        self.driver.close()

    """pytest -v -m "run_settings" test_full_tests.py"""
    @pytest.mark.run_settings
    def test_settings(self, init_driver_signin):
        self.driver = init_driver_signin

        """setting page"""
        settings = Settings(driver=self.driver)
        sleep(3)
        settings.check_settings_value()
        # change industry_c-size
        sleep(3)
        settings.change_industry_csize_cancel()
        sleep(2)
        settings.change_industry_csize_save()
        """reset passwd"""
        settings.reset_passwd()
        """re-sign-in"""
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        """sign-in"""
        login = Sign_in(driver=self.driver)
        login.user_signin(resetflag='Yes')
        self.driver.close()

    @pytest.mark.run_history
    def test_history(self, init_driver_signin):
        self.driver = init_driver_signin

        """history page"""
        history = History_page(driver=self.driver)
        history.check_history_page()
        history.check_scan_result()
        history.check_recent_result()
        history.download_file()
        sleep(3)
        print('download pass')
        history.check_file_exist()
        print('open file pass')

    # def test_others(self):
    #     self.driver = webdriver.Chrome(executable_path='../chromedriver')

    """test mail
    pytest -v -m "run_mails" test_full_tests.py"""
    @pytest.mark.run_mails
    def test_scan_mail(self):
        driver = None
        mail = test_mails(driver=driver)
        mail.scan_mail()

    @pytest.mark.run_mails
    def test_invite_mail(self):
        driver = None
        mail = test_mails(driver=driver)
        mail.invitation_mail()

    @pytest.mark.run_mails
    def test_reset_pw_mail(self):
        driver = None
        mail = test_mails(driver=driver)
        mail.reset_password_mail()

    @pytest.mark.run_mails
    def test_passwd_change_mail(self):
        driver = None
        mail = test_mails(driver=driver)
        mail.password_changed_mail()

