from time import sleep
from selenium.webdriver.common.keys import Keys
from cy.code.base_code import Basecode
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scan_page(Basecode):
    def wait_scan_finish(self):
        # customer login
        body = {
            "account": self.account_ini['mail'],
            "password": ""
        }
        headers = {
            'Content-Type': 'application/json',
            'Csrf-Token': 'test',
            'Connection': 'keep-alive'
        }
        customsign = requests.post(self.apifile['clogin'], headers=headers, json=body)
        customsign_result = customsign.json()
        print('custmsign api', customsign_result['status'])
        sleep(1)
        assert customsign_result['status'] == 0
        apicookie = customsign.cookies.get_dict()['ACCESS-TOKEN']

        # check scan status
        scan_status = 'pending'
        while scan_status == 'pending':
            customsign_cookies = {
                "ACCESS-TOKEN": apicookie,
                "CSRF-TOKEN": 'test',
                # "Domain": ''
            }
            get_scan_status = requests.get(self.apifile['scan_status'], headers=headers, cookies=customsign_cookies)
            scan_status = str(get_scan_status.json()['data']['task_state'])
            sleep(20)  # 每20秒打一次API確認狀態
        print('scan finish')

    def start_scan(self):
        self.driver.get(self.envinifile['scanpage'])
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.scanbutton)
        self.driver.find_element(*self.path_scan.scanbutton).click()
        assert 'https://www.example.com' == self.driver.find_element(*self.path_scan.Fri_domain).text
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.scan_pop_ok)
        sleep(2)
        self.driver.find_element(*self.path_scan.scan_pop_ok).click()
        sleep(3)
        assert 'Scanning' == self.driver.find_element(*self.path_scan.scan_status).text

        # wait scan finish
        Scan_page.wait_scan_finish(self)


    def add_domain(self, websitename, weburl):
        self.driver.get(self.envinifile['scanpage'])
        sleep(2)
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.Scan_page_section)
        sleep(1)
        self.driver.find_element(*self.path_scan.Scan_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.Add_domainbutton)
        self.driver.find_element(*self.path_scan.Add_domainbutton).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.pop_name)
        self.driver.find_element(*self.path_scan.pop_name).send_keys(websitename)
        self.driver.find_element(*self.path_scan.pop_url).send_keys(weburl)
        # self.driver.find_element(By.ID, self.path_scan.pop_name).send_keys('incorr')
        # self.driver.find_element(By.ID, self.path_scan.pop_url).send_keys('https://www.123.global')
        self.driver.find_element(*self.path_scan.pop_ok).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.tokenkey)
        assert "domain" in self.driver.find_element(*self.path_scan.tokenkey).get_attribute("value")

        # back scan list page and check status
        self.driver.find_element(*self.path_scan.back_icon).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.second_list_status)
        assert 'Verify' == self.driver.find_element(*self.path_scan.second_list_status).text
        sleep(1)


    def edit_unverify_domain(self):
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.Scan_page_section)
        self.driver.find_element(*self.path_scan.Scan_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.second_list_status)
        self.driver.find_element(*self.path_scan.second_list_status).click()
        sleep(3)
        self.driver.execute_script(
            'document.querySelector(\'#verify-page-edit-domain-button\').click()')  # 當前Button元素被界面上其他元素遮住了 的寫法
        # edit = self.driver.find_element(*self.path.edit_button)
        # self.driver.execute_script('arguments[0].click();', edit)   #當前Button元素被界面上其他元素遮住了 的寫法

        sleep(2)
        # 刪除舊內容
        # self.driver.execute_script("arguments[0].value=''", self.driver.find_element(*self.path.edit_pop_name))
        # self.driver.execute_script("arguments[0].value=''", self.driver.find_element(*self.path.edit_pop_url))
        self.driver.find_element(*self.path_scan.edit_pop_name).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(*self.path_scan.edit_pop_name).send_keys(Keys.DELETE)
        self.driver.find_element(*self.path_scan.edit_pop_url).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(*self.path_scan.edit_pop_url).send_keys(Keys.DELETE)
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.edit_pop_name)
        self.driver.find_element(*self.path_scan.edit_pop_name).send_keys('change incorr')
        self.driver.find_element(*self.path_scan.edit_pop_url).send_keys('https://www.google.com')
        sleep(1)
        self.driver.find_element(*self.path_scan.edit_pop_ok).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.edit_change_name)
        assert 'change incorr' == self.driver.find_element(*self.path_scan.edit_change_name).text
        assert 'https://www.google.com' == self.driver.find_element(*self.path_scan.edit_change_domain).text


    def del_domain(self):
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.Scan_page_section)
        self.driver.find_element(*self.path_scan.Scan_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.second_list_status)
        self.driver.find_element(*self.path_scan.second_list_status).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.delete_button)
        delete = self.driver.find_element(*self.path_scan.delete_button)
        self.driver.execute_script('arguments[0].click()', delete)
        sleep(2)
        assert 'Are you sure you want to delete the domain?' == self.driver.find_element(
            *self.path_scan.delete_confirm).text
        self.driver.find_element(*self.path_scan.delete_pop_ok).click()
        # 確認domain(element)已經不存在
        check_del_domain = self.base.getElementExistanceById(self.driver, self.path_scan.check_delete)
        assert False == check_del_domain


    def set_schedule(self):
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.Scan_page_section)
        self.driver.find_element(*self.path_scan.Scan_page_section).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.edit_icon)
        self.driver.find_element(*self.path_scan.edit_icon).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.edit_schedule_btn)
        self.driver.find_element(*self.path_scan.edit_schedule_btn).click()
        self.driver.find_element(*self.path_scan.edit_period).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.schedule_week)
        self.driver.find_element(*self.path_scan.schedule_week).click()
        self.driver.find_element(*self.path_scan.edit_time).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.schedule_time)
        self.driver.find_element(*self.path_scan.schedule_time).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.schedule_save)
        self.driver.find_element(*self.path_scan.schedule_save).click()
        assert 'Weekly' == self.driver.find_element(*self.path_scan.check_period).text
        assert '12:00 AM' in self.driver.find_element(*self.path_scan.check_time).text



    def verify_scan_2nd_domain(self):
        # customer login
        global getresourceid
        body = {
            "account": self.account_ini['mail'],
            "password": ""
        }
        headers = {
            'Content-Type': 'application/json',
            'Csrf-Token': 'test',
            'Connection': 'keep-alive'
        }
        customsign = requests.post(self.apifile['clogin'], headers=headers, json=body)
        customsign_result = customsign.json()
        print('custmsign api', customsign_result['status'])
        sleep(1)
        assert customsign_result['status'] == 0
        apicookie = customsign.cookies.get_dict()['ACCESS-TOKEN']
        # get domain id
        customsign_cookies = {
            "ACCESS-TOKEN": apicookie,
            "CSRF-TOKEN": 'test',
            # "Domain": 'cy-customer-api.sit.123.global'
        }
        getresourceid_api = requests.get(self.apifile['resource'], headers=headers, cookies=customsign_cookies)
        # {'data': [{'app_name': None, 'id': 578, 'is_verified': True, 'resource_type':
        # {'resource_type_name': 'domain'},
        # 'resource_url': 'https://www.example.com', 'state': 'verified', 'token_key': None},
        # {'app_name': 'qqq', 'id': 580, 'is_verified': False, 'resource_type': {'resource_type_name': 'domain'},
        # 'resource_url': 'http://', 'state': 'unverified',
        # 'token_key': 'domain-verification=e8b409891efa4ac8ae3c37474e3191d1'}], 'status': 0}

        # find the need verify website
        if getresourceid_api.json()['data'][1]['app_name'] == 'motest':
            getresourceid = getresourceid_api.json()['data'][1]['id']
        elif getresourceid_api.json()['data'][2]['app_name'] == 'motest':
            getresourceid = getresourceid_api.json()['data'][2]['id']
        # change verify status
        v_statusurl = self.apifile['v_status'] + rf'{getresourceid}/domain-verify-status'
        verify_body = {
            "is_verified": True,
            "state": "verified"
        }
        domainstatus = requests.patch(v_statusurl, headers=headers, json=verify_body, cookies=customsign_cookies)
        domainstatus_result = domainstatus.json()
        print('domainstatus api', domainstatus_result['status'])
        sleep(1)
        assert domainstatus_result['status'] == 0
        self.driver.refresh()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.scan_2ndbutton)
        self.driver.find_element(*self.path_scan.scan_2ndbutton).click()
        self.base.wait_element_display(driver=self.driver, locator=self.path_scan.scan_pop_ok)
        sleep(2)
        self.driver.find_element(*self.path_scan.scan_pop_ok).click()
        sleep(3)
        assert 'Scanning' == self.driver.find_element(*self.path_scan.scan_2ndstatus).text

    def check_scan_mail(self):
        mail_content = self.base.check_mail(mail_title="Scan successful", usermail=self.account_ini['mail'], env=self.test_env['env'])
        assert "Your Website scan is done!" in mail_content
