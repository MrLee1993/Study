# -*- coding： utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
from time import sleep


class TestWeChat():
    def setup(self):
        caps = {}
        caps['platform'] = 'Android'
        caps['deviceName'] = '8BNDU17722007089'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = 'true'
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化

        # 与服务端建立连接
        driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    """
        添加成员
    """

    def test_adduser(self):
        # 1、点击“通讯录”
        el1 = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        el1.click()

        sleep(2)

        # 2、点击“添加成员”
        el2 = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']")
        el2.click()

        # 3、点击“手动输入添加”，进入“添加成员”页
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        el3.click()

        el4 = self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']")
        el4.send_keys("测试1")

        el5 = self.self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']")
        el5.send_keys("18131165255")

        el6 = self.self.driver.find_element(MobileBy.XPATH, "//*[@text='手保存']")
        el6.click()

    def teardown(self):
        self.driver.quit()
