from selenium import webdriver
from selenium.webdriver.common.by import By

class Dashboardpath:
    # 可以把By也寫入變數 但引用變數前面要加*

    section_home = (By.ID, 'dashboard-sidebar-item-Home')
    dashboard_score = (By.XPATH, '//div[contains(@class, "SecurityScorePanelScoreText")]')
    score_button = (By.ID, 'dashboard-home-page-security-score-panel-hover-navigate-to-history-button')
    # new_threats_view = '//div[contains(@class, "NewlyAddViewMoreText") and text()="View more"]'
    new_threats_view = (By.ID, 'dashboard-home-page-newly-added-view-more-button')
    potential_threats = (By.ID, 'dashboard-home-potential-threats-view-more-button')
    h_risk = (By.XPATH, '//div[text()="High-risk"]/parent::div/*[contains(@class, "RiskNumberText")]')
    m_risk = (By.XPATH, '//div[text()="Medium-risk"]/parent::div/*[contains(@class, "RiskNumberText")]')
    l_risk = (By.XPATH, '//div[text()="Low-risk"]/parent::div/*[contains(@class, "RiskNumberText")]')
    cs_name = (By.XPATH, '//*[contains(@class, "ProductStatusSection")]/*[contains(@class, "CustomerNameText")]')
    his_filter_value = (By.XPATH, '//*[contains(@class, "Dropdown__DropdownValueDisplay")]')

    # Score Comparison
    user_score = (By.XPATH, '//*[text()="Your security score"]/parent::div'
                            '/parent::div/*[contains(@class, "ScoreSection")]')
    c_score = (By.XPATH, '//*[text()="Company size average "]/parent::div'
                         '/parent::div/*[contains(@class, "ScoreSection")]')
    c_size = (By.XPATH, '//*[text()="Company size average "]/parent::div/*[contains(@class, "ComparisonResult")]')
    i_avg_lv = (By.XPATH, '//*[text()="Industry average "]/parent::div/*[contains(@class, "ComparisonResult")]')
    i_avg = (By.XPATH, '//*[text()="Industry average "]/parent::div/parent::div/*[contains(@class, "ScoreSection")]')





