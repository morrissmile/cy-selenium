from cy.common_code.common import Base
from cy.locator.signpage import Signinpagepath
from cy.locator.scanpage import Scanpagepath
from cy.locator.dashboardpage import Dashboardpath
from cy.locator.settingspage import Settingspagepath
from cy.locator.historypage import Histoypagepath
from selenium import webdriver
from selenium.webdriver.common.by import By


class Basecode():
    def __init__(self, driver):
        #driver
        self.driver = driver
        # locator
        self.path_signin = Signinpagepath()
        self.path_dashboard = Dashboardpath()
        self.path_scan = Scanpagepath()
        self.path_settings = Settingspagepath()
        self.path_history = Histoypagepath()
        # readini
        base = Base()  # input scan url
        self.time = base.timestamp()
        self.account_ini = base.read_ini('account')  # input section
        self.test_env = base.read_ini('testenv')  # input section
        self.envinifile = base.read_env_ini(section='URL', env=self.test_env['env'])  # input section
        self.apifile = base.read_env_ini(section='internalAPI', env=self.test_env['env'])  # input section
        # print(self.apifile)
        self.base = base

