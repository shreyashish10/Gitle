from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:

    def __init__(self,driver):
        self.driver = driver



    user_name = (By.XPATH , "//input[@id='userid']")

    def login(self):
        return self.driver.find_element(*LoginPage.user_name)

    user_name_next = (By.XPATH , "//button[@id='next-btn']")

    def usernext(self):
        return self.driver.find_element(*LoginPage.user_name_next)


    password = (By.XPATH, "//input[@id='password']")

    def pass_text(self):
        return self.driver.find_element(*LoginPage.password)


    pass_next = (By.XPATH , "//button[@id='loginSubmitButton']")

    def passnextbt(self):
      return self.driver.find_element(*LoginPage.pass_next)