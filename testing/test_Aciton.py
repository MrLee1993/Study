# -*- coding： utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Test_Action:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_action(self):
        setups = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(setups)
        action.perform()
        time.sleep(3)
