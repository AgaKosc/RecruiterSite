import logging

from selenium.webdriver.common.by import By

from ..BasePage import BasePage

class LoginPage(BasePage):

    UsernameInput = (By.ID, "id_username")
    PasswordInput = (By.ID, "id_password")
    LoginButton = (By.XPATH, "//button[text()='Log in']")
    SingInLink = (By.LINK_TEXT, "Sing up")

    WrongLoginErrorMessageText = 'Please enter a correct username and password. ' \
                                 'Note that both fields may be case-sensitive.'

    def __fillLoginForm(self, user):
        logging.info("Filling login form with data: {0}/{1}".format(user.login, user.password))
        self.waitUntilElementIsVisible(self.UsernameInput)
        self.driver.find_element(*self.UsernameInput).clear()
        self.driver.find_element(*self.UsernameInput).send_keys(user.login)
        self.driver.find_element(*self.PasswordInput).clear()
        self.driver.find_element(*self.PasswordInput).send_keys(user.password)

    def loginWithProperData(self, user):
        self.__fillLoginForm(user)
        self.driver.find_element(*self.LoginButton).click()
        from ..Recruiter.HomePage import HomePage
        return HomePage(self.driver, self.browser)

    def checkWrongLoginErrorMessage(self):
        logging.info("Checking error message after logging with wrong data")
        self.waitUntilElementIsVisible(self.ErrorMessage)
        currentErrorMessageText = self.driver.find_element(*self.ErrorMessage).text.strip()
        self.Assertion.assertEqual(self.WrongLoginErrorMessageText, currentErrorMessageText)

    def loginWithWrongData(self, user):
        self.__fillLoginForm(user)
        self.driver.find_element(*self.LoginButton).click()
        return self
