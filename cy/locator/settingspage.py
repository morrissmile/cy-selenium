from selenium import webdriver
from selenium.webdriver.common.by import By

class Settingspagepath:
    section_settings = (By.ID, 'dashboard-sidebar-item-Settings ')   # 可以把By也寫入變數 但引用變數前面要加* 要變成 *section_settings
    custom_name = (By.XPATH, '//div[contains(@class,"CompanyNameText")]')
    username = (By.XPATH, '//div[contains(@class,"ContactNameText")]')
    contact_mail = (By.XPATH, '//div[contains(@class,"ContactEmailText")]')
    edit_btn = (By.XPATH, '//div[text()="Edit"]')
    industry = (By.XPATH, '//span[contains(@data-testid,"industry")]')
    indu_Pharmaceutical = (By.XPATH, '//div[@data-testid= "dashboard-setting-page-industry-dropdown-menu"]//div[@data-testid="2"]')
    uat_indu_Pharmaceutical = (By.XPATH, '//div[@data-testid= "dashboard-setting-page-industry-dropdown-menu"]//div[@data-testid="23"]')

    c_size = (By.XPATH, '//span[contains(@data-testid,"company")]')
    c_size_sel = (By.XPATH, '//div[@data-testid= "setting-company-size-dropdown-menu"]//div[@data-testid="2"]')


    set_save_btn = (By.ID, 'dashboard-setting-page-save-button')
    set_cancel_btn = (By.ID, 'dashboard-setting-page-cancel-button')

    reset_passwd_btn = (By.ID, 'dashboard-setting-page-reset-password-button')
    pp_lnk = (By.XPATH, '//div[contains(@class,"Container")]/*[contains(@href,"privacy")]')
    tou_lnk = (By.XPATH, '//div[contains(@class,"Container")]/*[contains(@href,"terms")]')

