from selenium.webdriver.common.by import By
from selenium import webdriver

class PartnerManagementPage:

    def __init__(self,driver):
        self.driver = driver

    partner_management_homepage = (By.XPATH, "//p[text()=' Partner Management ']")

    def click_partner_management(self):
        return self.driver.find_element(*PartnerManagementPage.partner_management_homepage)
