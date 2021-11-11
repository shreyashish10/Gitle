import pytest
import selenium
import time

import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.LoginPageData import LoginPageData
from pageObject.LoginPage import LoginPage
from pageObject.PartnerManagementPage import PartnerManagementPage
from utilities.BaseClass import BaseClass




class TestOne(BaseClass):

    def test_e2e(self,getData):
        actual_title="Asset Global"

        log = self.getLogger()


        log.info("entering user name")
        # self.driver.find_element_by_xpath("//input[@id='userid']").send_keys("D0X51244")
        lp = LoginPage(self.driver)
        #lp.login().send_keys("D0X51244")
        lp.login().send_keys(getData["userid"])

        log.info("pressing next entering user name")
        #self.driver.find_element_by_xpath("//button[@id='next-btn']").click()
        un = LoginPage(self.driver)
        un.usernext().click()
        #self.driver.implicitly_wait(2)
        time.sleep(4)
        #self.driver.implicitly_wait(5)


        log.info("Entering pass word")

        #self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Rm7E8dkmhq")
        self.verifythelink("password")
        pw = LoginPage(self.driver)
        #pw.pass_text().send_keys("Rm7E8dkmhq")
        pw.pass_text().send_keys(getData["password"])

        log.info("pressing next after submitting the password")
        #self.driver.find_element_by_xpath("//button[@id='loginSubmitButton']").click()
        pt_next = LoginPage(self.driver)
        pt_next.passnextbt().click()


        log.info("verifying the title "+ actual_title)
        expted_tit = self.driver.title
        assert actual_title == expted_tit
        time.sleep(5)

        log.info("changing language")
        self.driver.find_element_by_xpath("//span[@class='user-icon']").click()
        self.driver.implicitly_wait(5)
        log.info("selecting drop down for language")
        self.driver.find_element_by_xpath("//li[@class='dropdown-submenu']").click()
        self.driver.implicitly_wait(5)

        log.info("selecting language English")

        self.driver.find_element_by_xpath("//a[text()='angielski']").click()

        time.sleep(10)
        partnermagament_click = PartnerManagementPage(self.driver)
        partnermagament_click.click_partner_management().click()
        time.sleep(10)




    @pytest.fixture(params=LoginPageData.test_LoginPageData)
    def getData(self,request):
     return request.param




