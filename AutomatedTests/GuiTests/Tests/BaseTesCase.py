import logging
import unittest
import sys

from selenium.webdriver.support.ui import WebDriverWait


class BaseTestCase(unittest.TestCase):

    logging.basicConfig(level=logging.INFO)
    waitTime = 30

    def setUp(self, browser='chrome', env='dev'):
        from ..Helpers.Factories.SettingFactory import SettingsFactory
        from ..Helpers.Factories.DriverFactory import DriverFactory
        for arg in sys.argv:
            if "env" in arg:
                env = arg[arg.index('=')+1:]
        self.envSettings = SettingsFactory.getSettings(env)
        for arg in sys.argv:
            if "browser" in arg:
                browser = arg[arg.index('=')+1:]
        self.appDriver = DriverFactory.getWebdriver(browser)
        if browser.lower() != 'chrome':
            self.appDriver.maximize_window()
        self.appDriver.get(self.envSettings.Url)
        self.wait = WebDriverWait(self.appDriver, self.waitTime)
        from ..Pages.Login.LoginPage import LoginPage
        self.page = LoginPage(self.appDriver, browser)

    def tearDown(self):
        # self.ebayDriver.get_screenshot_as_file("{}.png".format(self._testMethodName))
        self.appDriver.quit()