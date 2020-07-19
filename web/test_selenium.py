# -*- coding： utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()
        print("执行完成")

    def test_name(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        time.sleep(5)

    def test_wework(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
