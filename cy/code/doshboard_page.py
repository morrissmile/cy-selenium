from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from cy.code.base_code import Basecode


class Dashboard(Basecode):
    def check_score_btn(self):
        self.driver.find_element(*self.path_dashboard.section_home).click()
        sleep(2)
        # 因為按鈕是滑鼠在上面才會出現 要先用action chains 將滑鼠移到上面 (需要import)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.path_dashboard.dashboard_score)).perform()
        sleep(1)
        # 點擊隱藏的按紐 利用上的的action chains
        # score_bn = rf'document.getElementById("{self.path.score_button}").click()' #利用 JS點
        # self.driver.execute_script(score_bn)
        self.driver.find_element(*self.path_dashboard.score_button).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_dashboard.his_filter_value)
        assert 'Overall' == self.driver.find_element(*self.path_dashboard.his_filter_value).text


    def check_potential_btn(self):
        self.driver.find_element(*self.path_dashboard.section_home).click()
        self.driver.find_element(*self.path_dashboard.potential_threats).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_dashboard.his_filter_value)
        assert 'Overall' == self.driver.find_element(*self.path_dashboard.his_filter_value).text


    def check_overview_btn(self):
        self.driver.find_element(*self.path_dashboard.section_home).click()
        self.driver.find_element(*self.path_dashboard.new_threats_view).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_dashboard.his_filter_value)
        assert 'Overall' == self.driver.find_element(*self.path_dashboard.his_filter_value).text


    def cal_score(self):
        self.driver.find_element(*self.path_dashboard.section_home).click()
        h_risk_score = self.driver.find_element(*self.path_dashboard.h_risk).text
        m_risk_score = self.driver.find_element(*self.path_dashboard.m_risk).text
        l_risk_score = self.driver.find_element(*self.path_dashboard.l_risk).text
        total_score = 100 - 3 * int(h_risk_score) - 2 * int(m_risk_score) - int(l_risk_score)
        assert str(total_score) == self.driver.find_element(*self.path_dashboard.dashboard_score).text
        return total_score


    def check_score_comparison(self, score):
        self.driver.find_element(*self.path_dashboard.section_home).click()
        assert str(score) == self.driver.find_element(*self.path_dashboard.user_score).text
        assert '84' == self.driver.find_element(*self.path_dashboard.c_score).text
        assert '1~20' == self.driver.find_element(*self.path_dashboard.c_size).text
        assert 'Education Services' == self.driver.find_element(*self.path_dashboard.i_avg_lv).text
        assert '86' == self.driver.find_element(*self.path_dashboard.i_avg).text


# drag_and_drop()          拖動
# move_to_element()     滑鼠懸停
# perform()  執行所有ActionChains類中儲存的行為，可以理解為對整個操作的提交動作
