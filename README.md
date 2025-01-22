#Basically the Sause.py code that acts as a class file

from selenium import webdriver
from selenium.webdriver.common.by import By

import booking.constants as const
import os

class Sauce(webdriver.Chrome):

    def __init__(self, driver_path=r"C:/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Sauce, self).__init__()

    def get_webpage(self):
        self.get(const.BASE_URL)

    def username_entry(self):
        username = self.find_element(By.ID, "user-name")
        username.click()
        username.clear()
        username.send_keys("standard_user")

    def password_entry(self):
        password = self.find_element(By.ID, "password")
        password.click()
        password.clear()
        password.send_keys("secret_sauce")

    def login_button(self):
        login = self.find_element(By.ID, "login-button")
        login.click()



