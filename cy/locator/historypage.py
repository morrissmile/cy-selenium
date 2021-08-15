from selenium import webdriver
from selenium.webdriver.common.by import By


class Histoypagepath:
    # 可以把By也寫入變數 但引用變數前面要加*
    history_page_section = (By.ID, "dashboard-sidebar-item-History")
    history_title = (By.XPATH, "//div[contains(@class, 'HistoryContainer')]/div[text()='History']")
    scan_result_title = (By.XPATH, "//div[text()='Scan Results ']")
    filter = (By.XPATH, "//span[@data-testid='history-page-filter-dropdown-value']")
    filter_overall = (By.XPATH, "//div[@data-testid='overall']")
    filter_domain = (By.XPATH, "//div[@data-testid='https://www.example.com']")

    domain_section = (By.XPATH, "//div[text()='Cname_Test']")
    overview_tab = (By.XPATH, "//*[text()='Overview ']")
    download_btn = (By.ID, "history-page-download-all-risk-report-button")

    # download modal
    modal_en_btn = (By.XPATH, "//button[text()='English']")
    modal_cn_btn = (By.XPATH, "//button[text()='中文']")
    modal_pdf_btn = (By.XPATH, "//button[text()='PDF']")
    modal_excel_btn = (By.XPATH, "//button[text()='Excel']")
    modal_download_btn = (By.ID, "modal-ok-button")

    # Scan results
    # hacking
    hacking_btn = (By.XPATH, "//div[text()='Hacking']/parent::div/parent::div//button")
    h_issue_btn = (By.XPATH, "//div[text()='Hacking']/parent::div[1]/parent::div[1]/parent::div[1]//div[1]/div[1]/div["
                             "1]/div[1]/div[1]/button")

    h_desc_content = (By.XPATH, "//div[text()='Hacking']/parent::div/parent::div/parent::div//*[contains(@class, "
                                "'VulnerabilityPanel')][1]//*[contains(@class, 'InnerPanelContentDescription')][1]")
    h_cwe_content = (By.XPATH, "//div[text()='Hacking']/parent::div/parent::div/parent::div//*[contains(@class, "
                               "'VulnerabilityPanel')][1]//*[contains(@class, 'InnerPanelContentDescription')][2]")
    h_miti_content = (By.XPATH, "//div[text()='Hacking']/parent::div/parent::div/parent::div//*[contains(@class, "
                                "'VulnerabilityPanel')][1]//*[contains(@class, 'InnerPanelContentDescription')][3]")
    h_recom_content = (By.XPATH, "//div[text()='Hacking']/parent::div/parent::div/parent::div//*[contains(@class, "
                                 "'VulnerabilityPanel')][1]//*[contains(@class, 'InnerPanelContentDescription')][4]")
    # Recent Vulnerabilities
    recent_btn = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div/parent::div//button")
    r_issue_btn = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div[1]/parent::div[1]"
                             "/parent::div[1]//div[1]/div[1]/div[1]/div[1]/div[1]/button")
    r_desc_content = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div/parent::div/parent::div//*["
                                "contains(@class, 'VulnerabilityPanel')][1]//*[contains(@class, "
                                "'InnerPanelContentDescription')][1]")
    r_cwe_content = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div/parent::div/parent::div//*["
                               "contains(@class, 'VulnerabilityPanel')][1]//*[contains(@class, "
                               "'InnerPanelContentDescription')][2]")
    r_miti_content = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div/parent::div/parent::div//*["
                                "contains(@class, 'VulnerabilityPanel')][1]//*[contains(@class, "
                                "'InnerPanelContentDescription')][2]")
    r_recom_content = (By.XPATH, "//div[text()='Recent Vulnerabilities']/parent::div/parent::div/parent::div//*["
                                 "contains(@class, 'VulnerabilityPanel')][1]//*[contains(@class, "
                                 "'InnerPanelContentDescription')][2]")


