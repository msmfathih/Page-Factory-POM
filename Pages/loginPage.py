__author__ = 'fathih'

from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.loginbtn_id = Locators.loginbtn_id

    # define locators dictionary where key name will became WebElement using PageFactory
    # locators = {
    #     "edtUserName": ('ID', 'email'),
    #     "edtPassword": ('ID', 'password'),
    #     "btnSignIn": ('ID', 'btnLogin'),
    # }
    #
    # def enter_username(self):
    #     # set_text(), click_button() methods are extended methods in PageFactory
    #     self.edtUserName.set_text("admin@gmail.com")  # edtUserName become class variable using PageFactory
    #
    # def enter_password(self):
    #     self.edtPassword.set_text("admin@123")
    #
    # def click_login(self):
    #     self.btnSignIn.click_button()

    # def login(self):
    #     # set_text(), click_button() methods are extended methods in PageFactory
    #     self.UserName.set_text("admin@gmail.com")  # edtUserName become class variable using PageFactory
    #     self.Password.set_text("admin@123")
    #     self.LogIn.click_button()

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.loginbtn_id).click()





