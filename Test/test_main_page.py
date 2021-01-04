__author__ = 'fathih'

import time
import pytest
import allure
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from Configuration.conftest import init_driver
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.FormPage import FormPage
from Pages.FormPage2 import FormPage2
from TestData.config import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

@allure.severity(allure.severity_level.NORMAL)
class Test_loginpage(BaseTest):

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    def test_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)

        # assert "Rent Vehicles" in self.driver.title
        # print("Assertion Test Pass")
        try:
            assert "Rent Vehicles" in self.driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "multicompetition" in self.driver.current_url

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(TestData.USERNAME)
        self.lp.enter_password(TestData.PASSWORD)
        verifyForgotPassword = self.driver.find_element(By.XPATH, Locators.forgot_password_xpath)
        assert verifyForgotPassword.text == Locators.forgot_password_message
        self.lp.click_login()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=2)
    def test_homepage(self):
        self.hp = HomePage(self.driver)
        self.hp.click_dropdown_menu()
        self.hp.select_registerdriver_page()
        # self.driver.execute_script("window.scrollBy(0,1000)", "")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    def test_fillform(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_drivername(TestData.DRIVER_NAME),time.sleep(2)
        self.ff.enter_mobile_number(TestData.DRIVER_MOBILE_NUMBER),time.sleep(2)
        self.ff.enter_email(TestData.DRIVER_EMAIL),time.sleep(2)
        self.ff.enter_driver_password(TestData.DRIVER_PASSWORD),time.sleep(2)
        self.ff.enter_nic(TestData.DRIVER_NIC),time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=4)
    def test_upload_licenece_copy_file(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_licence(TestData.FILE_UPLOAD_PATH),time.sleep(2)

    @pytest.mark.skip(reason="licence backcopy is not mendatory")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=5)
    def test_upload_licenece_backcopy_file(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_licence_back(TestData.FILE_UPLOAD_BACK_PATH),time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=6)
    def test_priority6_enter_vehicle_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_vehicle_number(TestData.VEHICLE_NUMBER)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=7)
    def test_vehicle_owner_radiobtn(self):
        element = self.driver.find_element_by_css_selector("input.is_vehicle_owner:nth-child(4)")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=8)
    def test_select_vehicle_type(self):
        self.ff = FormPage(self.driver)
        self.ff.select_vehicle_type(Locators.select_vehicle_type_xpath)
        self.driver.execute_script("window.scrollBy(0,500)", "")

    @pytest.mark.skip(reason="vehicle picture is not mendatory")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=9)
    def test_upload_vehicle_picture(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_vihicle_picture(TestData.FILE_UPLOAD_VEHICLE_PICTURE)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=10)
    def test_enter_engine_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_engine_number(TestData.ENGINE_NUMBER)

    @pytest.mark.skip(reason="chassis_number is not mendatory")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=11)
    def test_enter_chassis_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_chassis_number(TestData.CHASSIS_NUMBER)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=12)
    def test_hiring_times(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_prefer_hiring_from(TestData.HIRING_TIME_FROM)
        self.ff.enter_prefer_hiring_to(TestData.HIRING_TIME_TO)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=13)
    def test_upload_driver_registration(self):
        self.fp = FormPage2(self.driver)
        self.fp.upload_vehicle_registration_copy(TestData.FILE_UPLOAD_VEHICLE_REGISTRATION_COPY)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=14)
    def test_upload_driver_photo(self):
        self.fp = FormPage2(self.driver)
        self.fp.upload_driver_photo(TestData.FILE_UPLOAD_DRIVER_PHOTO)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=15)
    def test_enter_parking_location(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_parking_location(TestData.PARKING_LOCATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=16)
    def test_enter_hiring_location_from(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_prefer_hiring_from(TestData.HIRING_TIME_FROM)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=17)
    def test_enter_hiring_location_to(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_prefer_hiring_to(TestData.HIRING_TIME_TO)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=18)
    def test_select_hiring_location(self):
        self.fp = FormPage2(self.driver)
        self.fp.select_prefer_hiring_location(Locators.parking_location_xpath)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=19)
    def test_submit_details(self):
        element = self.driver.find_element_by_id("submitBtn")
        self.driver.execute_script("arguments[0].click();", element)
        verifyEmailId = self.driver.find_element(By.XPATH, Locators.verify_already_existing_email_xpath)
        assert verifyEmailId.text == TestData.EMAIL_VALIDATION































