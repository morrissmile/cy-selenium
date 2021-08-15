from selenium import webdriver
from selenium.webdriver.common.by import By


class Scanpagepath:
    # 可以把By也寫入變數 但引用變數前面要加*
    Scan_page_section = (By.ID, "dashboard-sidebar-item-Scan")
    scanbutton = (By.XPATH, "//*[text()='Cname_Test']/parent::div/parent::div/parent::div//*[text()='Scan']")
    #/parent::div 往上找一層
    scan_directly = (By.XPATH, "//*[text()='Scan Directly ']")
    verifybutton = (By.XPATH, "//*[text()='Verify']/parent::div/parent::div/parent::div//*[text()='Verify']")
    tokenkey = (By.XPATH, '//textarea')
    Add_domainbutton = (By.XPATH, "//*[text()='Add Domain']")
    # Add_domainbutton = "//*[text()='scan_list_button_1']"
    back_icon = (By.XPATH, '//*[text()="Scan "]/parent::div//button')
    # scan_finish = '//*[text()="Scan completed successfully!"]'

    #first website list
    Fri_verify_status = (By.XPATH, "//*[text()='Verified']")
    Fri_domain = (By.XPATH, "//*[text()='https://www.example.com']")
    scan_status = (By.XPATH, "//*[text()='Cname_Test']/parent::div/parent::div/parent::div//*[text()='Scanning']")

    # 2nd domain scan
    scan_2ndbutton = (By.XPATH, "//*[text()='motest']/parent::div/parent::div/parent::div//*[text()='Scan']")  # /parent::div 往上找一層
    scan_2ndstatus = (By.XPATH, "//*[text()='motest']/parent::div/parent::div/parent::div//*[text()='Scanning']")

    #start scan pop module
    scan_pop_ok = (By.XPATH, "//*[text()='OK']")

    #add domain  & pop-up module
    second_list_status = (By.XPATH, "//*[text()='Verify']")
    pop_name = (By.ID, 'domain-page-app-name-input')
    pop_url = (By.ID, 'domain-page-domain-url-input')
    pop_ok = (By.XPATH, "//*[text()='OK']")

    #edit 2nd domain
    edit_button = (By.XPATH, "//*[text()='Edit Domain']")
    edit_pop_name = (By.ID, "domain-page-app-name-input")
    edit_pop_url = (By.ID, "domain-page-domain-url-input")
    edit_pop_ok = (By.XPATH, "//*[text()='OK']")
    edit_change_name = (By.XPATH, '//*[@data-test = "verify-page-app-name-text"]')
    edit_change_domain = (By.XPATH, '//*[text() = "Scan Website"]/following::div[1]')    #同一層的下一個用follwing

    #delete domain
    delete_button = (By.XPATH, "//*[text()='Delete Domain ']")
    delete_confirm = (By.XPATH, "//*[text()='Are you sure you want to delete the domain?']")
    delete_pop_ok = (By.XPATH, "//*[text()='OK']")
    check_delete = (By.XPATH, "//*[text()='change incorr']")

    #set schedule
    edit_icon = (By.XPATH, "//*[text()='Cname_Test']/parent::div/parent::div/parent::div//img/parent::div")
    edit_schedule_btn = (By.XPATH, "//*[text()='Edit']")
    edit_period = (By.XPATH, "//*[text()='Manual scan']")
    edit_time = (By.ID, "dashboard-scan-page-date-picker")
    schedule_week = (By.XPATH, "//*[text()='Weekly']")
    schedule_time = (By.XPATH, "//*[text()='00:00']")
    schedule_save = (By.XPATH, "//*[text()='Save']")
    check_period = (By.XPATH, "//*[text()='Weekly']")
    check_time = (By.XPATH, "//span[contains(., '12:00 AM')]")








