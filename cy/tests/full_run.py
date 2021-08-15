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


"""python use"""
class full_run():
    def test_scan_full(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.driver.maximize_window()

        """sign-in"""
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
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
        sleep(7)
        """add domain and verify it"""
        # scan.add_domain(websitename='motest', weburl='http://')
        # scan.verify_scan_2nd_domain()
        # sleep(2)
        scan.add_domain(websitename='motest', weburl='https://www.offices355.com')
        sleep(3)
        scan.verify_scan_2nd_domain()
        sleep(2)
        self.driver.close()

    def test_dashboard_full_test(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.driver.maximize_window()

        """sign-in"""
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(8)

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

    def test_settings(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.driver.maximize_window()

        """sign-in"""
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(6)

        """setting page"""
        settings = Settings(driver=self.driver)
        sleep(3)
        settings.check_settings_value()
        """change industry_c-size"""
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

    def test_history(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.driver.maximize_window()
        login = Sign_in(driver=self.driver)
        login.user_signin()
        sleep(5)
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

    def test_check_mail(self):
        driver = None
        mail = test_mails(driver=driver)
        mail.invitation_mail()
        mail.password_changed_mail()
        mail.reset_password_mail()
        mail.scan_mail()




if __name__ == "__main__":
    """signup"""
    # signup = Create_acc(mail='sit+uat60')  # input scan url  =>  scanurl=' ', mail ='none' => timestamp
    # signup = Create_acc(mail='sit+test62')
    signup = Create_acc()
    """input scan url  =>  scanurl='https://', mail ='none' => timestamp"""
    signup.create_account()
    sleep(5)
    signup.verify_mail()
    signup.write_ini()
    sleep(2)

    full_test = full_run()

    full_test.test_scan_full()
    print('===scan pass===')

    # full_test.test_dashboard_full_test()
    # print('===dashboard pass===')
    #
    # full_test.test_settings()
    #
    # full_test.test_history()
    # full_test.test_check_mail()

