from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    ErrorMessage = (By.XPATH, "//div[@class='alert alert-danger']/p")
    WarningMessage = ()
    SuccessfullMessage = ()

    Assertion = TestCase()

    def __init__(self, driver, browser):
        self.driver = driver
        self.browser = browser
        self.waitTime = 30

    def waitTillJavaScriptsEnds(self):
        WebDriverWait(self.driver, self.waitTime).until(
            lambda driver: self.driver.execute_script("return jQuery.active == 0"))

    def waitForDocumentStateReady(self):
        WebDriverWait(self.driver, self.waitTime).until(
            lambda driver: self.driver.execute_script('return document.readyState=="complete";'))

    def waitUntilElementIsVisible(self, elementLocator):
        WebDriverWait(self.driver, self.waitTime).\
            until(expected_conditions.visibility_of_element_located(elementLocator))

    def waitUntilElementIsClickable(self, elementLocator):
        WebDriverWait(self.driver, self.waitTime). \
            until(expected_conditions.element_to_be_clickable(elementLocator))