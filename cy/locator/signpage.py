from selenium import webdriver
from selenium.webdriver.common.by import By

class Signinpagepath:
    # 可以把By也寫入變數 但引用變數前面要加*
    mail_input_field = (By.ID, 'login-email-input')
    password_input_field = (By.ID, 'login-password-input')
    Log_in_button = (By.XPATH, "//span[text()='Log in']")
    forgetpasswd_button = (By.XPATH, ".// *[text() = 'Forgot Password?']")
    verify_forgetpage = (By.XPATH, ".//*[text()='Forgot password? ']")
    forgetinput = (By.ID, 'reset-password-email-input')
    forgetbutton = (By.XPATH, "//*[text()='Confirm ']")
    back_btn = (By.XPATH, "//div[text()='Go back to login ']")
    verify_forgetsentpage = (By.XPATH, "//*[text()='Email sent']")

    # log out
    Avastar_button = (By.XPATH, '//div[contains(@class,"Avatar__Avatar")]')
    Logout_button = (By.XPATH, "//div[text()='Log out']")
